from models import db


class Model(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    brand_id = db.Column(db.Integer, db.ForeignKey('brand.id'))
    name = db.Column(db.String(256), index=True, unique=True)
