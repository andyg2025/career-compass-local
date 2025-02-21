# main.py
"""This module provides user-related APIs for user creation and retrieval."""

import logging
from sqlalchemy.orm import Session
from sqlalchemy import func
from fastapi import FastAPI, Depends, HTTPException
import models
from database import engine, get_db
from schemas import QuerySchema
from utils import get_jobs

models.Base.metadata.create_all(engine)

logging.basicConfig(level=logging.INFO)

app = FastAPI()

@app.get("/python")
def get_index():
    return {"msg": "Python service"}

@app.post("/python")
def post_user(request: QuerySchema, db: Session = Depends(get_db)):

    jobs = get_jobs(request)

    for job in jobs:
        db.add(job)
        db.commit()
        db.refresh(job)

# @app.get("/user/{user_id}", response_model=UserSchema)
# def get_user_by_id(user_id: int, db: Session = Depends(get_db)):
#     user = db.query(models.User).filter(models.User.id == user_id).first()
#     if not user:
#         raise HTTPException(status_code=404, detail="User not found")
#     return user


# @app.put("/user/{user_id}", response_model=UserSchema)
# def user_update_from_order(
#     user_id: int, request: UserOrderUpdateSchema, db: Session = Depends(get_db)
# ):
#     user = db.query(models.User).filter(models.User.id == user_id).first()
#     if not user:
#         raise HTTPException(status_code=404, detail="User not found")
#     user.orders = func.array_append(user.orders, request.order_id)
#     db.commit()
#     db.refresh(user)
#     return user
