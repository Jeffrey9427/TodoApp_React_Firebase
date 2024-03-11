from fastapi import FastAPI
from typing import Optional
from pydantic import BaseModel

app = FastAPI()

todos = {}


class Todos(BaseModel):
    id: Optional[int] = None
    title: Optional[str] = None
    completed: Optional[bool] = None


@app.get("/")
def index():
    return {"message": "Welcome to a todolist example of FastAPI!"}


# # Path parameter (decorator parameter + function parameter)
# @app.get("/todos/{todo_id}")
# def get_todo_by_id(
#     student_id: int = Path(..., description="The ID of the student you want to view.", gt=0)
# ):
#     # if student_id not in students:
#     #     return {"Error": f"Student ID {student_id} doesn't exist."}
#     return todos[student_id]


# Query parameters (solely function parameters)
@app.get("/todos")
def get_todos_by_title(title: str):
    for todo_id in todos:
        if todos[todo_id].title == title:
            return todos[todo_id]
    return {"Error": f"Todo name '{title}' not found."}

# Combining path and query


@app.get("/get-by-title-and-id")
def get_todos(*, todo_id: int, title: Optional[str] = None):
    for todo_id in todos:
        if todos[todo_id].title == title:
            return todos[todo_id]
    return {"Error": f"Todo name '{title}' not found."}

# Get todo by id


@app.get("/todos/get/{todo_id}")
def get_todo_by_id(todo_id: int):
    if todo_id not in todos:
        return {"Error": f"Todo ID {todo_id} not found."}
    return todos[todo_id]


# Post student (create new Student object in students list)
@app.post("/todos/post/{todo_id}")
def create_todo(todo_id: int, todo: Todos):
    if todo_id in todos:
        return {"Error": "Todo exists."}
    todos[todo] = todo
    return todos[todo_id]


# Update student
@app.put("/todos/put/{todo_id}")
def update_todo(todo_id: int, todo: Todos):
    if todo_id not in todos:
        return {"Error": f"Todo ID {todo_id} does not exist."}

    if todo.title != None:
        todos[todo_id].title = todo.title
    if todo.id != None:
        todos[todo_id].id = todo.id
    if todo.completed != None:
        todos[todo_id].completed = todo.completed

    return todos[todo_id]
