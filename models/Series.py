from models import db


class Series(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    model_id = db.Column(db.Integer, db.ForeignKey('model.id'))
    name = db.Column(db.String(256), index=True)
    generation_id = db.Column(db.Integer, db.ForeignKey('generation.id'))
    modifications = db.relationship('Modifications', backref='series', lazy='dynamic')


    def __repr__(self):
        return '<Model {}>'.format(self.name)