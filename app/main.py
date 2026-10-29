from fastapi import FastAPI, Request, HTTPException, status, Depends
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi.middleware.cors import CORSMiddleware
from .schemas import *
import uvicorn
from .database.database import Base, engine, get_db
from .models.OrmModels import *
from sqlalchemy.orm import Session

app = FastAPI(title="КиберNET")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],
    allow_credentials=True,
    allow_headers=["*"],
    allow_methods=["*"]
)



Base.metadata.create_all(bind=engine)





@app.get("/")
async def main_page():
    return "This is main page of site!"

@app.post("/users/", response_model=User, status_code=status.HTTP_201_CREATED, tags=["users"])
def create_user(payload: UserCreate, db: Session = Depends(get_db)):
    obj = UserORM(**payload.model_dump())
    db.add(obj)
    db.commit()
    db.refresh(obj)
    return obj


@app.get("/users/", response_model=list[User], tags=["users"])
def list_users(db: Session = Depends(get_db)):
    return db.query(UserORM).all()


@app.get("/users/{user_id}", response_model=User, tags=["users"])
def get_user(user_id: int, db: Session = Depends(get_db)):
    obj = db.get(UserORM, user_id)
    if not obj:
        raise HTTPException(404, "User not found")
    return obj


@app.patch("/users/{user_id}", response_model=User, tags=["users"])
def update_user(user_id: int, payload: UserUpdate, db: Session = Depends(get_db)):
    obj = db.get(UserORM, user_id)
    if not obj:
        raise HTTPException(404, "User not found")
    for k, v in payload.model_dump(exclude_unset=True).items():
        setattr(obj, k, v)
    db.commit()
    db.refresh(obj)
    return obj


@app.delete("/users/{user_id}", status_code=status.HTTP_204_NO_CONTENT, tags=["users"])
def delete_user(user_id: int, db: Session = Depends(get_db)):
    obj = db.get(UserORM, user_id)
    if not obj:
        raise HTTPException(404, "User not found")
    db.delete(obj)
    db.commit()


# ============================================================
# 6. GameSession
# ============================================================

@app.post("/sessions/", response_model=GameSession, status_code=status.HTTP_201_CREATED, tags=["game-sessions"])
def create_session(payload: GameSessionCreate, db: Session = Depends(get_db)):
    obj = GameSessionORM(**payload.model_dump())
    db.add(obj)
    db.commit()
    db.refresh(obj)
    return obj


@app.get("/sessions/", response_model=list[GameSession], tags=["game-sessions"])
def list_sessions(user_id: Optional[int] = None, db: Session = Depends(get_db)):
    q = db.query(GameSessionORM)
    if user_id is not None:
        q = q.filter(GameSessionORM.user_id == user_id)
    return q.all()


@app.get("/sessions/{session_id}", response_model=GameSession, tags=["game-sessions"])
def get_session(session_id: int, db: Session = Depends(get_db)):
    obj = db.get(GameSessionORM, session_id)
    if not obj:
        raise HTTPException(404, "GameSession not found")
    return obj


@app.patch("/sessions/{session_id}", response_model=GameSession, tags=["game-sessions"])
def update_session(session_id: int, payload: GameSessionUpdate, db: Session = Depends(get_db)):
    obj = db.get(GameSessionORM, session_id)
    if not obj:
        raise HTTPException(404, "GameSession not found")
    for k, v in payload.model_dump(exclude_unset=True).items():
        setattr(obj, k, v)
    db.commit()
    db.refresh(obj)
    return obj


@app.delete("/sessions/{session_id}", status_code=status.HTTP_204_NO_CONTENT, tags=["game-sessions"])
def delete_session(session_id: int, db: Session = Depends(get_db)):
    obj = db.get(GameSessionORM, session_id)
    if not obj:
        raise HTTPException(404, "GameSession not found")
    db.delete(obj)
    db.commit()


# ============================================================
# 7. Notification
# ============================================================

@app.post("/notifications/", response_model=Notification, status_code=status.HTTP_201_CREATED, tags=["notifications"])
def create_notification(payload: NotificationCreate, db: Session = Depends(get_db)):
    obj = NotificationORM(**payload.model_dump())
    db.add(obj)
    db.commit()
    db.refresh(obj)
    return obj


@app.get("/notifications/", response_model=list[Notification], tags=["notifications"])
def list_notifications(session_id: Optional[int] = None, db: Session = Depends(get_db)):
    q = db.query(NotificationORM)
    if session_id is not None:
        q = q.filter(NotificationORM.session_id == session_id)
    return q.all()


@app.get("/notifications/{notification_id}", response_model=Notification, tags=["notifications"])
def get_notification(notification_id: int, db: Session = Depends(get_db)):
    obj = db.get(NotificationORM, notification_id)
    if not obj:
        raise HTTPException(404, "Notification not found")
    return obj


@app.patch("/notifications/{notification_id}", response_model=Notification, tags=["notifications"])
def update_notification(notification_id: int, payload: NotificationUpdate, db: Session = Depends(get_db)):
    obj = db.get(NotificationORM, notification_id)
    if not obj:
        raise HTTPException(404, "Notification not found")
    for k, v in payload.model_dump(exclude_unset=True).items():
        setattr(obj, k, v)
    db.commit()
    db.refresh(obj)
    return obj


@app.delete("/notifications/{notification_id}", status_code=status.HTTP_204_NO_CONTENT, tags=["notifications"])
def delete_notification(notification_id: int, db: Session = Depends(get_db)):
    obj = db.get(NotificationORM, notification_id)
    if not obj:
        raise HTTPException(404, "Notification not found")
    db.delete(obj)
    db.commit()


# ============================================================
# 8. Report
# ============================================================

@app.post("/reports/", response_model=Report, status_code=status.HTTP_201_CREATED, tags=["reports"])
def create_report(payload: ReportCreate, db: Session = Depends(get_db)):
    obj = ReportORM(**payload.model_dump())
    db.add(obj)
    db.commit()
    db.refresh(obj)
    return obj


@app.get("/reports/", response_model=list[Report], tags=["reports"])
def list_reports(session_id: Optional[int] = None, db: Session = Depends(get_db)):
    q = db.query(ReportORM)
    if session_id is not None:
        q = q.filter(ReportORM.session_id == session_id)
    return q.all()


@app.get("/reports/{report_id}", response_model=Report, tags=["reports"])
def get_report(report_id: int, db: Session = Depends(get_db)):
    obj = db.get(ReportORM, report_id)
    if not obj:
        raise HTTPException(404, "Report not found")
    return obj


@app.patch("/reports/{report_id}", response_model=Report, tags=["reports"])
def update_report(report_id: int, payload: ReportUpdate, db: Session = Depends(get_db)):
    obj = db.get(ReportORM, report_id)
    if not obj:
        raise HTTPException(404, "Report not found")
    for k, v in payload.model_dump(exclude_unset=True).items():
        setattr(obj, k, v)
    db.commit()
    db.refresh(obj)
    return obj


@app.delete("/reports/{report_id}", status_code=status.HTTP_204_NO_CONTENT, tags=["reports"])
def delete_report(report_id: int, db: Session = Depends(get_db)):
    obj = db.get(ReportORM, report_id)
    if not obj:
        raise HTTPException(404, "Report not found")
    db.delete(obj)
    db.commit()
