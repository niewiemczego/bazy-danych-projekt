from fastapi import Depends
from sqlalchemy.orm import Session

from todo import models, schemas
from todo.database import get_db


def get_all_todos(db: Session = Depends(get_db)) -> list[models.Todo]:
    return db.query(models.Todo).all()


def get_todo_by_id(todo_id: int, db: Session = Depends(get_db)) -> models.Todo | None:
    return db.query(models.Todo).filter(models.Todo.id == todo_id).first()


def get_todo_by_title(
    todo_title: str, db: Session = Depends(get_db)
) -> models.Todo | None:
    return db.query(models.Todo).filter(models.Todo.title == todo_title).first()


def create_todo(todo: schemas.TodoCreate, db: Session = Depends(get_db)) -> models.Todo:
    db_todo = models.Todo(**todo.model_dump())
    db.add(db_todo)
    db.commit()
    db.refresh(db_todo)
    return db_todo
