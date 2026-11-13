<template>
    <div class="mode-page">
      <img src="../assets/icons/circuit2.png" alt="" class="circuit2-bg" />

      <div class="content">
        <h1 class="title">
            Выбор роли: <span class="role-name">{{ roleTitle }}</span>
        </h1>

        <div class="modes">
            <button class="mode-btn" @click="selectMode('story')">
                Сюжет
            </button>

            <button class="mode-btn" @click="selectMode('minigame')">
                Мини-игры
            </button>

            <button class="mode-btn" @click="selectMode('time')">
                Испытание на время
            </button>
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

const roleTitle = computed(() => {
    if (userStore.role === 'schoolboy') return 'Школьник'
    if (userStore.role === 'student') return 'Студент'
    if (userStore.role === 'senior') return 'Пожилой человек'
    return ''
})

function selectMode(mode: GameMode) {
    userStore.setMode(mode)
    router.push('/game')
}
</script>

<style scoped>
.mode-page {
    height: 100vh;
    background: #ffffff;
    display: flex;    
    align-items: center;
    justify-content: center;
    font-family: Arial, sans-serif;
    padding: 40px 60px;   
    box-sizing: border-box; 
    position: relative;
    overflow: hidden;
}

.content {
    text-align: left;
    z-index: 2;
    max-width: 700px;
    margin-left: 300px;
    margin-bottom: 100px;
}

.title {
    font-size: 45px;
    font-weight: 900; 
    margin-top: -29px;   
    margin-bottom: 20px;
    letter-spacing: 1px;
    white-space: nowrap;
}

.role-name {
    font-style: italic;
    font-weight: 900;
    display: inline;
}

.modes {
    display: flex;
    flex-direction: column;
    gap: 35px;
    margin-top: 150px;
    margin-left: 40px;
}

.mode-btn {
    background: none;
    border: none;
    font-size: 38px;
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

.circuit2-bg {
    position: absolute;
    left: 20px;
    top: 50%;
    transform: translateY(-50%);
    height: 75%;
    width: auto;
    pointer-events: none;
    z-index: 1;
    opacity: 1;
}
</style>