<template>
<<<<<<< HEAD
  <main>
    <router-view />
  </main>
</template>

<script setup>
</script>

<style>
main {
  max-width: 800px;
  margin: 0 auto;
  padding: 20px;
  background-color: #fff;
  border-radius: 10px;
  box-shadow: 0 5px 15px rgba(0, 0, 0, 0.1);
  font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
}
=======
  <div class="container">
    <h1>To-Do List</h1>

    <Notification 
      v-if="notification.message" 
      :message="notification.message" 
      :type="notification.type" 
    />

    <!-- Formulário de adicionar/editar -->
    <TaskForm 
      :editTask="taskBeingEdited"
      @task-added="fetchTasks"
      @task-updated="finishEdit"
      @cancel-edit="finishEdit"
      @notify="showNotification"
    />

    <!-- Filtros -->
    <div class="filters">
      <button :class="{ active: filter === 'all' }" @click="filter = 'all'">Todas</button>
      <button :class="{ active: filter === 'done' }" @click="filter = 'done'">Concluídas</button>
      <button :class="{ active: filter === 'pending' }" @click="filter = 'pending'">Pendentes</button>
    </div>

    <!-- Lista de tarefas -->
    <TaskList 
      :tasks="filteredTasks" 
      @task-updated="fetchTasks" 
      @task-deleted="fetchTasks"
      @edit-task="startEdit"
      @notify="showNotification"
    />

    <!-- Contadores -->
    <p class="counters">
      Total: {{ tasks.length }} |
      Concluídas: {{ doneCount }} |
      Pendentes: {{ pendingCount }}
    </p>
  </div>
</template>

<script>
import TaskForm from './components/TaskForm.vue'
import TaskList from './components/TaskList.vue'
import api from './services/api'
import Notification from './components/Notification.vue'

export default {
  components: { TaskForm, TaskList, Notification },
  data() {
    return {
      tasks: [],
      taskBeingEdited: null,
      filter: 'all',
      notification: {
        message: '',
        type: 'success'
      }
    }
  },
  computed: {
    filteredTasks() {
      if (this.filter === 'done') return this.tasks.filter(t => t.done)
      if (this.filter === 'pending') return this.tasks.filter(t => !t.done)
      return this.tasks
    },
    doneCount() {
      return this.tasks.filter(t => t.done).length
    },
    pendingCount() {
      return this.tasks.filter(t => !t.done).length
    }
  },
  methods: {
    async fetchTasks() {
      try {
        const response = await api.get('/tasks')
        this.tasks = response.data
      } catch (err) {
        this.showNotification('Erro ao buscar tarefas', 'error')
        console.error(err)
      }
    },
    startEdit(task) {
      this.taskBeingEdited = task
    },
    finishEdit() {
      this.taskBeingEdited = null
      this.fetchTasks()
    },
    showNotification(message, type = 'success') {
      this.notification = { message, type }
      setTimeout(() => {
        this.notification.message = ''
      }, 3000)
    }
  },
  mounted() {
    this.fetchTasks()
  }
}
</script>

<style>
.container {
  max-width: 600px;
  margin: 40px auto;
  font-family: Arial, sans-serif;
}

.filters {
  margin: 15px 0;
}

.filters button {
  margin-right: 10px;
  padding: 5px 10px;
}

.filters .active {
  background-color: #333;
  color: #fff;
}

.counters {
  margin-top: 15px;
  font-weight: bold;
}
/* Responsividade */
  @media (max-width: 600px) {
    .container {
      margin: 20px auto;
      padding: 10px;
    }

    input[type="text"],
    button {
      width: 100%;
      margin-bottom: 10px;
    }

    .filters {
      flex-direction: column;
    }

    .filters button {
      width: 100%;
    }
  }
>>>>>>> a1e7d05fc1e7bfbae028df6bdd30b747269d8873
</style>