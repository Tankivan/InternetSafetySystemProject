import type { UserRole } from "../types/models"

export interface NotificationData {
    notification_id: number
    role: UserRole
    notification_type: number
    message: string
}

export const notifications: NotificationData[] = [
    {
        notification_id: 1,
        role: 'schoolboy',
        notification_type: 1,
        message: 'Никогда не сообщай свои личные данные (номер телефона, адрес) незнакомцам. Настоящие друзья не просят номер телефона ради игрового скина!'
    },
    {
        notification_id: 2,
        role: 'student',
        notification_type: 1,
        message: 'Всегда проверяй адрес электронной почты отправителя. Официальные электронные письма от университетов приходят только с корпоративного домена, а не с бесплатных почтовых сервисов!'
    },
    {
        notification_id: 3,
        role: 'senior',
        notification_type: 1,
        message: 'Реальные сотрудники банка никогда не просят у клиентов код из СМС! Если вам звонят и просят продиктовать код, то это мошенники.'
    }
]