from sqlalchemy import update

from database.session import get_session
from database.models import User

def list_users():
  users = []

  with get_session() as session:
    users = session.query(User).all()

  return users

def create_user(user: User):
  with get_session() as session:
    session.add(user)
    session.commit()
    session.refresh(user)

  return user

def delete_user(user: User):
  with get_session() as session:
    session.delete(user)
    session.commit()

def get_user(user_id: int):
  found_user = None

  with get_session() as session:
    found_user = session.get(User, user_id)
    # found_user = session.query(User).where(User.id == user_id).one()

  return found_user

def update_user(user_to_update: User):
  with get_session() as session:
    updated_user = session.get(User, user_to_update.id)

    update_statement = update(User).values({
      User.name: user_to_update.name,
      User.email: user_to_update.email
    }).where(User.id == updated_user.id)

    update_result = session.execute(update_statement)
    session.commit()
    session.refresh(updated_user)

    if update_result.rowcount != 1:
      raise RuntimeError("Falha ao atualizar o usuário")

  return updated_user

updated_user = update_user(User(
  id=12,
  name="Andre",
  email="andre@email.com",
))

print(updated_user)
