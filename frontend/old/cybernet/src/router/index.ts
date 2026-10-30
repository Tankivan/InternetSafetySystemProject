import { createRouter, createWebHistory } from "vue-router"
import MainMenuView from "../views/MainMenuView.vue"
import RoleSelectView from "../views/RoleSelectView.vue"
import GameModeView from "../views/GameModeView.vue"
import GameSessionView from "../views/GameSessionView.vue"
import ResultView from "../views/ResultView.vue"
import StatisticsView from "../views/StatisticsView.vue"

const router = createRouter({
    history: createWebHistory(),
    routes: [
        {path: '/', name: 'menu', component: MainMenuView},
        {path: '/role', name: 'role', component: RoleSelectView},
        {path: '/mode', name: 'mode', component: GameModeView},
        {path: '/game', name: 'game', component: GameSessionView},
        {path: '/result', name: 'result', component: ResultView},
        {path: '/stastistic', name: 'stastistic', component: StatisticsView}
    ]
})

export default router