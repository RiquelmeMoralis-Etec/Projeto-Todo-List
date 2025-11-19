<template>
<<<<<<< HEAD
  <li class="task-item">
    <input 
      type="checkbox" 
      :checked="task.done" 
      @change="toggleDone"
      class="checkbox"
    />

    <span 
      class="task-title"
      :class="{ done: task.done }"
      :title="task.title"
    >
=======
  <li>
    <input type="checkbox" :checked="task.done" @change="toggleDone" />

    <span class="task-title"
        :class="{ done: task.done }"
        :title="task.title">
>>>>>>> a1e7d05fc1e7bfbae028df6bdd30b747269d8873
      {{ task.title }}
    </span>

    <div class="actions">
      <button @click="$emit('edit-task', task)">✏️</button>
<<<<<<< HEAD
      <button @click="deleteTask">🗑️</button>
=======
      <button @click="deleteTask">🗑</button>
>>>>>>> a1e7d05fc1e7bfbae028df6bdd30b747269d8873
    </div>
  </li>
</template>

<<<<<<< HEAD
=======

>>>>>>> a1e7d05fc1e7bfbae028df6bdd30b747269d8873
<script>
import api from '../services/api'

export default {
  props: ['task'],
<<<<<<< HEAD
=======
  data() {
    return {
      editing: false,
      editedTitle: this.task.title
    }
  },
>>>>>>> a1e7d05fc1e7bfbae028df6bdd30b747269d8873
  methods: {
    async toggleDone() {
      await api.put(`/tasks/${this.task._id}`, { done: !this.task.done })
      this.$emit('task-updated')
    },
    async deleteTask() {
      try {
        await api.delete(`/tasks/${this.task._id}`)
        this.$emit('task-deleted')
        this.$emit('notify', 'Tarefa deletada com sucesso', 'success')
      } catch (error) {
        this.$emit('notify', 'Erro ao deletar tarefa', 'error')
      }
<<<<<<< HEAD
    }
  }
}
</script>

<style scoped>
.task-item {
  display: grid;
  grid-template-columns: auto 1fr auto;
  align-items: flex-start;
  background: #f9f9f9;
  border-radius: 6px;
  margin-bottom: 10px;
  padding: 10px 12px;
  transition: box-shadow 0.2s;
  gap: 10px;
}

.task-item:hover {
  box-shadow: 0 4px 10px rgba(0,0,0,0.08);
}

.checkbox {
  margin-top: 4px;
  flex-shrink: 0;
}

.task-title {
  font-size: 16px;
  color: #333;
  white-space: normal;
  overflow-wrap: break-word;
  word-break: normal;
  max-width: 40ch;
  line-height: 1.4;
}

.task-title.done {
  text-decoration: line-through;
  color: #888;
}

.actions {
  display: flex;
  gap: 6px;
  flex-shrink: 0;
}

button {
  border: none;
  background: #2c7a7b;
  color: white;
  padding: 6px 10px;
  border-radius: 5px;
  cursor: pointer;
  font-size: 14px;
}

button:hover {
  background: #285e61;
}
</style>
=======
    },
    startEdit() {
      this.editing = true
      this.editedTitle = this.task.title
    },
    async saveEdit() {
      if (!this.editedTitle.trim()) return
      await api.put(`/tasks/${this.task._id}`, { title: this.editedTitle })
      this.editing = false
      this.$emit('task-updated')
    }
  }
}
</script>
>>>>>>> a1e7d05fc1e7bfbae028df6bdd30b747269d8873
