from app import db, ma, bcrypt
from sqlalchemy.dialects.sqlite import BLOB


class User(db.Model):

    def __init__(self, user_id, user_name, email, password, balance):
        super(User, self).__init__(user_id=user_id)
        super(User, self).__init__(user_name=user_name)
        super(User, self).__init__(email=email)
        self.hashed_password = bcrypt.generate_password_hash(password)
        super(User, self).__init__(balance=balance)

    user_id = db.Column(db.Integer, primary_key=True)
    user_name = db.Column(db.String(30))
    email = db.Column(db.String(30))
    hashed_password = db.Column(db.String(128))
    balance = db.Column(db.Integer)


class UserSchema(ma.Schema):
    class Meta:
        fields = ("user_id", "user_name", "email", "password", "balance")
        model = User


user_schema = UserSchema()
