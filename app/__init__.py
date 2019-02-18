from flask_cors import CORS
from flask import Flask

app = Flask(__name__)

CORS(app)

# we'll add config later
# app.config.from_object('config')

# putting the import here avoids a circular reference
from app import views
