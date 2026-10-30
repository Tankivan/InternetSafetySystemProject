<template>
    <div class="settings-page">
        <div class="content">
            <h1 class="title">Настройки</h1>
            <div class="title-line"></div>

            <div class="settings-list">
                <!-- Имя игрока -->
                <div class="setting-row">
                    <span class="setting-label">Имя игрока:</span>
                    <input
                        class="setting-input"
                        type="text"
                        :value="settingsStore.userName"
                        @input="onNameInput"
                        maxlength="20"
                    />
                </div>
                <div class="setting-row">
                    <span class="setting-label">Сложность:</span>
                    <div class="difficulty-options">
                        <button
                            class="diff-btn"
                            :class="{ active: settingsStore.difficulty === 'easy' }"
                            @click="settingsStore.setDifficulty('easy')"
                        >Лёгкая</button>
                        <button
                            class="diff-btn"
                            :class="{ active: settingsStore.difficulty === 'medium' }"
                            @click="settingsStore.setDifficulty('medium')"
                        >Средняя</button>
                        <button
                            class="diff-btn"
                            :class="{ active: settingsStore.difficulty === 'hard' }"
                            @click="settingsStore.setDifficulty('hard')"
                        >Сложная</button>
                    </div>
                </div>
            </div>

            <div class="bottom-buttons">
                <button class="bottom-btn" @click="settingsStore.resetSettings()">
                    <span class="btn-text">Сбросить</span>
                </button>
                <button class="bottom-btn" @click="$router.back()">
                    <span class="btn-text">Назад</span>
                </button>
            </div>
        </div>

        <img src="../assets/icons/circuit1.png" alt="circuit-bg" class="circuit-bg"/>
    </div>
</template>

<script setup lang="ts">
import { useSettingsStore } from '../stores/settingsStore'

const settingsStore = useSettingsStore()

function onNameInput(event: Event) {
    const target = event.target as HTMLInputElement
    settingsStore.setUserName(target.value)
}
</script>

<style scoped>
.settings-page {
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
    right: -120px;
    top: 50%;
    transform: translateY(-50%);
    height: 85%;
    width: auto;
    pointer-events: none;
    z-index: 1;
    mix-blend-mode: multiply;
}

.content {
    z-index: 2;
    position: relative;
    width: 100%;
    max-width: 800px;
    margin-right: 200px;
}

.title {
    font-size: 52px;
    font-weight: 700;
    font-style: italic;
    color: #000;
    margin: 0 0 15px 0;
    letter-spacing: 1px;
}

.title-line {
    height: 2px;
    background: #000;
    width: 100%;
    margin-bottom: 60px;
}

/* Строки настроек */
.settings-list {
    display: flex;
    flex-direction: column;
    gap: 50px;
}

.setting-row {
    display: flex;
    align-items: center;
    gap: 25px;
    font-size: 34px;
}

.setting-label {
    font-weight: 700;
    font-style: italic;
    color: #000;
    min-width: 260px;
}

/* Поле ввода имени */
.setting-input {
    background: transparent;
    border: none;
    border-bottom: 2px solid #000;
    font-size: 34px;
    font-style: italic;
    font-family: inherit;
    color: #000;
    padding: 0 10px 6px 10px;
    width: 300px;
    outline: none;
}

/* Сложность */
.difficulty-options {
    display: flex;
    gap: 30px;
}

.diff-btn {
    background: none;
    border: none;
    font-size: 34px;
    font-style: italic;
    font-family: inherit;
    color: #000;
    cursor: pointer;
    padding: 0 0 6px 0;
    border-bottom: 2px solid transparent;
    transition: transform 0.2s;
}

.diff-btn:hover {
    transform: translateX(10px);
}

.diff-btn.active {
    font-weight: 700;
    border-bottom: 2px solid #000;
}

/* Кнопки внизу */
.bottom-buttons {
    display: flex;
    gap: 60px;
    margin-top: 80px;
}

.bottom-btn {
    background: none;
    border: none;
    font-size: 34px;
    font-weight: 700;
    font-style: italic;
    font-family: inherit;
    color: #000;
    cursor: pointer;
    padding: 0 20px 10px 20px;
    border-bottom: 2px solid #000;
    transition: transform 0.2s;  
}

.btn-text {
    display: inline-block;
    transition: transform 0.2s;
}

.bottom-btn:hover {
    transform: translateX(15px);
}
</style>