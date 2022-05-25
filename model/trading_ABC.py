from app import db, ma, bcrypt
from sqlalchemy.dialects.sqlite import BLOB


class TradingABC(db.Model):

    def __init__(self, sender_id, receiver_id, date, amount):
        super(TradingABC, self).__init__(sender_id=sender_id)
        super(TradingABC, self).__init__(receiver_id=receiver_id)
        super(TradingABC, self).__init__(date=date)
        super(TradingABC, self).__init__(amount=amount)

    sender_id = db.Column(db.Integer, primary_key=True)
    receiver_id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.Date, primary_key=True)
    amount = db.Column(db.Float)


class TradingABCSchema(ma.Schema):
    class Meta:
        fields = ("user_id", "item_id", "date", "price", "quantity", "status")
        model = TradingABC


trading_abc_schema = TradingABCSchema()
trading_abcs_schema = TradingABCSchema(many=True)
