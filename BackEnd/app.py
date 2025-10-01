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
    app.run(debug=True, port=5000)