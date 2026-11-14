import { defineStore } from "pinia"
import { ref } from "vue"
import type { GameMode, UserRole } from "../types/models"

export const useUserStore = defineStore('user', () => {
    const role = ref<UserRole | null>(null)
    const mode = ref<GameMode | null>(null)
    const userName = ref<string>('Игрок')
    const errorsCount = ref<number>(0)
    const startTime = ref<number>(0)
    const completionTime = ref<string>('00:00:00')
    

    function setRole(newRole: UserRole){
        role.value = newRole
    }

    function setMode(newMode: GameMode){
        mode.value = newMode
    }

    function setUserName(name: string){
        userName.value = name
    }

    function addError() {
        errorsCount.value++
    }

    function startGameTimer() {
        errorsCount.value = 0
        startTime.value = Date.now()
    }

    function stopGameTimer() {
        if (startTime.value === 0)
            return
        const endTime = Date.now()
        const diff = endTime - startTime.value

        const seconds = Math.floor(diff / 1000)
        const h = Math.floor(seconds / 3600).toString().padStart(2, '0')
        const m = Math.floor((seconds % 3600) / 60).toString().padStart(2, '0')
        const s = (seconds % 60).toString().padStart(2, '0')

        completionTime.value = `${h}:${m}:${s}`
    }

    function reset() {
        role.value = null
        mode.value = null
        userName.value = 'Игрок'
    }

    return {
        role,
        mode,
        userName,
        setRole,
        setMode,
        setUserName,
        reset,
        errorsCount,
        completionTime,
        addError,
        startGameTimer,
        stopGameTimer
    }
})