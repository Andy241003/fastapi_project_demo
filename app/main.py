from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from .database import SessionLocal, engine, Base
from .crud import get_users, create_user

Base.metadata.create_all(bind=engine)

app = FastAPI()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get("/users")
def read_users(db: Session = Depends(get_db)):
    return get_users(db)

@app.post("/users")
def add_user(name: str, email: str, db: Session = Depends(get_db)):
    return create_user(db, name, email)
