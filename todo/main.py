from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy.orm import Session
from starlette import status

from todo.database import get_db
from todo.models import Todo

from .crud import get_todo_by_id
from .database import Base, engine

# This only runs once when the databasea has not been created yet
Base.metadata.create_all(bind=engine)

app = FastAPI()


@app.get("/")
def reda_all_todos(db: Session = Depends(get_db)):
    return db.query(Todo).all()


@app.get("/{id}", status_code=status.HTTP_200_OK, )
def read_todo_by_id(user_id: int, db: Session = Depends(get_db)):
    db_todo = get_todo_by_id(user_id, db)
    if db_todo is None:
        raise HTTPException(status_code=404, detail="Todo not found")
    return db_todo