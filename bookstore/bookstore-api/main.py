import time
import dotenv
from typing import Annotated
from fastapi import FastAPI, Depends

from routers import auth, books

dotenv.load_dotenv()

app = FastAPI()

def get_message():
  return "Exemplo de mensagem injetada"

@app.get("/api/health")
def health_check(message: Annotated[dict, Depends(get_message)]):
  return {
    "healthy": True,
    "timestamp": time.asctime(),
    "message": message,
  }

app.include_router(auth.router)
app.include_router(books.router)
