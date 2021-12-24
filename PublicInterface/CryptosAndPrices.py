from flask_restful import Resource, reqparse

from DataBridge.DataBridge import getCryptosOfInterest
from CoinMarketCapApi.Api import Api



class CryptosAndPrices(Resource):

    def get(self):
        api = Api()
        cryptos = getCryptosOfInterest()
        return { 'data': list(api.getQuotes(cryptos))}, 200