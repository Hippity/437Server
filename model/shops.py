from app import db, ma, bcrypt
from sqlalchemy.dialects.sqlite import BLOB

class Shops(db.Model):

    def __init__(self, shop_id, manager_id, shop_name, location):
        super(User, self).__init__(shop_id=manager_name)
        super(User, self).__init__(manager_id=manager_name)
        super(User, self).__init__(shop_name=shop_name)
        super(User, self).__init__(location=location)

    shop_id = db.Column(db.Integer, primary_key=True)
    manager_id = db.Column(db.String(30), primary_key=True)
    shop_name = db.Column(db.String(30))
    location = db.Column(db.String(45))




class UserSchema(ma.Schema):
    class Meta:
        fields = ("shop_id", "manager_id", "shop_name", "location")
        model = Shops


user_schema = ShopsSchema()