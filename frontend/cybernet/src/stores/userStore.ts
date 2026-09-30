import { defineStore } from "pinia"
import { ref } from "vue"
import type { UserRole } from "../types/models"

export const useUserStore = defineStore('user', () => {
    const role = ref<UserRole | null>(null)
    const userName = ref<string>('Игрок')

    function setRole(newRole: UserRole){
        role.value = newRole
    }

    function setUserName(name: string){
        userName.value = name
    }

    function reset() {
        role.value = null
        userName.value = 'Игрок'
    }

    return {
        role,
        userName,
        setRole,
        setUserName,
        reset
    }
})