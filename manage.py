from app import app
from app import db
from models.Brand import Brand

@app.shell_context_processor
def make_shell_context():
    return {'db': db, 'Brand': Brand}
