from flask import Flask, request
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)


class HelloWorld(Resource):
    def get(self):
        return {'about': 'Hello World!'}

    def post(self):
        message = request.get_json()
        return {'users data': message}, 201


class Add(Resource):
    def get(self, num1, num2):
        return {'result': num1 + num2}


class Sub(Resource):
    def get(self, num1, num2):
        return {'result': num1 - num2}


class Multi(Resource):
    def get(self, num1, num2):
        return {'result': num1 * num2}


class Div(Resource):
    def get(self, num1, num2):
        return {'result': num1 / num2}


api.add_resource(HelloWorld, '/')
api.add_resource(Add, '/add/<int:num1>/<int:num2>')
api.add_resource(Sub, '/sub/<int:num1>/<int:num2>')
api.add_resource(Multi, '/multi/<int:num1>/<int:num2>')
api.add_resource(Div, '/div/<int:num1>/<int:num2>')

if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0", port=8000)