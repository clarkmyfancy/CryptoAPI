from flask import Flask
from flask_restful import Resource, Api, reqparse
import pandas as pd
import ast


app = Flask(__name__)
api = Api(app)

class Users(Resource):
    
    def get(self):
        return 12

api.add_resource(Users, '/users')


if __name__ == '__main__':
    app.run()  # run our Flask app