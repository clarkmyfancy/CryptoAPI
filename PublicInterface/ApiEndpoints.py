
from flask import Flask
from flask_restful import Api

from .Cryptos import Cryptos
from PublicInterface.CryptosAndPrices import CryptosAndPrices

class ApiEndpoints:

    def __init__(self):
        self.app = Flask(__name__)
        self.api = Api(self.app)

        self.api.add_resource(Cryptos, '/api/cryptos')
        self.api.add_resource(CryptosAndPrices, '/api/get-prices')

        self.app.run(debug=True)
