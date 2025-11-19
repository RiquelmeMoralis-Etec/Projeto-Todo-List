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
      const userId = localStorage.getItem("user_id");

      if (this.isEditing) {
        await api.put(`/tasks/${this.editTask._id}`, { title: this.taskTitle });
        this.$emit("task-updated");
        this.$emit("notify", "Tarefa atualizada com sucesso", "success");
      } else {
        await api.post("/tasks", { title: this.taskTitle, user_id: userId });
        this.$emit("task-added");
        this.$emit("notify", "Tarefa adicionada com sucesso", "success");
      }

      this.taskTitle = "";
      this.isEditing = false;
    },
    cancelEdit() {
      this.$emit('cancel-edit')
      this.taskTitle = ''
      this.isEditing = false
    }
  }
}
</script>