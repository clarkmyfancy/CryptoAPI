from flask_restful import Resource, Api, reqparse

class Users(Resource):

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