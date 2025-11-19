<<<<<<< HEAD
from flask import Flask, request, jsonify, session
from flask_cors import CORS
from flask_session import Session
from bson import ObjectId
from pymongo import MongoClient
from config import Config
from database import (
    add_user,
    authenticate_user,
    add_task,
    get_tasks_by_user,
    update_task,
    delete_task,
)

app = Flask(__name__)
app.config.from_object(Config)

Session(app)
CORS(app, supports_credentials=True)

client = MongoClient(Config.MONGO_URI)
db = client[Config.DB_NAME]
users = db.users
tasks = db.tasks

@app.route("/api/register", methods=["POST"])
def register():
    data = request.get_json()
    email = data.get("email")
    password = data.get("password")

    if not email or not password:
        return jsonify({"error": "Campos obrigatórios"}), 400

    user_id = add_user(email, password)
    if not user_id:
        return jsonify({"error": "Usuário já existe"}), 400

    return jsonify({"message": "Usuário criado com sucesso"}), 201


@app.route("/api/login", methods=["POST"])
def login():
    data = request.get_json()
    email = data.get("email")
    password = data.get("password")

    user = authenticate_user(email, password)
    if not user:
        return jsonify({"error": "Credenciais inválidas"}), 401

    session["user"] = user
    return jsonify({"message": "Login bem-sucedido"}), 200


@app.route('/api/logout', methods=['POST'])
def logout():
    session.pop('user', None)
    return jsonify({"message": "Logout realizado"}), 200


@app.route("/api/session", methods=["GET"])
def check_session():
    if "user" in session:
        return jsonify({"logged_in": True, "user": session["user"]}), 200
    return jsonify({"logged_in": False}), 401

@app.route("/api/tasks", methods=["GET"])
def get_tasks():
    user = session.get("user")
    if not user:
        return jsonify({"error": "Usuário não autenticado"}), 401

    user_id = user["_id"]
    user_tasks = get_tasks_by_user(user_id)
    return jsonify(user_tasks)

@app.route("/api/tasks", methods=["POST"])
def create_task():
    user = session.get("user")
    if not user:
        return jsonify({"error": "Usuário não autenticado"}), 401

    data = request.get_json()
    title = data.get("title")
    if not title:
        return jsonify({"error": "Título obrigatório"}), 400

    task_id = add_task(title, user["_id"])
    return jsonify({"_id": task_id, "title": title, "done": False}), 201


@app.route("/api/tasks/<task_id>", methods=["PUT"])
def update_task_route(task_id):
    user = session.get("user")
    if not user:
        return jsonify({"error": "Usuário não autenticado"}), 401

    data = request.get_json()
    updates = {}
    if "done" in data:
        updates["done"] = data["done"]
    if "title" in data:
        updates["title"] = data["title"]

    update_task(task_id, updates, user["_id"])
    return jsonify({"message": "Tarefa atualizada com sucesso"}), 200


@app.route("/api/tasks/<task_id>", methods=["DELETE"])
def delete_task_route(task_id):
    user = session.get("user")
    if not user:
        return jsonify({"error": "Usuário não autenticado"}), 401

    delete_task(task_id, user["_id"])
    return jsonify({"message": "Tarefa deletada com sucesso"}), 200


if __name__ == "__main__":
=======
from flask import Flask, request, jsonify
from flask_cors import CORS
from bson import ObjectId
from database import tasks_collection

app = Flask(__name__)
CORS(app)

# Função auxiliar para converter ObjectId em string
def serialize_task(task):
    return {
        "_id": str(task["_id"]),
        "title": task["title"],
        "done": task["done"]
    }

# GET - listar todas as tarefas
@app.route('/api/tasks', methods=['GET'])
def get_tasks():
    tasks = list(tasks_collection.find())
    return jsonify([serialize_task(task) for task in tasks])

# POST - adicionar nova tarefa
@app.route('/api/tasks', methods=['POST'])
def add_task():
    data = request.get_json()
    new_task = {
        "title": data.get("title", ""),
        "done": False
    }
    result = tasks_collection.insert_one(new_task)
    new_task["_id"] = str(result.inserted_id)
    return jsonify(new_task), 201

# PUT - atualizar tarefa (done e/ou title)
@app.route('/api/tasks/<task_id>', methods=['PUT'])
def update_task(task_id):
    data = request.get_json()

    update_data = {}
    if "done" in data:
        update_data["done"] = data["done"]
    if "title" in data:
        update_data["title"] = data["title"]

    if not update_data:
        return jsonify({"error": "Nenhum campo para atualizar"}), 400

    updated = tasks_collection.find_one_and_update(
        {"_id": ObjectId(task_id)},
        {"$set": update_data},
        return_document=True
    )

    if updated:
        return jsonify(serialize_task(updated))
    return jsonify({"error": "Task not found"}), 404

# DELETE - remover tarefa
@app.route('/api/tasks/<task_id>', methods=['DELETE'])
def delete_task(task_id):
    result = tasks_collection.delete_one({"_id": ObjectId(task_id)})
    if result.deleted_count > 0:
        return jsonify({"message": "Deleted"}), 200
    return jsonify({"error": "Task not found"}), 404

if __name__ == '__main__':
>>>>>>> a1e7d05fc1e7bfbae028df6bdd30b747269d8873
    app.run(debug=True, port=5000)