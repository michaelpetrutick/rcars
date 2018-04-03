from models import db


class Brand(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(256), index=True, unique=True)

    def __repr__(self):
        return '<Brand {}>'.format(self.name)
