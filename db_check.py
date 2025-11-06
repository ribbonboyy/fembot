from pymongo import MongoClient
import os
from dotenv import load_dotenv

load_dotenv()

def test_mongo_connection():
    uri = os.getenv("MONGO_URI")
    if not uri:
        return "not found in enviroment"

    try:
        client = MongoClient(uri, serverSelectionTimeoutMS=3000)
        client.admin.command("ping")
        return "Mongodb connected yes idk"
    except Exception as e:
        return f"failed to connected: {e}"

if __name__ == "__main__":
    print(test_mongo_connection())
