import json
import uuid

class Answer:
    def __init__(self, id, resposta):
        self.id = id
        self.resposta = resposta

    def toJson(self):
        return json.dumps(self, default=lambda o: o.__dict__)
