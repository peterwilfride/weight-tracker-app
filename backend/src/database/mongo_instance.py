import os
import dotenv
from pymongo import MongoClient

dotenv_file = dotenv.find_dotenv()
dotenv.load_dotenv(dotenv_file)

CONNECTION_STRING = os.environ.get("MONGODB_STRING_CONNECTION")

connection = MongoClient(CONNECTION_STRING)

if __name__ == '__main__':
    try:
        client = connect
        db = client.test
        db.command("serverStatus")
    except Exception as e:
        print(e)
    else:
        print("You are connected!")