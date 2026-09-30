<template>
    <div class="role-page">
        <div class="content">
            <h1 class="title">Выбор роли:</h1>

            <div class="roles">
                <button class="role-btn" @click="selectRole('schoolboy')">Школьник</button>
                <button class="role-btn" @click="selectRole('student')">Студент</button>
                <button class="role-btn" @click="selectRole('senior')">Пожилой человек</button>
            </div>
        </div>

        <img src="../assets/icons/circuit1.png" alt="circuit1-bg"/>
    </div>
</template>

<script setup lang="ts">
import { useRouter } from 'vue-router'
import { useUserStore } from '../stores/userStore'
import type { UserRole } from '../types/models'

const router = useRouter()
const userStore = useUserStore()

function selectRole(role: UserRole) {
    userStore.setRole(role)
    router.push('/mode')
}
</script>

<style scoped>
.role-page {
    min-height: 100vh;
    height: 100vh;
    background: #ffffff;
    display: flex;
    align-items: center;
    justify-content: center;
    font-family: Arial, sans-serif;
    padding: 40px 60px;    
    position: relative;
    overflow: hidden;
    box-sizing: border-box;
}

.content {
    text-align: left;
    z-index: 2;
    max-width: 600px;
    margin-right: 80px;    
    margin-bottom: 120px;
}

.title {
    font-size: 64px;
    font-weight: 900;
    margin-bottom: 120px;
    letter-spacing: 1px;
}

.roles {
    display: flex;
    flex-direction: column;
    gap: 40px;
}

.role-btn {
    background: none;
    border: none;
    font-size: 40px;
    font-style: italic;
    font-family: inherit;
    color: #000;
    cursor: pointer;
    padding: 0;
    text-align: left;
    transition: transform 0.2s;
}

.role-btn:hover {
    transform: translateX(15px);
}

.circuit1-bg {
    position: absolute;
    right: -100px;
    top: 50%;    
    transform: translateY(-50%);
    height: 70%;
    width: auto;
    pointer-events: none;
    z-index: 1;    
}
</style>