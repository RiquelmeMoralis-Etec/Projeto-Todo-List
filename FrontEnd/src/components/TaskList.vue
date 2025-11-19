<template>
  <ul>
      <TaskItem
        v-for="task in tasks"
        :key="task._id"
        :task="task"
        @task-updated="$emit('task-updated')"
        @task-deleted="$emit('task-deleted')"
        @edit-task="$emit('edit-task', $event)"
        @notify="$emit('notify', $event, $event2)"
      />
  </ul>
</template>

<script>
import TaskItem from './TaskItem.vue'

export default {
  props: ['tasks'],
  components: { TaskItem }
}
</script>