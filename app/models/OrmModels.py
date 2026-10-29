from datetime import datetime
from sqlalchemy import Integer, String, Boolean, DateTime
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy.orm import sessionmaker, DeclarativeBase
from sqlalchemy import ForeignKey, Time
from ..database.database import Base
from typing import Optional

class UserORM(Base):
    __tablename__ = "User"

    user_id: Mapped[int] = mapped_column(Integer, primary_key=True)
    user_name: Mapped[str] = mapped_column(String(50), nullable=False)
    role: Mapped[str] = mapped_column(String(50), nullable=False)
    rank: Mapped[str] = mapped_column(String(50), nullable=False)


class GameSessionORM(Base):
    __tablename__ = "GameSession"

    session_id: Mapped[int] = mapped_column(Integer, primary_key=True)
    user_id: Mapped[Optional[int]] = mapped_column(
        ForeignKey("User.user_id"), nullable=True
    )
    game_mode: Mapped[int] = mapped_column(Integer, nullable=False)
    level_id: Mapped[int] = mapped_column(Integer, nullable=False)
    difficulty: Mapped[int] = mapped_column(Integer, nullable=False)
    location: Mapped[str] = mapped_column(String(50), nullable=False)
    result: Mapped[int] = mapped_column(Integer, nullable=False, default=0)
    completion_time: Mapped[object] = mapped_column(Time, nullable=False)
    error_count: Mapped[int] = mapped_column(Integer, nullable=False)
    score: Mapped[int] = mapped_column(Integer, nullable=False)
    achievements: Mapped[str] = mapped_column(String(100), nullable=False)


class NotificationORM(Base):
    __tablename__ = "Notification"

    notification_id: Mapped[int] = mapped_column(Integer, primary_key=True)
    session_id: Mapped[Optional[int]] = mapped_column(
        ForeignKey("GameSession.session_id"), nullable=True
    )
    notification_type: Mapped[int] = mapped_column(Integer, nullable=False)
    message: Mapped[str] = mapped_column(String(200), nullable=False)


class ReportORM(Base):
    __tablename__ = "Report"

    report_id: Mapped[int] = mapped_column(Integer, primary_key=True)
    session_id: Mapped[Optional[int]] = mapped_column(
        ForeignKey("GameSession.session_id"), nullable=True
    )
    detailed_report: Mapped[str] = mapped_column(String(200), nullable=False)
    recommendation: Mapped[str] = mapped_column(String(100), nullable=False)