from flask_restful import Resource, reqparse

from DataBridge.DataBridge import getCryptosOfInterest, addToCryptosOfInterest

class Cryptos(Resource):

    def get(self):
        contents = getCryptosOfInterest()
        return { "data": contents }, 200

    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument('new-token', required=True)

        args = parser.parse_args()
        addToCryptosOfInterest(args['new-token'])
        return None, 200
# # return {'data': data}, 200  #