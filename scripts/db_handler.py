
from pymongo import MongoClient

def save_to_mongodb(data, mongo_uri="mongodb://localhost:27017", db_name="twitter_trends", collection_name="trends"):
    client = MongoClient(mongo_uri)
    db = client[db_name]
    collection = db[collection_name]
    collection.insert_one(data)
    client.close()
