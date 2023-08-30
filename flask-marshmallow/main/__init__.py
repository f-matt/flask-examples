from flask import Flask
from flask_restful import Api
from pathlib import Path
import configparser

BASE_DIR = Path(__file__).resolve().parent.parent

config = configparser.ConfigParser()
config.read(f'{BASE_DIR}/.env')

app = Flask(__name__)
api = Api(app)

from main.services import IndexEndpoint, ItemsService

api.add_resource(IndexEndpoint, '/')
api.add_resource(ItemsService, '/items')
