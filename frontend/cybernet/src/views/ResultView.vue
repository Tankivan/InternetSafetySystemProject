<template>
    <div class="result-page">
        <div class="top-section">
            <img src="../assets/icons/result.png" alt="result" class="gauge-img"/>
            <div class="title-wrapper">
                <h1 class="title">Результат</h1>
                <div class="title-line"></div>
            </div>
        </div>

        <div class="stats-list">
            <div class="stat-row">
                <span class="stat-label">Уровень:</span>
                <span class="stat-value">{{ levelText }}</span>
            </div>
            <div class="stat-row">
                <span class="stat-label">Время:</span>
                <span class="stat-value">{{ timeText }}</span>
            </div>
            <div class="stat-row">
                <span class="stat-label">Ошибки:</span>
                <span class="stat-value">{{ errorsText }}</span>
            </div>
            <div class="stat-row">
                <span class="stat-label">Достижения:</span>
                <span class="stat-value">{{ achievementsText }}</span>
            </div>
        </div>

        <div class="bottom-buttons">
            <button class="bottom-btn" @click="goToStatistics">
                <span class="btn-text">Статистика</span>
            </button>
            <div class="divider"></div>
            <button class="bottom-btn" @click="goToMenu">
                <span class="btn-text">Меню</span>
            </button>
        </div>
    </div>
</template>

<script setup lang="ts">
import { computed } from 'vue'
import { useRouter } from 'vue-router'
import { useUserStore } from '../stores/userStore'

const router = useRouter()
const userStore = useUserStore()

const levelText = computed(() => userStore.levelResult || 'Пройден')
const timeText = computed(() => userStore.timeResult || '00:00:00')
const errorsText = computed(() => userStore.errorsResult ?? '.......')
const achievementsText = computed(() => userStore.achievementsResult || 'Нет')

function goToStatistics() {
    router.push('/statistics')
}

function goToMenu() {
    router.push('/')
}
</script>

<style scoped>
.result-page {
    min-height: 100vh;
    height: 100vh;
    background: #f5f5f7;
    font-family: Arial, sans-serif;
    position: relative;
    overflow: hidden;
    box-sizing: border-box;
}

.top-section {
    position: absolute;
    top: 50px;
    left: 60px;
    right: 60px;
    display: flex;
    align-items: flex-start;
    gap: 40px;
}

.gauge-img {
    height: 300px;
    width: auto;
    pointer-events: none;
    mix-blend-mode: multiply;
    position: relative;
    z-index: 1;
    margin-left: 100px;
    margin-top: -20px;
}

.title-wrapper {
    flex: 1;
    padding-top: 40px;
    margin-left: -300px;
}

.title {
    font-size: 52px;
    font-weight: 700;
    font-style: italic;
    color: #000;
    margin: 0 0 25px 0;
    letter-spacing: 1px;
}

.title-line {
    height: 2px;
    background: #000;
    width: 60%;
    margin-left: 130px;
    position: relative;
    z-index: 2;
}

.stats-list {
    position: absolute;
    top: 50%;
    transform: translateY(-50%);
    left: 340px;
    display: flex;
    flex-direction: column;
    gap: 25px;
}

.stat-row {
    font-size: 38px;
    display: flex;
    gap: 15px;
    align-items: baseline;
}

.stat-label {
    font-weight: 700;
    font-style: italic;
    color: #000;
}

.stat-value {
    font-weight: 400;
    font-style: italic;
    color: #000;
}

/* Кнопки в правом нижнем углу */
.bottom-buttons {
    position: absolute;
    bottom: 50px;
    right: 80px;
    display: flex;
    align-items: flex-end;
}

.bottom-btn {
    background: none;
    border: none;
    font-size: 38px;
    font-weight: 700;
    font-style: italic;
    font-family: inherit;
    color: #000;
    cursor: pointer;
    padding: 0 40px 12px 40px;
    border-bottom: 2px solid #000;
}

.btn-text {
    display: inline-block;
    transition: transform 0.2s;
}

.bottom-btn:hover .btn-text {
    transform: translateX(15px);
}

.divider {
    width: 2px;
    height: 90px;
    background: #000;
    align-self: flex-end;
    margin-bottom: -25px;
}
</style>