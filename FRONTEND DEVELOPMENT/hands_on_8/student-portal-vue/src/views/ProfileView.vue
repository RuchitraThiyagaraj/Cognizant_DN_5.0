<script setup>

import {useEnrollmentStore} from '../stores/enrollment'

const store=useEnrollmentStore()

</script>

<template>

<h2>Enrolled Courses</h2>

<div

v-for="course in store.enrolledCourses"

:key="course.id"

>

{{ course.name }}

</div>

<h3>

Total Credits

{{ store.totalCredits }}

</h3>

</template>