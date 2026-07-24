<template>
<div class="card">
    <h3>{{ name }}</h3>
    <p>Code : {{ code }}</p>
    <p>Credits : {{ credits }}</p>
    <p>Grade : {{ grade }}</p>
</div>
</template>

<script setup>

defineProps({
    name:String,
    code:String,
    credits:Number,
    grade:String
})

</script>

<style scoped>
.card{
    border:1px solid gray;
    padding:10px;
    margin:10px;
}
</style>