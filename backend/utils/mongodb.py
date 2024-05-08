from pymongo import MongoClient

class MongoDBManager:
    def __init__(self, config):
        self.client = MongoClient(config['MONGO_URI'])
        self.db = self.client.tradething
    
    def get_collection(self, collection_name):
        return self.db[collection_name]
    
    def ping(self):
        return self.db.command('ping')