from fastapi import Depends
from sqlalchemy.orm import Session

from .database import get_db
from .schemas import Todo


def get_all_todos(db: Session = Depends(get_db)) -> list[Todo]:
    return db.query(Todo).all()


def get_todo_by_id(user_id: int, db: Session = Depends(get_db)) -> Todo | None:
    return db.query(Todo).filter(Todo.id == user_id).first()
