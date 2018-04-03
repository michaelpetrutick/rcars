from models import db
from datetime import datetime

class Generation(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(256), index=True, unique=True)
    model_id = db.Column(db.Integer, db.ForeignKey('model.id'))
    year_begin = db.Column(db.DateTime, index=True, default=datetime.utcnow)
    year_end = db.Column(db.DateTime, index=True, default=datetime.utcnow)
