from app import db, ma, bcrypt
from sqlalchemy.dialects.sqlite import BLOB


class ShopItems(db.Model):

    def __init__(self, item_id, shop_id, item_name, img, description, price, quantity):
        super(ShopItems, self).__init__(item_id=item_id)
        super(ShopItems, self).__init__(shop_id=shop_id)
        super(ShopItems, self).__init__(item_name=item_name)
        super(ShopItems, self).__init__(img=img)
        super(ShopItems, self).__init__(description=description)
        super(ShopItems, self).__init__(price=price)
        super(ShopItems, self).__init__(quantity=quantity)

    item_id = db.Column(db.Integer, primary_key=True)
    shop_id = db.Column(db.Integer, primary_key=True)
    item_name = db.Column(db.String(30))
    img = db.Column(db.Text)
    description = db.Column(db.Text)
    price = db.Column(db.Float)
    quantity = db.Column(db.Integer)


class ShopItemsSchema(ma.Schema):
    class Meta:
        fields = ("item_id", "shop_id", "item_name", "img", "description", "price", "quantity")
        model = ShopItems


shop_item_schema = ShopItemsSchema()
shop_items_schema = ShopItemsSchema(many=True)
