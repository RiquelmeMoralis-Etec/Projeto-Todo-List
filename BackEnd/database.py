<<<<<<< HEAD
from pymongo import MongoClient
from werkzeug.security import generate_password_hash, check_password_hash
from bson import ObjectId

client = MongoClient("mongodb://localhost:27017/")
db = client.todo_db

users_collection = db.users
tasks_collection = db.tasks

def add_user(email, password):
    if users_collection.find_one({"email": email}):
        return None
    hashed = generate_password_hash(password)
    user = {"email": email, "password": hashed}
    result = users_collection.insert_one(user)
    return str(result.inserted_id)

def authenticate_user(email, password):
    user = users_collection.find_one({"email": email})
    if user and check_password_hash(user["password"], password):
        return {"_id": str(user["_id"]), "email": user["email"]}
    return None

def add_task(title, user_id):
    task = {"title": title, "done": False, "user_id": user_id}
    result = tasks_collection.insert_one(task)
    return str(result.inserted_id)

def get_tasks_by_user(user_id):
    tasks = list(tasks_collection.find({"user_id": user_id}))
    for t in tasks:
        t["_id"] = str(t["_id"])
    return tasks

def update_task(task_id, updates, user_id):
    tasks_collection.update_one(
        {"_id": ObjectId(task_id), "user_id": user_id},
        {"$set": updates}
    )

def delete_task(task_id, user_id):
    tasks_collection.delete_one({"_id": ObjectId(task_id), "user_id": user_id})
=======
# database.py
from pymongo import MongoClient

# conexão com MongoDB local (Compass)
client = MongoClient("mongodb://localhost:27017/")

# banco de dados "todo_db"
db = client["todo_db"]

# coleção "tasks"
tasks_collection = db["tasks"]
>>>>>>> a1e7d05fc1e7bfbae028df6bdd30b747269d8873
