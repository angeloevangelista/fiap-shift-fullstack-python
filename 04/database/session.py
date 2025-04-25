import os
import dotenv
from sqlalchemy import create_engine
from sqlalchemy.orm import Session

dotenv.load_dotenv()

def get_connection_string():
  # connection_string = (
  #   f"{os.getenv('DB_ENGINE')}://"
  #   f"{os.getenv('DB_USER')}:"
  #   f"{os.getenv('DB_PASS')}@"
  #   f"{os.getenv('DB_HOST')}:{os.getenv('DB_PORT')}/"
  #   f"{os.getenv('DB_NAME')}"
  # )

  connection_string = "postgresql://docker-user:docker-password@localhost:5432/todos"

  return connection_string

def get_session():
  engine = create_engine(
    get_connection_string(),
    echo=True,
  )

  return Session(engine)
