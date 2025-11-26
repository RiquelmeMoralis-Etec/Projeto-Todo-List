<template>
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
      {{ task.title }}
    </span>

    <div class="actions">
      <button @click="$emit('edit-task', task)">✏️</button>
      <button @click="deleteTask">🗑️</button>
    </div>
  </li>
</template>

<script>
import api from "../services/api"

export default {
  props: ["task"],
  methods: {
    async toggleDone() {
      try {
        await api.put(`/tasks/${this.task._id}`, { done: !this.task.done })
        this.$emit("task-updated")
        this.$emit("notify", "Tarefa atualizada", "success")

      } catch (e) {
        if (!e.response) {
          this.$emit("notify", "Erro de conexão com servidor", "error")
          return
        }

        const status = e.response.status

        if (status === 401) {
          this.$emit("notify", "Sessão expirada, faça login novamente", "error")
          this.$router.push("/login")
        }
        else if (status === 404) {
          this.$emit("notify", "Tarefa não encontrada", "error")
        }
        else {
          this.$emit("notify", "Erro ao atualizar tarefa", "error")
        }
      }
    },

    async deleteTask() {
      try {
        await api.delete(`/tasks/${this.task._id}`)
        this.$emit("task-deleted")
        this.$emit("notify", "Tarefa deletada com sucesso", "success")

      } catch (e) {
        if (!e.response) {
          this.$emit("notify", "Erro de conexão com servidor", "error")
          return
        }

        const status = e.response.status

        if (status === 401) {
          this.$emit("notify", "Sessão expirada, faça login novamente", "error")
          this.$router.push("/login")
        }
        else if (status === 404) {
          this.$emit("notify", "Tarefa já deletada ou não encontrada", "error")
        }
        else {
          this.$emit("notify", "Erro ao deletar tarefa", "error")
        }
      }
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