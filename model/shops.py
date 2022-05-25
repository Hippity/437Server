from sqlalchemy import ForeignKey

from app import db, ma, bcrypt
from sqlalchemy.dialects.sqlite import BLOB

from model import manager

class Shops(db.Model):

    def __init__(self, shop_id, manager_id, shop_name, location, img):
        super(Shops, self).__init__(shop_id=shop_id)
        super(Shops, self).__init__(manager_id=manager_id)
        super(Shops, self).__init__(shop_name=shop_name)
        super(Shops, self).__init__(location=location)
        super(Shops, self).__init__(img=img)

    shop_id = db.Column(db.Integer, primary_key=True)
    manager_id = db.Column(db.String(30))
    shop_name = db.Column(db.String(30))
    location = db.Column(db.String(45))
    img = db.Column(db.Text)


class ShopsSchema(ma.Schema):
    class Meta:
        fields = ("shop_id", "manager_id", "shop_name", "location", "img")
        model = Shops


shop_schema = ShopsSchema()
shops_schema = ShopsSchema(many=True)
