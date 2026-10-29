from sqlalchemy import Integer, String, Boolean
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy.orm import sessionmaker, DeclarativeBase
from ..database.database import Base

class User(Base):
    __tablename__ = "User"

    user_id: Mapped[int] =mapped_column(Integer, primary_key= True)
    user_name: Mapped[str] = mapped_column(String(50), nullable=False)
    role: Mapped[str] = mapped_column(String(50), nullable=False)
    rank: Mapped[str] = mapped_column(String(50), nullable=False)