from api.utils.database import db
from marshmallow_sqlalchemy import ModelSchema
from marshmallow import fields

#transaction table model
class Transaction(db.Model):
    __tablename__ = 'transaction'

#transaction table fields
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    transaction_reference = db.Column(db.String(80), nullable=False)
    amount = db.Column(db.Integer, nullable=False)
    merchant_id = db.Column(db.Integer, db.ForeignKey('merchant.id'), nullable=False)
    channel_id = db.Column(db.Integer, db.ForeignKey('channels.id'), nullable=False)
    currency = db.Column(db.String(20), nullable=False)
    transaction_date = db.Column(db.String(80), nullable=False)
    status = db.Column(db.String(50), nullable=False)
    message = db.Column(db.String(80), nullable=False)
    customer_id = db.Column(db.Integer, nullable=False)
    first_name = db.Column(db.String(80), nullable=False)
    last_name = db.Column(db.String(80), nullable=False)
    email = db.Column(db.String(80), nullable=False)
    customer_code = db.Column(db.String(50), nullable=False)
    number_used = db.Column(db.String(50), nullable=False)
    channel = db.Column(db.String(50), nullable=False)

    def __init__(self, transaction_reference, amount, merchant_id, channel_id, currency, transaction_date, status, message, customer_id, first_name, last_name, email, customer_code, number_used, channel):
        self.transaction_reference = transaction_reference
        self.amount = amount
        self.merchant_id = merchant_id
        self.channel_id = channel_id
        self.currency = currency
        self.transaction_date = transaction_date
        self.status = status
        self.message = message
        self.customer_id = customer_id
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.customer_code = customer_code
        self.number_used = number_used
        self.channel = channel
    

    def create(self):
        db.session.add(self)
        db.session.commit()
        return self

#transaction table with flask marshmallow
class TransactionSchema(ModelSchema):
    class Meta(ModelSchema.Meta):
        model = Transaction
        sqla_session = db.session
    
    id = fields.Number(dump_only=True)
    transaction_reference = fields.String(required=True)
    amount = fields.Integer(required=True)
    merchant_id = fields.Integer(required=True)
    channel_id = fields.Integer(required=True)
    currency = fields.String(required=True)
    transaction_date = fields.String(required=True)
    status = fields.String(required=True)
    message = fields.String(required=True)
    customer_id = fields.Integer(required=True)
    first_name = fields.String(required=True)
    last_name = fields.String(required=True)
    email  = fields.String(required=True)
    customer_code = fields.String(required=True)
    number_used = fields.String(required=True)
    channel = fields.String(required=True)