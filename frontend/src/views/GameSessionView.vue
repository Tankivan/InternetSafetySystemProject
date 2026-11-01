<template>
    <div class="game-page">
     <img src="../assets/icons/circuit3.png" alt="" class="circuit3-bg" />

     <div class="content">
        <div v-if="currentScenario" class="game-content">            
        
        <div class="speech-bubble">
            <div class="situation-text">{{ displayedText }}<span v-if="isTyping" class="cursor">|</span>
            </div>        
        </div>

        <div class="typing-label" v-show="isTyping">Печатает...</div>

        <div class="variants">
            <button v-for="(variant, index) in currentScenario.variants" :key="index" class="variant-btn" 
            :class="{
                'correct': selectedVariantIndex !== null && variant.correct,
                'wrong': selectedVariantIndex === index && !variant.correct,
                'disable': selectedVariantIndex !== null
            }"
            :disabled="selectedVariantIndex !== null"
            @click="handleAnswer(index)">{{ variant.text }}            
            </button>
        </div>
    </div>

        <div v-else>
            <h2>Сценарий не найден! Выберите роль заново.</h2>
        </div>

        <div v-if="selectedVariantIndex !== null" class="feedback-block">
            <p class="feedback-text">{{ currentScenario.variants[selectedVariantIndex].explanation }}</p>
            <button class="next-btn" @click="handleNext">Далее</button>
        </div>

        <div class="hint-container" v-if="selectedVariantIndex === null">
            <button class="hint-btn" @click="showHint = true">
                Подсказка
            </button>
        </div>

        <div v-if="showHint" class="modal-overlay" @click.self="showHint = false">
            <div class="modal-content">
                <h2>Подсказка</h2>
                <p>{{ currentHint }}</p>
                <button class="close-btn" @click="showHint = false">Понятно</button>
            </div>
        </div>
     </div>
    </div>
</template>

<script setup lang="ts">
import { computed, onMounted, ref } from 'vue'
import { useUserStore } from '../stores/userStore'
import { scenarios } from '../data/scenarios'
import { notifications } from '../data/notifications'

const showHint = ref(false)

const currentHint = computed(() => {
    if (!userStore.role)
    return ''
    const hint = notifications.find(n => n.role === userStore.role)
    return hint ? hint.message: 'Подсказка не найдена!'
})

const userStore = useUserStore()

const roleScenarios = computed(() => {
    return scenarios.filter(s => s.role === userStore.role)
})

const currentScenario = computed (() => {
    return roleScenarios.value[0]
})

const displayedText = ref('')
const isTyping = ref(false)

function startTyping(text: string) {
    displayedText.value = ''
    isTyping.value = true
    let i = 0

    const interval = setInterval(() => {
        if (i < text.length) {
            displayedText.value += text[i]
            i++
        }
        else {
            clearInterval(interval)
            isTyping.value = false
        }
    }, 50)
}

onMounted(() => {
    if (currentScenario.value) {
        userStore.startGameTimer()
        startTyping(currentScenario.value.situation)
    }
})

const selectedVariantIndex = ref<number | null>(null)

function handleAnswer(index: number) {
    if (selectedVariantIndex.value !== null)
    return

selectedVariantIndex.value = index

const isCorrect = currentScenario.value.variants[index].correct
    if (!isCorrect) {
        userStore.addError()
    }
}

import { useRouter } from 'vue-router'

const router = useRouter()

function handleNext() {
    userStore.stopGameTimer()
    router.push('/result')
}
</script>

<style scoped>
.game-page {
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
    margin-left: 250px;
}

.speech-bubble {  
    border: 3px solid #000; 
    border-radius: 40px; 
    padding: 15px 30px;    
    margin-bottom: 15px;   
    display: inline-block;  
    width: 500px;
    box-sizing: border-box;  
    position: relative;
    top: -60px;
    z-index: 1;
}

.speech-bubble::after {
    content: '';
    position: absolute;
    left: 11px;
    bottom: -2.5px;
    width: 18px;
    height: 10px;
    background: #ffffff;
    border-left: 3px solid #000;
    border-bottom: 3px solid #000;
    transform: skew(-30deg);
    z-index: -1;
}

.variants {
    display: flex;
    flex-direction: column;
    gap: 20px;
    position: relative;
    top: 60px;
    left: 60px;
}

.variant-btn:nth-child(1) {
    margin-left: 0;
}

.variant-btn:nth-child(2) {
    margin-left: 60px;
}

.variant-btn:nth-child(3) {
    margin-left: 120px;
}

.variant-btn {
    background: #ffffff;
    border: 2px solid #000;
    border-radius: 50px;
    padding: 12px 35px;
    font-size: 22px;
    font-family: inherit;
    cursor: pointer;
    transition: all 0.2s;
    text-align: center;
    width: 450px;
    max-width: 100%;
}

.variant-btn:hover {
    background: #000;
    color: #fff;
}

.variant-btn.correct {
    background: #e6ffe6;
    border-color: #00cc00;
    color: #006600;
}

.variant-btn.wrong {
    background: #ffe6e6;
    border-color: #cc0000;
    color: #990000;
}

.variant-btn.disable {
    cursor: default;
    opacity: 0.7;
}

.feedback-block {
    margin-top: 20px;
    padding: 20px;
    background: #f9f9f9;
    border-radius: 20px;
    border: 2px solid #ccc;
    position: relative;
    top: 80px;
    left: 60px;
    max-width: 450px;
}

.feedback-text {
    font-size: 18px;
    margin-bottom: 15px;
    line-height: 1.4;
}

.next-btn {
    padding: 10px 30px;
    font-size: 18px;
    background: #000;
    color: #fff;
    border: none;
    border-radius: 30px;
    cursor: pointer;
    font-family: inherit;
}

.circuit3-bg {
    position: absolute;
    left: 10px;
    top: 50%;
    transform: translateY(-50%);
    height: 75%;
    width: auto;
    pointer-events: none;
    z-index: 1;
    opacity: 1;
}

.typing-label {
    font-size: 24px;
    font-style: italic;
    margin-bottom: 60px;
    margin-left: 250px;
    color: #000;
    text-align: right;
}

.situation-text {
    font-size: 18px;
    line-height: 1.5;
    color: #000;
    text-align: left;
}

.cursor {
    animation: blink 1s step-end infinite;
    font-weight: bold;
}

@keyframes blink {
    0%, 100% { opacity: 1; }
    50% { opacity: 0; }
}

.hint-container {
    position: absolute;
    top: 100px;
    right: 50px;
}

.hint-btn {
    background: #fff;
    border: 2px solid #000;
    border-radius: 30px;
    padding: 10px 20px;
    font-size: 18px;
    cursor: pointer;
    transition: all 0.2s;
}

.hint-btn:hover {
    background: #000;
    color: #fff;
}

.modal-overlay {
    position: fixed;
    top: 0;
    left: 0;
    width: 100vw;
    height: 100vh;
    background: rgba(0, 0, 0, 0.6);
    display: flex;
    align-items: center;
    justify-content: center;
    z-index: 999;
}

.modal-content {
    background: #fff !important;
    padding: 40px;
    border-radius: 30px;
    max-width: 600px;
    text-align: left;
    box-shadow: 0 10px 30px rgba(0,0,0,0.3);
    position: relative;
    z-index: 1000;
}

.modal-content h2 {
    font-size: 32px;
    margin-bottom: 20px;
}

.modal-content p {
    font-size: 20px;
    line-height: 1.5;
    margin-bottom: 30px;
}

.close-btn {
    background: #000;
    color: #fff;
    border: none;
    padding: 12px 40px;
    font-size: 18px;
    border-radius: 30px;
    cursor: pointer;
}
</style>