from app import app
from app import db
from models.Brand import Brand
from models.Generation import Generation
from models.Model import Model
from models.Series import Series
from models.Modifications import Modifications

@app.shell_context_processor
def make_shell_context():
    return {'db': db, 'Brand': Brand, 'Generation':Generation, 'Model':Model, 'Series':Series, 'Modifications':Modifications}
