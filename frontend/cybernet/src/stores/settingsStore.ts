import { defineStore } from "pinia"
import { ref } from "vue"

export type Difficulty = 'easy' | 'medium' | 'hard'

const STORAGE_KEY = 'game-settings'

export const useSettingsStore = defineStore('settings', () => {
    const userName = ref<string>('Игрок')
    const difficulty = ref<Difficulty>('medium')

    function save() {
        localStorage.setItem(STORAGE_KEY, JSON.stringify({
            userName: userName.value,
            difficulty: difficulty.value,
        }))
    }

    function load() {
        const raw = localStorage.getItem(STORAGE_KEY)
        if (!raw) return
        try {
            const data = JSON.parse(raw)
            userName.value = data.userName ?? 'Игрок'
            difficulty.value = data.difficulty ?? 'medium'
        } catch {
        }
    }

    function setUserName(name: string) {
        userName.value = name
        save()
    }

    function setDifficulty(value: Difficulty) {
        difficulty.value = value
        save()
    }

    function resetSettings() {
        userName.value = 'Игрок'
        difficulty.value = 'medium'
        save()
    }

    load()

    return {
        userName,
        difficulty,
        setUserName,
        setDifficulty,
        resetSettings,
    }
})