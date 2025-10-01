# init_db.py
from database import tasks_collection

# tarefas de exemplo
sample_tasks = [
    {"title": "Estudar Vue.js", "done": False},
    {"title": "Configurar MongoDB Compass", "done": True},
    {"title": "Finalizar projeto ToDoList", "done": False}
]

def init_db():
    if tasks_collection.count_documents({}) == 0:  # só popula se estiver vazio
        tasks_collection.insert_many(sample_tasks)
        print("Banco inicializado com tarefas de exemplo!")
    else:
        print("Banco já contém tarefas, nada a fazer.")

if __name__ == "__main__":
    init_db()