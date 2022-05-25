from app import db, ma, bcrypt
from sqlalchemy.dialects.sqlite import BLOB

from model.user import User


class Manager(db.Model):

    def __init__(self, manager_id, manager_name, password):
        super(User, self).__init__(manager_name=manager_name)
        self.hashed_password = bcrypt.generate_password_hash(password)

    id = db.Column(db.Integer, primary_key=True)
    user_name = db.Column(db.String(30), unique=True)
    hashed_password = db.Column(db.String(128))
    balance = db.Column(db.Integer)


class ManagerSchema(ma.Schema):
    class Meta:
        fields = ("id", "manager_name", "password")
        model = Manager


user_schema = ManagerSchema()
