<template>
    <div class="mode-page">
        <img src="../assets/icons/circuit1.png" alt="circuit-bg" class="circuit-bg"/>

        <div class="content">
            <h1 class="title">
                Выбор роли: <span class="role-name">{{ roleName }}</span>
            </h1>

            <div class="modes">
                <button class="mode-btn" @click="selectMode('story')">Сюжет</button>
                <button class="mode-btn" @click="selectMode('minigame')">Мини-игры</button>
                <button class="mode-btn" @click="selectMode('time')">Испытание на время</button>
            </div>
        </div>
    </div>
</template>

<script setup lang="ts">
import { computed } from 'vue'
import { useRouter } from 'vue-router'
import { useUserStore } from '../stores/userStore'
import type { GameMode } from '../types/models'

const router = useRouter()
const userStore = useUserStore()

const roleNames: Record<string, string> = {
    schoolboy: 'Школьник',
    student: 'Студент',
    senior: 'Пожилой человек',
}

const roleName = computed(() => {
    const role = userStore.role
    return role ? roleNames[role] || 'Не выбрана' : 'Не выбрана'
})

function selectMode(mode: GameMode) {
    userStore.setMode(mode)
    router.push(`/game/${mode}`)
}
</script>

<style scoped>
.mode-page {
    min-height: 100vh;
    height: 100vh;
    background: #f5f5f7;
    display: flex;
    align-items: center;
    justify-content: center;
    font-family: Arial, sans-serif;
    padding: 40px 60px;
    position: relative;
    overflow: hidden;
    box-sizing: border-box;
}

.circuit-bg {
    position: absolute;
    left: -180px;
    top: 50%;
    transform: translateY(-50%);
    height: 110%;
    width: auto;
    pointer-events: none;
    z-index: 1;
    mix-blend-mode: multiply;
}

.content {
    margin-top: -50px;
    text-align: left;
    z-index: 2;
    max-width: 700px;
    margin-left: 380px;
    position: relative;
    display: flex;
    flex-direction: column;
    justify-content: space-between;
    height: 70vh;
    padding-top: 0;
}

.title {
    font-size: 52px;
    font-weight: 900;
    letter-spacing: 1px;
    color: #000;
    margin: 0;
}

.role-name {
    font-size: 42px;
    font-weight: 400;
    font-style: italic;
    margin-left: 10px;
}

.modes {
    display: flex;
    flex-direction: column;
    gap: 40px;
    margin-bottom: 80px;
}

.mode-btn {
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

.mode-btn:hover {
    transform: translateX(15px);
}
</style>