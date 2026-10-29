from datetime import time
from pydantic import BaseModel, Field, ConfigDict
from decimal import  Decimal
from typing import Optional

class User(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    user_id: int = Field(..., description="Уникальный идентификатор Пользователя")
    user_name: str = Field(..., max_length=50, description= "Имя Пользователя")
    role: str =  Field(..., max_length=50, description="Выбранная роль Пользователя")
    rank: str = Field(..., max_length=50, description="Ранг или звание Пользователя")

class GameSession(BaseModel):
    model_config = ConfigDict(from_attributes=True)
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
    model_config = ConfigDict(from_attributes=True)
    notification_id : int = Field(..., description="Уникальный идентификатор уведомления")
    session_id: int|None = Field(None, description="Уникальный идентификатор сессии, если есть")
    notification_type: int = Field(..., description="Тип Уведомления")
    message: str = Field(..., max_length=200, description= "Текст Уведомления")

class Report(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    report_id: int = Field(..., description="Уникальный идентификатор отчёта")
    session_id: int|None = Field(None, description="Уникальный идентификатор сессии, если есть")
    detailed_report: str = Field(..., max_length=200, description= "Подробный разбор")
    recommendation: str = Field(..., max_length=100, description= "Полученные достижения")

class UserCreate(BaseModel):
    user_name: str
    role: str
    rank: str


class UserUpdate(BaseModel):
    user_name: Optional[str] = None
    role: Optional[str] = None
    rank: Optional[str] = None


class GameSessionCreate(BaseModel):
    user_id: Optional[int] = None
    game_mode: int
    level_id: int
    difficulty: int
    location: str
    result: int = 0
    completion_time: "time"  # см. import ниже
    error_count: int
    score: int
    achievements: str


class GameSessionUpdate(BaseModel):
    user_id: Optional[int] = None
    game_mode: Optional[int] = None
    level_id: Optional[int] = None
    difficulty: Optional[int] = None
    location: Optional[str] = None
    result: Optional[int] = None
    completion_time: Optional["time"] = None
    error_count: Optional[int] = None
    score: Optional[int] = None
    achievements: Optional[str] = None


class NotificationCreate(BaseModel):
    session_id: Optional[int] = None
    notification_type: int
    message: str


class NotificationUpdate(BaseModel):
    session_id: Optional[int] = None
    notification_type: Optional[int] = None
    message: Optional[str] = None


class ReportCreate(BaseModel):
    session_id: Optional[int] = None
    detailed_report: str
    recommendation: str


class ReportUpdate(BaseModel):
    session_id: Optional[int] = None
    detailed_report: Optional[str] = None
    recommendation: Optional[str] = None