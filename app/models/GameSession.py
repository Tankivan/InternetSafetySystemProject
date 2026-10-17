from datetime import time
from sqlalchemy import Integer, String, Boolean, DateTime
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy.orm import sessionmaker, DeclarativeBase
from sqlalchemy import ForeignKey


class Base(DeclarativeBase):
    pass

class GameSession(Base):
    __tablename__ = "GameSession"

    session_id : Mapped[int] = mapped_column(Integer, primary_key=True)
    user_id : Mapped[int | None] = mapped_column(ForeignKey("User.user_id"), nullable= True)
    game_mode : Mapped[int] = mapped_column(Integer, nullable= False) # у сессии не может не быть игрового режима
    level_id : Mapped[int] = mapped_column(Integer, nullable= False) # у сессии не может не быть индекса уровня
    difficulty  : Mapped[int] = mapped_column(Integer, nullable=False) # такая же логика
    location : Mapped[str] = mapped_column(String(50), nullable=False)
    result : Mapped[int] = mapped_column(Integer)
    completion_time: Mapped[time] =mapped_column(DateTime) # Возможно понадобится исправление. На данный записывает время прохождения, а не за сколько было пройдено.
    error_count: Mapped[int] = mapped_column(Integer, nullable=False)
    score: Mapped[int] = mapped_column(Integer, nullable= False)
    achievements: Mapped[str] = mapped_column(String(100), nullable=False)