import os
import time
import dotenv
from typing import Annotated
from fastapi import FastAPI, Depends
from fastapi.middleware.cors import CORSMiddleware

from routers import auth, books, authors

dotenv.load_dotenv()

app = FastAPI()

app.add_middleware(
  CORSMiddleware,
  allow_origins=os.getenv("ALLOWED_ORIGINS", "").split(","),
  allow_methods=["DELETE", "GET", "POST", "PUT", "OPTIONS"],
  allow_headers=["*"],
)

# @app.middleware("http")
# async def my_middleware(request: Request, call_next):
#   response = await call_next(request)
#   response.headers["Access-Control-Allow-Origin"] = "http://localhost:5173"
#   return response

def sum_numbers(numbers):
  result = 0

  for number in numbers:
    result += number

  return result

def get_message():
  return "Hello, World"

@app.get("/api/health")
def health_check(message: Annotated[str, Depends(get_message)]):
  return {
    "healthy": True,
    "timestamp": time.asctime(),
    "message": message,
  }

app.include_router(auth.router)
app.include_router(books.router)
app.include_router(authors.router)
