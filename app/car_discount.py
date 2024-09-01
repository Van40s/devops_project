from pymongo import MongoClient
import os


def get_mongo_uri():
    mongo_uri = os.getenv("MONGODB_URI")
    if not mongo_uri:
        host = os.getenv("MONGODB_HOST")
        port = os.getenv("MONGODB_PORT")
        username = os.getenv("MONGODB_USERNAME")
        password = os.getenv("MONGODB_PASSWORD")
        if username:
            auth = username
            if password:
                auth = f"{username}:{password}"
            if not port or host.__contains__(":"):
                mongo_uri = f"mongodb://{auth}@{host}"
            else:
                mongo_uri = f"mongodb://{auth}@{host}:{port}"
        else:
            mongo_uri = f"mongodb://{host}:{port}"

    return mongo_uri


MONGO_URI = get_mongo_uri()

mongo_client = MongoClient(MONGO_URI)
db = mongo_client["dealership"]
collection = db["available_cars"]


def calculate_discount(discount):
    mongo_docs = collection.find({}, {"price": 1})
    updated_count = 0

    print("Testing branch rules and deployment. v3")

    for doc in mongo_docs:
        discounted_price = doc["price"] * (1 - discount / 100.0)

        result = collection.update_one(
            {"_id": doc["_id"]},
            {"$set": {"price": int(discounted_price)}},  # testing pre-commit to fail
        )  # testing branch rules v2 #testing branch rules v3
        if result.modified_count > 0:
            updated_count += 1  # Increment the count for each updated document
            # forgot to add secrets. Testing build and push again.

    return updated_count


def get_available_cars():
    mongo_docs = collection.find({}, {"_id": 0})

    in_db = []

    for doc in mongo_docs:
        in_db.append(doc)

    return in_db
