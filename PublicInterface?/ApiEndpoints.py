from flask import Flask
from flask_restful import Resource, Api, reqparse
import pandas as pd
import ast
import json

from DataBridge.DataBridge import getCryptosOfInterest, getUsers


app = Flask(__name__)
api = Api(app)

class Cryptos(Resource):

    def get(self):
        contents = getCryptosOfInterest()
        return { "data": contents }, 200

class Users(Resource):
    
    def get(self):
        contents = getUsers()
        return contents, 200

    def post(self):
        parser = reqparse.RequestParser()

        parser.add_argument('userId', required=True)
        parser.add_argument('name', required=False)

        args = parser.parse_args()

        file = open("Database/Users.txt", "a")
        file.write(args['userId'])
        file.write("\n")
        file.close()
        return None, 200
# return {'data': data}, 200  #



api.add_resource(Users, '/users')
api.add_resource(Cryptos, '/cryptos')


if __name__ == '__main__':
    app.run()  # run our Flask app