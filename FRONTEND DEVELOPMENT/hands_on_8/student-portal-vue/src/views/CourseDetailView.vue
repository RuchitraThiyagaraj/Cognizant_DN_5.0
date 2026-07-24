<script setup>
import { useRoute, useRouter } from 'vue-router'

const route = useRoute()
const router = useRouter()

function enroll() {
  router.push('/profile')
}
</script>

<template>
  <h2>Course Detail</h2>

  <p>Course ID: {{ route.params.id }}</p>

  <button @click="enroll">
    Enroll
  </button>
</template>

<style scoped>
button {
  margin-top: 10px;
}
</style>