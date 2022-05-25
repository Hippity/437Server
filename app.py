import datetime
from db_config import DB_CONFIG
from flask import Flask, request, jsonify
from flask_bcrypt import Bcrypt
from flask_cors import CORS
from flask_marshmallow import Marshmallow
from flask_sqlalchemy import SQLAlchemy
from flask import abort
import jwt

SECRET_KEY = "b'|\xe7\xbfU3`\xc4\xec\xa7\xa9zf:}\xb5\xc7\xb9\x139^3@Dv'"
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = DB_CONFIG
CORS(app)
db = SQLAlchemy(app)
ma = Marshmallow(app)
bcrypt = Bcrypt(app)

from model.user import User, user_schema


def create_token(user_id):
    payload = {
        'exp': datetime.datetime.utcnow() + datetime.timedelta(days=4),
        'iat': datetime.datetime.utcnow(),
        'sub': user_id
    }
    return jwt.encode(
        payload,
        SECRET_KEY,
        algorithm='HS256'
    )


def extract_auth_token(authenticated_request):
    auth_header = authenticated_request.headers.get('Authorization')
    if auth_header:
        try:
            return auth_header.split(" ")[1]
        except IndexError:
            return None

    else:
        return None


def decode_token(token):
    payload = jwt.decode(token, SECRET_KEY, 'HS256')
    return payload


@app.route('/hello', methods=['GET'])
def hello_world():
    return "Hello World!"


@app.route("/signUp", methods=['POST'])
def signUp():
    user_id = request.json["user_id"]
    user_name = request.json["user_name"]
    user_email = request.json["email"]
    password = request.json["password"]
    balance = 0
    image = ""
    new_user = User(user_id, user_name, user_email, password, balance)

    db.session.add(new_user)
    db.session.commit()

    return jsonify(user_schema.dump(new_user))


@app.route("/authentication", methods=["POST"])
def auth():
    user_id = request.json["user_id"]
    password = request.json["password"]
    if not user_id and not password:
        abort(400)

    user = User.query.filter_by(user_id=user_id).first()

    if user is None:
        abort(403)

    passMatch = bcrypt.check_password_hash(user.hashed_password, password)

    if not passMatch:
        abort(403)

    tok = create_token(user_id)
    username = user.user_name
    username_initial = username[0].upper()

    payload = decode_token(tok)

    return jsonify(token=tok, user_name=username, user_initial=username_initial, balance=user.balance,
                   payload_id=payload['sub'])


@app.route("/credentials", methods=["POST"])
def credentials():
    tok = request.json["token"]
    payload = decode_token(tok)
    user = User.query.filter_by(user_id=payload['sub']).first()

    user_id = payload['sub']
    username = user.user_name
    username_initial = username[0].upper()
    userbalance = user.balance

    return jsonify(user_id=user_id, user_name=username, user_initial=username_initial, balance=userbalance)

@app.route("/addcoins", methods=["PUT"])
def addcoins():
    user_id = request.json["user_id"]
    coins = request.json["coins"]
    user = User.query.get(user_id)

    if user is None:
        abort(403)
    else:
        user.balance = user.balance + int(coins)
        db.session.commit()

    return jsonify(user_schema.dump(user)), 200
