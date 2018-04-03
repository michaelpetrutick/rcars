from flask import Flask
from config import DevelopmentConfig
from models import db
from flask_migrate import Migrate

from models.Brand import Brand

app = Flask(__name__)

from app import routes
app.config.from_object(DevelopmentConfig)

# Initialize database
db.init_app(app)

migrate = Migrate(app, db)

from app import routes