# database.py
from pymongo import MongoClient

# conexão com MongoDB local (Compass)
client = MongoClient("mongodb://localhost:27017/")

# banco de dados "todo_db"
db = client["todo_db"]

# coleção "tasks"
tasks_collection = db["tasks"]