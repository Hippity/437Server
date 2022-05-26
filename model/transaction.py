from app import db, ma, bcrypt
from sqlalchemy.dialects.sqlite import BLOB


class Transaction(db.Model):

    def __init__(self, user_id, item_id, date, price, quantity, status):
        super(Transaction, self).__init__(user_id=user_id)
        super(Transaction, self).__init__(item_id=item_id)
        super(Transaction, self).__init__(date=date)
        super(Transaction, self).__init__(price=price)
        super(Transaction, self).__init__(quantity=quantity)
        super(Transaction, self).__init__(status=status)

    user_id = db.Column(db.Integer, primary_key=True)
    item_id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.DateTime, primary_key=True)
    price = db.Column(db.Float)
    quantity = db.Column(db.Integer)
    status = db.Column(db.Integer)


class TransactionSchema(ma.Schema):
    class Meta:
        fields = ("user_id", "item_id", "date", "price", "quantity", "status")
        model = Transaction


transaction_schema = TransactionSchema()
transactions_schema = TransactionSchema(many=True)
