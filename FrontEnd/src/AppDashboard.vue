<template>
  <div class="container">

    <div class="top-bar">
      <h2>To-Do List</h2>
      <button @click="logout">Sair</button>
    </div>

    <h1>To-Do List</h1>

    <Notification 
      v-if="notification.message" 
      :message="notification.message" 
      :type="notification.type" 
    />

    <TaskForm 
      :editTask="taskBeingEdited"
      @task-added="fetchTasks"
      @task-updated="finishEdit"
      @cancel-edit="finishEdit"
      @notify="showNotification"
    />

    <div class="filters">
      <button :class="{ active: filter === 'all' }" @click="filter = 'all'">Todas</button>
      <button :class="{ active: filter === 'done' }" @click="filter = 'done'">Concluídas</button>
      <button :class="{ active: filter === 'pending' }" @click="filter = 'pending'">Pendentes</button>
    </div>

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
        const response = await api.get("/tasks");
        this.tasks = response.data;
      } catch (err) {
        this.showNotification("Erro ao buscar tarefas", "error");
        console.error(err);
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
    },
    async logout() {
      try {
        await api.post("/logout", {}, { withCredentials: true });
        this.$router.push("/login");
      } catch (err) {
        console.error("Erro ao fazer logout:", err);
      }
    },
  },
  mounted() {
    this.fetchTasks()
  }
}
</script>

<style>
.top-bar {
  display: flex;
  justify-content: space-between;
  align-items: center;
  margin-bottom: 20px;
}

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
</style>