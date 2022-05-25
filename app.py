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
from model.manager import Manager, manager_schema
from model.shops import Shops, shop_schema, shops_schema
from model.shop_items import ShopItems, shop_item_schema, shop_items_schema
from model.posted_items import PostedItem, posted_item_schema, posted_items_schema
from model.transaction import Transaction, transaction_schema, transactions_schema
from model.trading_ABC import TradingABC, trading_abc_schema, trading_abcs_schema


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
    role = 0
    new_user = User(user_id, user_name, user_email, password, balance, role)

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


@app.route("/shops", methods=["GET"])
def shops():
    shops_all = Shops.query.all()
    return jsonify(shops_schema.dump(shops_all)), 200


@app.route("/shop_items", methods=["GET", "POST"])
def shop_items():
    shop_id = request.json["shop_id"]
    shop_items_list = ShopItems.query.filter_by(shop_id=shop_id)
    return jsonify(shop_items_schema.dump(shop_items_list))


@app.route("/shop_item", methods=["GET", "POST"])
def shop_item():
    item_id = request.json["item_id"]
    item = ShopItems.query.filter_by(item_id=item_id).first()
    return jsonify(shop_item_schema.dump(item))


@app.route("/add_to_cart", methods=["POST"])
def add_to_cart():
    user_id = request.json["user_id"]
    item_id = request.json["item_id"]
    date = datetime.date.today()
    item = ShopItems.query.filter_by(item_id=item_id).first()
    price = item.price
    quantity = request.json["quantity"]
    status = 0

    item_added = Transaction(user_id, item_id, date, price, quantity, status)

    db.session.add(item_added)
    db.session.commit()

    return jsonify(transaction_schema.dump(item_added))


@app.route("/buy_in_cart", methods=["PUT"])
def buy_in_cart():
    user_id = request.json["user_id"]
    item_id = request.json["item_id"]
    date = request.json["date"]
    item = ShopItems.query.filter_by(item_id=item_id).first()
    price = item.price
    quantity = request.json["quantity"]

    item_in_transaction = Transaction.query.filter_by(user_id=user_id, item_id=item_id, date=date).first()

    user = User.query.get(user_id)

    user.balance = user.balance - int(price) * int(quantity)
    item.quantity = item.quantity - int(quantity)
    item_in_transaction.status = 1
    item_in_transaction.quantity = quantity

    db.session.commit()

    return jsonify({
        "shop_items": shop_item_schema.dump(item),
        "transaction": transaction_schema.dump(item_in_transaction),
        "user": user_schema.dump(user)
    })


@app.route("/search", methods=["GET", "POST"])
def search():
    item_search = request.json["item_search"]
    if len(item_search) == 0:
        items = ShopItems.query.all()
    else:
        search_query = "%{}%".format(item_search)
        items = ShopItems.query.filter(ShopItems.item_name.like(search_query)).all()

    return jsonify(shop_items_schema.dump(items))
