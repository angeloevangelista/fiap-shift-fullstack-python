import os
from datetime import datetime, timezone, timedelta

import jwt
import bcrypt
from pydantic import BaseModel
from fastapi import APIRouter, HTTPException

from database.models import User
from dependencies import DbSessionDependency

router = APIRouter()

class UserRequest(BaseModel):
  username: str
  password: str

@router.post("/cadastro", status_code=201)
def create_user(
  user_request: UserRequest,
  db_session: DbSessionDependency,
):
  existing_user = db_session.query(User).where(
    User.name == user_request.username,
  ).one_or_none()

  if existing_user != None:
    raise HTTPException(400, detail="Um usuário com o mesmo nome já existe")

  hashed_password = bcrypt.hashpw(
    bytes(user_request.password, encoding="utf-8"),
    bcrypt.gensalt(rounds=8),
  ).decode("utf-8")

  created_user = User(
    name=user_request.username,
    password=hashed_password,
  )

  db_session.add(created_user)
  db_session.commit()
  db_session.refresh(created_user)

  del(created_user.password)

  return created_user

@router.post("/", status_code=201)
def create_session(
  user_request: UserRequest,
  db_session: DbSessionDependency,
):
  found_user = db_session.query(User).where(
    User.name == user_request.username,
  ).one_or_none()

  if found_user is None:
    raise HTTPException(401, "A combinação usuário e senha não coincidem")

  passwords_match = bcrypt.checkpw(
    bytes(user_request.password, encoding="utf-8"),
    bytes(found_user.password, encoding="utf-8"),
  )

  if not passwords_match:
    raise HTTPException(401, "A combinação usuário e senha não coincidem")

  jwt_token = jwt.encode(
    {
      "iat": datetime.now(tz=timezone.utc),
      "exp": datetime.now(tz=timezone.utc) + timedelta(minutes=15),
      "user_id": found_user.id,
      "user_name": found_user.name,
    },
    os.getenv("AUTH_SECRET"),
    algorithm="HS256",
  )

  del(found_user.password)

  return {
    "token": jwt_token,
    "user": found_user,
    "tokenRenovado": None,
  }
