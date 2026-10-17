from sqlalchemy import Integer, String, Boolean
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy.orm import sessionmaker, DeclarativeBase
from sqlalchemy import ForeignKey


class Base(DeclarativeBase):
    pass

class Notification(Base):
    __tablename__ = "Notification"

    notification_id: Mapped[int] = mapped_column(Integer, primary_key= True)
    session_id: Mapped[int | None] = mapped_column(ForeignKey("GameSession.session_id"), nullable=True)
    notification_type: [int] = mapped_column(Integer, nullable=False)
    message: [str] = mapped_column(String(200), nullable=False)