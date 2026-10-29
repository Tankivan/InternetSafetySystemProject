from sqlalchemy import Integer, String, Boolean
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy.orm import sessionmaker, DeclarativeBase
from sqlalchemy import ForeignKey
from ..database.database import Base


class Report(Base):
    report_id : Mapped[int] = mapped_column(Integer, primary_key= True)
    session_id : Mapped[int | None] = mapped_column(ForeignKey("GameSession.session_id"), nullable=True)
    detailed_report: Mapped[str] = mapped_column(String(200), nullable=False)
    recommendation: Mapped[str] = mapped_column(String(100), nullable=False)