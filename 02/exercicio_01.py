from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import uuid

id = uuid.uuid4()

app = FastAPI()

class Todo(BaseModel):
  id: int = None
  summary: str
  description: str
  completed: bool

tasks_db = []

@app.get("/tasks")
def list_tasks(summary: str = ""):
  
  print("summary: " + summary)

  if summary != "":
    return [ task for task in tasks_db if summary in task.summary ]

  return tasks_db

@app.post("/tasks", status_code=201)
def create_task(task: Todo):
  task.id = str(uuid.uuid4())
  tasks_db.append(task)
  return task
