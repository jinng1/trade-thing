from pymongo import MongoClient

class MongoDBManager:
    def __init__(self, config):
        self.client = MongoClient(config['MONGO_URI'])
        self.db = self.client.tradething
    
    def add_to_collection(self, collection_name, data):
        collection = self.get_collection(collection_name)
        collection.insert_one(data)
    
    def ping(self):
        return self.db.command('ping')