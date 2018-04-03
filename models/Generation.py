from models import db

class Generation(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(256), index=True)
    model_id = db.Column(db.Integer, db.ForeignKey('model.id'))
    year_begin = db.Column(db.String(128), index=True)
    year_end = db.Column(db.String(128), index=True)
    series = db.relationship('Series', backref='generation', lazy='dynamic')
