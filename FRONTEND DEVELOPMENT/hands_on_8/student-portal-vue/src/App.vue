<script setup>

import Header from './components/Header.vue'

</script>

<template>

<Header/>

<nav>

<RouterLink to="/">Home</RouterLink>

|

<RouterLink to="/courses">Courses</RouterLink>

|

<RouterLink to="/profile">Profile</RouterLink>

</nav>

<RouterView/>

</template>