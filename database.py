from pymongo import MongoClient
import os
from dotenv import load_dotenv

load_dotenv()

MONGO_URL = os.getenv("MONGO_URL", "mongodb+srv://a9666653_db_user:fzE3luXxNHFmgDth@cluster0.tumvab5.mongodb.net/")

client = MongoClient(MONGO_URL)
db = client["taskflow"]
users_collection = db["users"]
products_collection = db["products"]