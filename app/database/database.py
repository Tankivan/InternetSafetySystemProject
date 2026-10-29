from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import DeclarativeBase
class Base(DeclarativeBase):
    pass

SQLALCHEMY_DATABASE_URL = "sqlite:///.information_safety_db.db"

engine = create_engine(
    url=SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread":False}
)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
