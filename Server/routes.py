from flask.views import MethodView
from flask import request, make_response, jsonify

class Home(MethodView):
    def get(self):
        return 'Hello World!'
    def post(self):
        data = request.get_json()
        if data["msg"]:
            return data["msg"]
        else:
            return None