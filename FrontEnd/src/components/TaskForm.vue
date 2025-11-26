<template>
  <form @submit.prevent="handleSubmit">
    <input 
      v-model="taskTitle" 
      placeholder="Digite uma tarefa..." 
      required 
    />
    <button type="submit">
      {{ isEditing ? "Salvar Alterações" : "Adicionar" }}
    </button>
    <button v-if="isEditing" type="button" @click="cancelEdit">
      Cancelar
    </button>
  </form>
</template>

<script>
import api from '../services/api'

export default {
  props: {
    editTask: {
      type: Object,
      default: null
    }
  },
  data() {
    return {
      taskTitle: '',
      isEditing: false
    }
  },
  watch: {
    editTask: {
      immediate: true,
      handler(newTask) {
        if (newTask) {
          this.taskTitle = newTask.title
          this.isEditing = true
        } else {
          this.taskTitle = ''
          this.isEditing = false
        }
      }
    }
  },
  methods: {
    async handleSubmit() {
      try {
        if (!this.taskTitle.trim()) {
          this.$emit("notify", "O título não pode estar vazio", "error")
          return
        }

        if (this.isEditing) {
          // UPDATE TASK
          await api.put(`/tasks/${this.editTask._id}`, {
            title: this.taskTitle
          })

          this.$emit("task-updated")
          this.$emit("notify", "Tarefa atualizada com sucesso", "success")

        } else {
          // CREATE TASK (sem user_id!)
          await api.post("/tasks", {
            title: this.taskTitle
          })

          this.$emit("task-added")
          this.$emit("notify", "Tarefa adicionada com sucesso", "success")
        }

        this.taskTitle = ""
        this.isEditing = false

      } catch (e) {
        if (!e.response) {
          this.$emit("notify", "Erro de conexão com servidor", "error")
          return
        }

        const status = e.response.status

        if (status === 400) {
          this.$emit("notify", "Título da tarefa inválido", "error")
        }
        else if (status === 401) {
          this.$emit("notify", "Sessão expirada, faça login novamente", "error")
          this.$router.push("/login")
        }
        else if (status === 404) {
          this.$emit("notify", "Tarefa não encontrada", "error")
        }
        else {
          this.$emit("notify", "Erro inesperado ao salvar tarefa", "error")
        }
      }
    },

    cancelEdit() {
      this.$emit('cancel-edit')
      this.taskTitle = ''
      this.isEditing = false
    }
  }
}
</script>