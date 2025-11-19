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
    app.run(debug=True, port=5000)