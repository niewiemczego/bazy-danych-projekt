from typing import List

from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy.orm import Session
from starlette import status

from todo import crud, models, schemas
from todo.database import get_db
from todo.schemas import TodoCreate

from .database import Base, engine

# This only runs once when the databasea has not been created yet
Base.metadata.create_all(bind=engine)

app = FastAPI()


@app.get("/")
def reda_all_todos(db: Session = Depends(get_db), response_model=List[schemas.Todo]):
    return db.query(models.Todo).all()


@app.get(
    "/{id}",
    status_code=status.HTTP_200_OK,
)
def read_todo_by_id(
    user_id: int, db: Session = Depends(get_db), response_model=schemas.Todo
):
    db_todo = crud.get_todo_by_id(user_id, db)
    if db_todo is None:
        raise HTTPException(status_code=404, detail="Todo not found")
    return db_todo


@app.get("/todo/{title}")
def read_todo_by_title(
    title: str, db: Session = Depends(get_db), response_model=schemas.Todo
):
    db_todo = crud.get_todo_by_title(title, db)
    if db_todo is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Todo not found"
        )
    return db_todo


@app.post("/")
def create_todo(
    todo: TodoCreate, db: Session = Depends(get_db), response_model=schemas.Todo
):
    db_todo = crud.get_todo_by_title(todo.title, db)
    if db_todo is not None:
        raise HTTPException(status_code=400, detail="Todo already created")
    return crud.create_todo(todo, db)
