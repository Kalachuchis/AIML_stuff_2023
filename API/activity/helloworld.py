from flask import Flask
from flask_restx import Resource, Api, reqparse

app = Flask(__name__)
api = Api(app, title="Sample API", description="My first API")

parser = reqparse.RequestParser()
parser.add_argument('var1', type=int, help='Helpful Description')
parser.add_argument('var2', type=int, help='Description')


@api.route('/hello')
class HelloWorld(Resource):
    def get(self):
        return {'hello': 'world'}, 200


@api.route('/parser')
class HelloWorld(Resource):

    def post(self):
        print(api.payload)


if __name__ == '__main__':
    app.run(debug=True)
