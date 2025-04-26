import os
import jwt
from jwt.exceptions import ExpiredSignatureError, InvalidAlgorithmError, InvalidSignatureError
from typing import Annotated
from fastapi import Depends, Header, HTTPException
from sqlalchemy.orm import Session

from database.models import User
from database.session import get_session

def get_logged_user(authorization: Annotated[str, Header()] = ""):
  try:
    auth_token = authorization.removeprefix("Bearer ")

    if auth_token == "":
      raise HTTPException(401, "Nenhum token foi informado")

    if len(auth_token.split(".")) != 3:
      raise HTTPException(401, "O token informado é inválido")

    token_payload = jwt.decode(
      auth_token,
      os.getenv("AUTH_SECRET"),
      algorithms=["HS256"],
    )
  except ExpiredSignatureError:
    raise HTTPException(401, "O token informado está expirado")
  except InvalidAlgorithmError:
    raise HTTPException(401, "O token informado é inválido")
  except InvalidSignatureError:
    raise HTTPException(401, "O token informado está alterado")

  logged_user = User(
    id=token_payload["user_id"],
    name=token_payload["user_name"],
  )

  return logged_user

DbSessionDependency = Annotated[Session, Depends(get_session)]
LoggedUserDependency = Annotated[User, Depends(get_logged_user)]
