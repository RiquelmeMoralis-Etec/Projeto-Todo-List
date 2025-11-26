<template>
  <div v-if="visible" :class="['Notification', type]">
    {{ message }}
  </div>
</template>

<script>
export default {
  props: {
    message: {
      type: String,
      required: true
    },
    type: {
      type: String,
      default: 'success'
    }
  },
  data() {
    return {
      visible: true
    }
  },
  mounted() {
    setTimeout(() => {
      this.visible = false
    }, 3000)
  }
}
</script>

<style scoped>
.notification {
  padding: 12px;
  margin: 10px auto;
  max-width: 600px;
  width: 100%;
  border-radius: 5px;
  text-align: center;
  font-weight: bold;
  font-size: 16px;
  box-shadow: 0 2px 8px rgba(0, 0, 0, 0.1);
  transition: opacity 0.3s ease;
}

.success {
  background-color: #d4edda;
  color: #155724;
  border: 1px solid #c3e6cb;
}

.error {
  background-color: #f8d7da;
  color: #721c24;
  border: 1px solid #f5c6cb;
}
</style>