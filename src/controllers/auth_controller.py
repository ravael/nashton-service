from flask import request, Response, json, Blueprint

users = Blueprint("users", __name__)


f = open('src/controllers/data.json')
data = json.load(f)

@users.route('/signin', methods = ["GET", "POST"])
def handle_login():
    return Response(
            response=json.dumps(data),
            status=200,
            mimetype='application/json'
            )
