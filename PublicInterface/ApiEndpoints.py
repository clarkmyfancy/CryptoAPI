
from flask import Flask
from flask_restful import Resource, Api, reqparse
import pandas as pd
import ast
import json

from .Cryptos import Cryptos

class ApiEndpoints:

    def __init__(self):
        self.app = Flask(__name__)
        self.api = Api(self.app)

        self.api.add_resource(Cryptos, '/cryptos')

        self.app.run()
