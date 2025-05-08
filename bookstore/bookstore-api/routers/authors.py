from typing import List
from pydantic import BaseModel
from fastapi import APIRouter, HTTPException
from sqlalchemy import update

from database.models import Author
from dependencies import DbSessionDependency, LoggedUserDependency

router = APIRouter()

class AuthorRequest(BaseModel):
  nome: str
  email: str
  telefone: str
  bio: str

class AuthorResponse(AuthorRequest):
  id: int

@router.post("/autores", status_code=201)
def create_author(
  author_request: AuthorRequest,
  db_session: DbSessionDependency,
  _: LoggedUserDependency,
):
  author = Author(
    name=author_request.nome,
    email=author_request.email,
    cellphone=author_request.telefone,
    bio=author_request.bio,
  )

  db_session.add(author)
  db_session.commit()
  db_session.refresh(author)

  return author

@router.get("/autores/{author_id}", response_model=AuthorResponse)
def get_author(
  author_id: int,
  db_session: DbSessionDependency,
  _: LoggedUserDependency,
):
  found_author = db_session.get(Author, author_id)

  if found_author == None:
    raise HTTPException(404, "O autor informado não existe")

  return AuthorResponse(
    id=found_author.id,
    nome=found_author.name,
    email=found_author.email,
    telefone=found_author.cellphone,
    bio=found_author.bio,
  )

@router.get("/autores", response_model=List[AuthorResponse])
def list_authors(
  db_session: DbSessionDependency,
  _: LoggedUserDependency,
):
  authors = []

  found_authors = db_session.query(Author).all()

  for author in found_authors:
    authors.append(AuthorResponse(
      id=author.id,
      nome=author.name,
      email=author.email,
      telefone=author.cellphone,
      bio=author.bio,
    ))

  return authors

@router.delete("/autores/{author_id}", status_code=204)
def delete_author(
  author_id: int,
  db_session: DbSessionDependency,
  _: LoggedUserDependency,
):
  found_author = db_session.get(Author, author_id)

  if found_author == None:
    raise HTTPException(404, "O autor informado não existe")

  db_session.delete(found_author)
  db_session.commit()

@router.put("/autores/{author_id}")
def update_author(
  author_id: int,
  author_request: AuthorRequest,
  db_session: DbSessionDependency,
  _: LoggedUserDependency,
):
  found_author = db_session.get(Author, author_id)

  if found_author == None:
    raise HTTPException(404, "O autor informado não existe")

  update_statement = update(Author).values({
    Author.name: author_request.nome,
    Author.email: author_request.email,
    Author.cellphone: author_request.telefone,
    Author.bio: author_request.bio,
  }).where(Author.id == author_id)

  update_result = db_session.execute(update_statement)
  db_session.commit()
  db_session.refresh(found_author)

  if update_result.rowcount != 1:
    raise HTTPException(400, "Um erro ocorreu durante a atualização do autor")

  return found_author
