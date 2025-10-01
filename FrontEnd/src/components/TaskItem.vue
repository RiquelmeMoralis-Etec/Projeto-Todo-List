<template>
  <li>
    <input type="checkbox" :checked="task.done" @change="toggleDone" />

    <span class="task-title"
        :class="{ done: task.done }"
        :title="task.title">
      {{ task.title }}
    </span>

    <div class="actions">
      <button @click="$emit('edit-task', task)">✏️</button>
      <button @click="deleteTask">🗑</button>
    </div>
  </li>
</template>


<script>
import api from '../services/api'

export default {
  props: ['task'],
  data() {
    return {
      editing: false,
      editedTitle: this.task.title
    }
  },
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