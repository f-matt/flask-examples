from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from pathlib import Path
from dotenv import load_dotenv
import os

BASE_DIR = Path(__file__).resolve().parent.parent
load_dotenv(os.path.join(BASE_DIR, '.env'))

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = os.environ.get("DATABASE_URI")
app.config["SQLALCHEMY_BINDS"] = {
    "second": os.environ.get("SECOND_DATABASE_URI"),
}

db = SQLAlchemy(app)

import module_a.endpoints

@app.route("/")
def index():
    return "Status: online"
