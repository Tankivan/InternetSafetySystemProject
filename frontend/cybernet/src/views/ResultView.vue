<template>
    <div class="page">
        <h1>Результат</h1>
        <button @click="$router.push('/')">Назад в меню</button>
    </div>
</template>

<script setup lang="ts">
</script>

<style scoped>
.page {
    min-height: 100vh;
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: center;
    font-family: Arial, sans-serif;
}
</style>