from src.config.database import MongoDBConnection

class RiddleService:
    
    def get_riddle(self, _id):
        client = MongoDBConnection().get_client()
        db = client.admin
        riddle = db.riddle
        return riddle.find_one({"_id" : _id})