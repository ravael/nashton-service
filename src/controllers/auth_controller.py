from flask import request, Response, json, Blueprint
from src.models.answer import Answer

users = Blueprint("users", __name__)


f = open('src/controllers/data.json')
data = json.load(f)

@users.route('/signin', methods = ["GET", "POST"])
def handle_login():
    return Response(
            response=json.dumps(create_answer().toJson(), indent=4),
            status=200,
            mimetype='application/json'
            )

def create_answer():
    answer = Answer(1,"Resposta")
    return answer
