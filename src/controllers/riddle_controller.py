from flask import request, Response, json, Blueprint
from src.models.answer import Answer
from src.services.riddle_service import RiddleService

riddle = Blueprint("riddle", __name__)

class RiddleController:

    @riddle.route('/<int:_id>', methods = ["GET"])
    def get_riddle(_id):

        service = RiddleService()
        
        return Response(
            response=json.dumps(service.get_riddle(_id)),
            status=200,
            mimetype='application/json')
 
