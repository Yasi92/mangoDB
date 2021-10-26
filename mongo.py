import os
import pymongo

if os.path.exists("env.py"):
    import env

MONGO_URL = os.environ.get("MONGO_URL")
DATABASE = "myFirstDB"
COLLECTION = "celebrities"

def mongo_connect(url):
    try:
        conn = pymongo.MongoClient(url)
        print("Mongo is connected")
        return conn

    except pymongo.errors.ConnectionFailure as e:
        print("Could not connect to MongoDB: %S") % e


conn = mongo_connect(MONGO_URL)

coll = conn[DATABASE][COLLECTION]

new_doc ={"first" : "douglas", "last" : "adams", "dob" : "11/03/1952", "hair_color" : "grey", "occupation" : "writer", "nationality" : "british"}
coll.insert_one(new_doc)


coll.update_many({"nationality" : "american"}, {"$set": {"hair_color" : "maroon"}})
documents = coll.find({"nationality" : "american"})
for doc in documents:
    print(doc)