
from pymongo import MongoClient
from config_loader import load_config

def save_to_mongodb(data, mongo_uri, db_name, collection_name="trends"):
    # Connect to MongoDB
    client = MongoClient(mongo_uri)
    db = client[db_name]
    collection = db[collection_name]
    
    # Insert data into the collection
    collection.insert_one(data)
    client.close()

def fetch_from_mongodb(mongo_uri, db_name, collection_name="trends"):

    # Connect to MongoDB and fetch data
    client = MongoClient(mongo_uri)
    db = client[db_name]
    collection = db[collection_name]
    
    # Fetch the latest document, sorted by the _id field (descending order)
    latest_document = collection.find_one({}, sort=[('_id', -1)])  # Sort by _id to get the latest inserted document

    # Convert ObjectId to string before returning the data
    if latest_document:
        latest_document["_id"] = str(latest_document["_id"])  # Convert ObjectId to string
    else:
        latest_document = None

    client.close()
    return latest_document
