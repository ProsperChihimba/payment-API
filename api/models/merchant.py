from api.utils.database import db
#from marshmallow_sqlalchemy import ModelSchema
from marshmallow_sqlalchemy import ModelSchema
from marshmallow import fields

#merchant table model
class Merchant(db.Model):
    __tablename__ = 'merchant'

#merchant table fields
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    trading_name = db.Column(db.String(80), nullable=False)
    industry = db.Column(db.String(80), nullable=False)
    category = db.Column(db.String(80), nullable=False)
    busness_type = db.Column(db.String(80), nullable=False)
    legal_busness_name = db.Column(db.String(80))
    description = db.Column(db.String(80), nullable=False)
    general_email = db.Column(db.String(80), nullable=False)
    private_key = db.Column(db.String(80), nullable=False)
    public_key = db.Column(db.String(80), nullable=False)


    def __init__(self, trading_name, industry, category, busness_type, legal_busness_name, description, general_email, private_key, public_key):
        self.trading_name = trading_name
        self.industry = industry
        self.category = category
        self.busness_type = busness_type
        self.legal_busness_name = legal_busness_name
        self.description = description
        self.general_email = general_email
        self.private_key = private_key
        self.public_key = public_key


    def create(self):
        db.session.add(self)
        db.session.commit()
        return self

#mechant table with flask marshmallow
class MerchantSchema(ModelSchema):
    class Meta(ModelSchema.Meta):
        model = Merchant
        sqla_session = db.session
    
    id = fields.Number(dump_only=True)
    trading_name = fields.String(required=True)
    industry = fields.String(required=True)
    category = fields.String(required=True)
    busness_type = fields.String(required=True)
    legal_busness_name = fields.String(required=True)
    description = fields.String(required=True)
    general_email = fields.String(required=True)
    private_key = fields.String(required=True)
    public_key = fields.String(required=True)