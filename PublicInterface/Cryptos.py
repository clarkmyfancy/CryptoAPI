from flask_restful import Resource

from DataBridge.DataBridge import getCryptosOfInterest

class Cryptos(Resource):

    def get(self):
        contents = getCryptosOfInterest()
        return { "data": contents }, 200