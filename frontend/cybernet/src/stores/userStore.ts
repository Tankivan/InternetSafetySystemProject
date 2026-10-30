import { defineStore } from "pinia"
import { ref } from "vue"
import type { UserRole, GameMode } from "../types/models"

export const useUserStore = defineStore('user', () => {
    const role = ref<UserRole | null>(null)
    const mode = ref<GameMode | null>(null)
    const userName = ref<string>('Игрок')

    // Поля результата
    const levelResult = ref<string>('Пройден')
    const timeResult = ref<string>('00:00:00')
    const errorsResult = ref<number | null>(null)
    const achievementsResult = ref<string>('Нет')

    function setRole(newRole: UserRole) {
        role.value = newRole
    }

    function setMode(newMode: GameMode) {
        mode.value = newMode
    }

    function setUserName(name: string) {
        userName.value = name
    }

    function setResult(data: {
        level?: string
        time?: string
        errors?: number | null
        achievements?: string
    }) {
        if (data.level !== undefined) levelResult.value = data.level
        if (data.time !== undefined) timeResult.value = data.time
        if (data.errors !== undefined) errorsResult.value = data.errors
        if (data.achievements !== undefined) achievementsResult.value = data.achievements
    }

    function reset() {
        role.value = null
        mode.value = null
        userName.value = 'Игрок'
        levelResult.value = 'Пройден'
        timeResult.value = '00:00:00'
        errorsResult.value = null
        achievementsResult.value = 'Нет'
    }

    return {
        role,
        mode,
        userName,
        levelResult,
        timeResult,
        errorsResult,
        achievementsResult,
        setRole,
        setMode,
        setUserName,
        setResult,
        reset
    }
})