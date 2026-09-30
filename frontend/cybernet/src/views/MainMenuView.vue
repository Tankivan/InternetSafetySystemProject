<template>
    <div class="main-menu">     
        <img src="../assets/icons/circuit.png" alt="" class="circuit-bg"/>
        <div class="content">
            <h1 class="title">КиберНЕТ</h1>

            <div class="menu">
                <button class="menu-btn" @click="start">
                    <img src="../assets/icons/icon-start.png" alt="СТАРТ" class="icon"/>
                    <span>СТАРТ</span>
                </button>

                <button class="menu-btn" @click="stats">
                    <img src="../assets/icons/icon-stats.png" alt="Статистика" class="icon"/>
                    <span>Статистика</span>
                </button>

                <button class="menu-btn" @click="exit">
                    <img src="../assets/icons/icon-exit.png" alt="ВЫХОД" class="icon"/>
                    <span>ВЫХОД</span>
                </button>
            </div>
        </div>   
        
        <button class="settings-btn" @click="settings">
            <img src="../assets/icons/icon-settings.png" alt="Настройки" class="settings-icon"/>        
        </button>
    </div>
</template>

<script setup lang="ts">
import { useRouter } from 'vue-router'

const router = useRouter()

function start(){
    router.push('/role')
}

function stats(){
    router.push('/statistics')
}

function exit(){
    if (confirm('Вы уверены, что хотите выйти?')){
        window.close()
    }
}

function settings(){
    router.push('/settings')
}
</script>

<style scoped>
.main-menu {
    min-height: 100vh;
    background: #ffffff;
    display: flex;
    align-items: center;
    justify-content: flex-start;   
    font-family: Arial, sans-serif;  
    padding-left: 45%;
    position: relative;  
}

.content {    
    text-align: left;
    padding: 40px;
    max-width: 500px;     
}

.title {
    font-size: 64px;
    font-weight: 900;
    margin-bottom: 80px;
    letter-spacing: 2px;
}

.menu {
    display: flex;
    flex-direction: column;
    gap: 10px;
}

.menu-btn {
    display: flex;
    align-items: center;
    gap: 30px;
    background: none;
    border: none;
    font-size: 40px;
    font-style: italic;
    cursor: pointer;
    padding: 0;
    transition: transform 0.2s;
    font-family: inherit;
    color: #000;
}

.menu-btn:hover {
    transform: translateX(10px);
}

.icon {
    width: 100px;
    height: 100px;
    object-fit: contain;
}

.settings-btn {
    position: absolute;
    bottom: 110px;
    right: 60px;
    background: none;
    border: none;
    cursor: pointer;
    padding: 10px;
    transition: transform 0.3s;
}

.settings-btn:hover {
    transform: rotate(90deg);
}

.settings-icon {
    width: 60px;
    height: 60px;
    object-fit: contain;
}

.circuit-bg {
    position: absolute;
    left: 40px;
    top: 0;
    height: 100%;
    width: auto;
    opacity: 1;
    pointer-events: none;
}
</style>