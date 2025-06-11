# main.py
from fastapi import FastAPI
from database import engine
import models

app = FastAPI()

# Tạo các bảng từ model
models.Base.metadata.create_all(bind=engine)

@app.get("/")
def read_root():
    return {"message": "Hello from FastAPI + XAMPP MySQL"}
