<template>
    <div class="result-page">
        <div class="content">
            <div class="speedometer">
                <img src="../assets/icons/speedometer.png" alt="Спидометр" class="gauge-img">
            </div>

            <div class="stats-container">
            <h1 class="title">Результат</h1>
            <div class="line"></div>
        
            <div class="stats">
                <p><strong>Уровень:</strong> Пройден</p>
                <p><strong>Время:</strong> {{ userStore.completionTime }}</p>
                <p><strong>Ошибки:</strong> {{ userStore.errorsCount }}</p>
                <p><strong>Достижения:</strong> Нет</p>
            </div>

            <div class="footer-link">
                <button class="link-btn" @click="goToStatistics">Статистика</button>
                <div class="divider"></div>
                <button class="link-btn" @click="goToMenu">Меню</button>
            </div>
        </div>
    </div>
    </div>
</template>

<script setup lang="ts">
import { useRouter } from 'vue-router'
import { useUserStore } from '../stores/userStore'

const router = useRouter()
const userStore = useUserStore()

function goToStatistics() {
    router.push('/statistics')
}

function goToMenu() {
    router.push('/')
}
</script>

<style scoped>
.result-page {
    height: 100vh;
    background: #ffffff;
    display: flex;
    align-items: center;   
    justify-content: center;
    font-family: Arial, sans-serif;
}

.content {
    display: flex;
    align-items: center;
    gap: 60px;
}

.speedometer {
    width: 300px;
    height: auto;
    margin-top: -260px;
}

.gauge-img {
    width: 100%;
    height: auto;
    display: block;
}

.stats-container {
    text-align: left;
    position: relative;    
    left: -20px;
}

.title {
    font-size: 48px;
    font-weight: 900;
    font-style: italic;
    margin: 0 0 10px 0;
}

.line {
    height: 2px;
    background: #000;
    margin-bottom: 30px;
    width: calc(100% + 100px);
    transform: translateX(-179px);
}

.stats {
    font-size: 32px;
    font-style: italic;
    line-height: 1.8;
    margin-bottom: 50px;
    color: #000;
    position: relative;
    left: -30px;
}

.stats strong {
    font-style: normal;
    font-weight: bold;
}

.footer-link {
    display: flex;
    align-items: center;
    gap: 30px;
    font-size: 32px;
    font-style: italic;
    font-weight: bold;
    border-bottom: 2px solid #000;
    padding-bottom: 5px;
    width: fit-content;
    margin-top: 40px;
    position: relative;
}

.link-btn {
    padding: 0;
    font-size: inherit;
    font-weight: inherit;
    font-family: inherit;
    font-style: inherit;
    background: none;
    border: none;    
    cursor: pointer;  
    text-decoration: none;  
}

.link-btn:hover {    
    color: #666;
}

.divider {
    width: 2px;
    height: 70px;
    background: #000;
    position: absolute;
    left: 68%;
    top: 69%;
    transform: translate(-50%, -50%);
}
</style>