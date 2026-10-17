from datetime import time
from pydantic import BaseModel, Field, ConfigDict
from decimal import  Decimal

class User(BaseModel):
    user_id: int = Field(..., description="Уникальный идентификатор Пользователя")
    user_name: str = Field(..., max_length=50, description= "Имя Пользователя")
    role: str =  Field(..., max_length=50, description="Выбранная роль Пользователя")
    rank: str = Field(..., max_length=50, description="Ранг или звание Пользователя")

class GameSession(BaseModel):
    session_id: int = Field(..., description="Уникальный идентификатор игрововй сессии")
    user_id:  int|None = Field(None, description="Уникальный идентификатор пользователя, если есть")
    game_mode: int = Field(..., description="Режим сессии")
    level_id: int = Field(..., description="Уникальный идентификатор уровня")
    difficulty : int = Field(..., description= "Уровень Сложности")
    location: str = Field(..., max_length=50, description= "Игровая локация")
    result: int= Field(..., description= "Результат")
    completion_time: time = Field(..., description="Время прохождения") # Возможно понадобится исправление. На данный записывает время прохождения, а не за сколько было пройдено.
    error_count: int = Field(..., description= "Количество ошибок")
    score: int = Field(..., description="Набранные очки")
    achievements: str = Field(..., max_length=100, description= "Полученные достижения")

class Notification(BaseModel):
    notification_id : int = Field(..., description="Уникальный идентификатор уведомления")
    session_id: int|None = Field(None, description="Уникальный идентификатор сессии, если есть")
    notification_type: int = Field(..., description="Тип Уведомления")
    message: str = Field(..., max_length=200, description= "Текст Уведомления")

class Report(BaseModel):
    report_id: int = Field(..., description="Уникальный идентификатор отчёта")
    session_id: int|None = Field(None, description="Уникальный идентификатор сессии, если есть")
    detailed_report: str = Field(..., max_length=200, description= "Подробный разбор")
    recommendation: str = Field(..., max_length=100, description= "Полученные достижения")