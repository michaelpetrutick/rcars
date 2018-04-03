from models import db


class Model(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    brand_id = db.Column(db.Integer, db.ForeignKey('brand.id'))
    name = db.Column(db.String(256), index=True)
    generation = db.relationship('Generation', backref='model', lazy='dynamic')
    series = db.relationship('Series', backref='model', lazy='dynamic')
    modifications = db.relationship('Modifications', backref='model', lazy='dynamic')


    def __repr__(self):
        return '<Model {}>'.format(self.name)