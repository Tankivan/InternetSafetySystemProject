export type UserRole = 'schoolboy' | 'student' | 'senior'

export type GameMode = 'story' | 'minigame' | 'time'

export interface User 
{
    user_id: number
    user_name: string
    role: UserRole
    rank: string
}

export interface GameSession
{
    session_id: number
    user_id: number
    game_mode: GameMode
    level_id: number
    difficulty: number
    location: string
    result: number
    completion_time: string
    error_count: number
    score: number
    achievements: string
}

export interface Variant 
{
    text: string
    correct: boolean
    explanation: string
}

export interface Scenario
{
    id: number
    role: UserRole
    level: number
    situation: string
    variants: Variant[]
}