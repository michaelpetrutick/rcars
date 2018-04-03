from models import db

# "modification_id","series_id","model_id","modification_name","start_production_year","end_production_year"
class Modifications(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    series_id = db.Column(db.Integer, db.ForeignKey('series.id'))
    model_id = db.Column(db.Integer, db.ForeignKey('model.id'))
    name = db.Column(db.String(256), index=True)




    year_begin = db.Column(db.String(128), index=True)
    year_end = db.Column(db.String(128), index=True)

