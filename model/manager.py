from app import db, ma, bcrypt
from sqlalchemy.dialects.sqlite import BLOB

from model.user import User


class Manager(db.Model):

    def __init__(self, manager_name, password):
        super(Manager, self).__init__(manager_name=manager_name)
        self.hashed_password = bcrypt.generate_password_hash(password)

    manager_id = db.Column(db.Integer, primary_key=True)
    manager_name = db.Column(db.String(30), unique=True)
    hashed_password = db.Column(db.String(128))


class ManagerSchema(ma.Schema):
    class Meta:
        fields = ("manager_id", "manager_name", "password")
        model = Manager


manager_schema = ManagerSchema()
