from pymongo import MongoClient
import os

MONGO_URI = os.getenv("MONGO_URI")

mongo_client = MongoClient(MONGO_URI)
db = mongo_client["dealership"]
collection = db["available_cars"]


def calculate_discount(discount):
    mongo_docs = collection.find({}, {"price": 1})
    updated_count = 0

    for doc in mongo_docs:
        discounted_price = doc["price"] * (1 - discount / 100.0)

        result = collection.update_one(
            {"_id": doc["_id"]},
            {
                "$set": {"price": int(discounted_price)}}, # testing pre-commit to fail
        )
        if result.modified_count > 0:
            updated_count += 1  # Increment the count for each updated document

    return updated_count
