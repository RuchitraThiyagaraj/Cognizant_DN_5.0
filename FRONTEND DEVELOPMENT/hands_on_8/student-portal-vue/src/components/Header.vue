<template>
  <header>
    <h2>Student Portal</h2>

    <p>
      Enrolled: {{ store.enrolledCourses.length }}
    </p>
  </header>
</template>

<script setup>
import { useEnrollmentStore } from '../stores/enrollment'

const store = useEnrollmentStore()
</script>

<style scoped>
header {
  background: #42b883;
  color: white;
  padding: 15px;
}
</style>