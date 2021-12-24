
from flask import Flask
from flask_restful import Api

from .Cryptos import Cryptos

class ApiEndpoints:

    def __init__(self):
        self.app = Flask(__name__)
        self.api = Api(self.app)

        self.api.add_resource(Cryptos, '/api/cryptos')

        self.app.run()
