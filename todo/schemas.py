from pydantic import BaseModel, Field


class TodoBase(BaseModel):
    title: str
    description: str
    priority: int
    completed: bool = Field(default=False)


class TodoCreate(TodoBase):
    pass


class Todo(TodoBase):
    id: int

    class Config:
        from_attributes = True
