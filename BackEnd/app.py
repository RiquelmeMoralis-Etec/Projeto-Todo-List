from flask import Flask, request, jsonify, session
from flask_cors import CORS
from flask_session import Session
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

@app.route("/api/register", methods=["POST"])
def register():
    data = request.get_json()
    email = data.get("email")
    password = data.get("password")

    if not email or not password:
        return jsonify({"message": "Email e senha são obrigatórios"}), 400

    user_id = add_user(email, password)
    if not user_id:
        return jsonify({"message": "Usuário já existe"}), 409

    return jsonify({"message": "Usuário criado"}), 201


@app.route("/api/login", methods=["POST"])
def login():
    data = request.get_json()
    email = data.get("email")
    password = data.get("password")

    user = authenticate_user(email, password)
    if not user:
        return jsonify({"message": "Credenciais inválidas"}), 401

    session["user"] = user
    return jsonify({"message": "Login realizado"}), 200


@app.route("/api/logout", methods=["POST"])
def logout():
    session.pop("user", None)
    return jsonify({"message": "Logout OK"}), 200


@app.route("/api/session", methods=["GET"])
def check_session():
    if "user" in session:
        return jsonify({"user": session["user"]}), 200
    return jsonify({"message": "Não autenticado"}), 401

@app.route("/api/tasks", methods=["GET"])
def get_tasks():
    user = session.get("user")
    if not user:
        return jsonify({"message": "Não autenticado"}), 401

    user_tasks = get_tasks_by_user(user["_id"])
    return jsonify(user_tasks), 200


@app.route("/api/tasks", methods=["POST"])
def create_task():
    user = session.get("user")
    if not user:
        return jsonify({"message": "Não autenticado"}), 401

    data = request.get_json()
    title = data.get("title")

    if not title:
        return jsonify({"message": "Título obrigatório"}), 400

    task_id = add_task(title, user["_id"])
    return jsonify({"_id": task_id, "title": title, "done": False}), 201


@app.route("/api/tasks/<task_id>", methods=["PUT"])
def update_task_route(task_id):
    user = session.get("user")
    if not user:
        return jsonify({"message": "Não autenticado"}), 401

    data = request.get_json()
    update_task(task_id, data, user["_id"])

    return jsonify({"message": "Atualizado"}), 200


@app.route("/api/tasks/<task_id>", methods=["DELETE"])
def delete_task_route(task_id):
    user = session.get("user")
    if not user:
        return jsonify({"message": "Não autenticado"}), 401

    delete_task(task_id, user["_id"])
    return jsonify({"message": "Removido"}), 200


if __name__ == "__main__":
    app.run(debug=True, port=5000)