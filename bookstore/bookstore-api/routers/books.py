from pydantic import BaseModel
from fastapi import APIRouter, HTTPException
from sqlalchemy import update

from database.models import Book
from dependencies import DbSessionDependency, LoggedUserDependency

router = APIRouter()

class BookRequest(BaseModel):
  titulo: str
  resumo: str
  ano: int
  paginas: int
  isbn: int

class BookResponse(BookRequest):
  id: int

@router.post("/livros", status_code=201)
def create_book(
  book_request: BookRequest,
  db_session: DbSessionDependency,
  _: LoggedUserDependency,
):
  existing_book = db_session.query(Book).where(
    Book.title == book_request.titulo,
  ).one_or_none()

  if existing_book != None:
    raise HTTPException(400, "O livro informado já existe")

  created_book = Book(
    title=book_request.titulo,
    summary=book_request.resumo,
    year=book_request.ano,
    pages=book_request.paginas,
    isbn=str(book_request.isbn),
  )

  db_session.add(created_book)
  db_session.commit()
  db_session.refresh(created_book)

  return created_book

@router.get("/livros/{book_id}", response_model=BookResponse)
def get_book(book_id: int, db_session: DbSessionDependency, _: LoggedUserDependency):
  found_book = db_session.get(Book, book_id)

  if found_book == None:
    raise HTTPException(404, "O livro informado não existe")

  return BookResponse(
    id=found_book.id,
    titulo=found_book.title,
    resumo=found_book.summary,
    ano=found_book.year,
    paginas=found_book.pages,
    isbn=int(found_book.isbn),
  )

@router.get("/livros")
def list_books(db_session: DbSessionDependency, _: LoggedUserDependency,):
  books = db_session.query(Book).all()

  books_response = []

  for book in books:
    books_response.append(
      BookResponse(
        id=book.id,
        titulo=book.title,
        resumo=book.summary,
        ano=book.year,
        paginas=book.pages,
        isbn=int(book.isbn),
      )
    )

  return books

@router.delete("/livros/{book_id}", status_code=204)
def delete_book(book_id: int, db_session: DbSessionDependency, _: LoggedUserDependency):
  found_book = db_session.get(Book, book_id)

  if found_book == None:
    raise HTTPException(404, "O livro informado não existe")

  db_session.delete(found_book)
  db_session.commit()

@router.put("/livros/{book_id}", response_model=BookResponse)
def update_book(
  book_id: int,
  book_request: BookRequest,
  db_session: DbSessionDependency,
  _: LoggedUserDependency,
):
  found_book = db_session.get(Book, book_id)

  if found_book == None:
    raise HTTPException(404, "O livro informado não existe")

  update_statement = update(Book).values({
    Book.title: book_request.titulo,
    Book.summary: book_request.resumo,
    Book.year: book_request.ano,
    Book.pages: book_request.paginas,
    Book.isbn: str(book_request.isbn)
  }).where(
    Book.id == book_id
  )

  update_result = db_session.execute(update_statement)
  db_session.commit()
  db_session.refresh(found_book)

  if update_result.rowcount != 1:
    raise HTTPException(400, "Não foi possível atualizar o livro informado")

  return BookResponse(
    id=found_book.id,
    titulo=found_book.title,
    resumo=found_book.summary,
    ano=found_book.year,
    paginas=found_book.pages,
    isbn=int(found_book.isbn),
  )
