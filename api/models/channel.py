from api.utils.database import db
from marshmallow_sqlalchemy import ModelSchema
from marshmallow import fields

#channel table model
class Channel(db.Model):
    __tablename__ = 'channels'

#channel table fields
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    provider_name = db.Column(db.String(50), nullable=False)
    provider_code = db.Column(db.String(50), nullable=False)


    def __init__(self, provider_name, provider_code):
        self.provider_name = provider_name
        self.provider_code = provider_code
    
    
    def create(self):
        db.session.add(self)
        db.session.commit()
        return self

#channel database with flask marshmallow
class ChannelSchema(ModelSchema):
    class Meta(ModelSchema.Meta):
        model = Channel
        sqla_session = db.session
    
    id = fields.Number(dump_only=True)
    provider_name = fields.String(required=True)
    provider_code = fields.String(required=True)