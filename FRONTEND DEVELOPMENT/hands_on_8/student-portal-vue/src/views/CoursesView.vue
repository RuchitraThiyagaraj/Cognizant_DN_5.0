<script setup>
import CourseCard from '../components/CourseCard.vue'
import { ref, onMounted, computed } from 'vue'
import { useEnrollmentStore } from '../stores/enrollment'

const store = useEnrollmentStore()

const searchTerm = ref("")
const courses = ref([])

onMounted(() => {
  courses.value = [
    { id: 1, name: "Python", code: "CS101", credits: 4, grade: "A" },
    { id: 2, name: "Java", code: "CS102", credits: 3, grade: "A+" },
    { id: 3, name: "DBMS", code: "CS103", credits: 4, grade: "B+" },
    { id: 4, name: "Vue", code: "CS104", credits: 2, grade: "A" },
    { id: 5, name: "AI", code: "CS105", credits: 5, grade: "O" }
  ]
})

const filteredCourses = computed(() => {
  return courses.value.filter(course =>
    course.name.toLowerCase().includes(searchTerm.value.toLowerCase())
  )
})
</script>

<template>
  <input
    placeholder="Search"
    v-model="searchTerm"
  />

  <div v-for="course in filteredCourses" :key="course.id">
    <CourseCard
      :name="course.name"
      :code="course.code"
      :credits="course.credits"
      :grade="course.grade"
    />

    <button @click="store.enroll(course)">
      Enroll
    </button>
  </div>
</template>