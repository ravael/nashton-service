import pymongo

connection_string = f"mongodb://balta:e296cd9f@localhost:27017/admin"

class MongoDBConnection:
    __instance = None

    def __new__(cls):
        if cls.__instance is None:
            cls.__instance = super().__new__(cls)
            cls.__instance.client = pymongo.MongoClient(connection_string)
        return cls.__instance

    def get_client(self):
        return self.client

    def close_connection(self):
        self.client.close()