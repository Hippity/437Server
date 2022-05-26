from app import db, ma, bcrypt
from sqlalchemy.dialects.sqlite import BLOB


class PostedItem(db.Model):

    def __init__(self, user_id, category, item_name, img, description, price, quantity, date):
        super(PostedItem, self).__init__(user_id=user_id)
        # super(PostedItem, self).__init__(item_id=item_id)
        super(PostedItem, self).__init__(category=category)
        super(PostedItem, self).__init__(item_name=item_name)
        super(PostedItem, self).__init__(img=img)
        super(PostedItem, self).__init__(description=description)
        super(PostedItem, self).__init__(price=price)
        super(PostedItem, self).__init__(quantity=quantity)
        super(PostedItem, self).__init__(date=date)

    user_id = db.Column(db.Integer, primary_key=True)
    item_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    category = db.Column(db.String(30))
    item_name = db.Column(db.String(45))
    img = db.Column(db.Text)
    description = db.Column(db.Text)
    price = db.Column(db.Float)
    quantity = db.Column(db.Integer)
    date = db.Column(db.Date)


class PostedItemSchema(ma.Schema):
    class Meta:
        fields = ("user_id", "item_id", "category", "item_name", "img", "description", "price", "quantity", "date")
        model = PostedItem


posted_item_schema = PostedItemSchema()
posted_items_schema = PostedItemSchema(many=True)
