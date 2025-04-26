from typing import List
from sqlalchemy import String, Text, Integer
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship

class Base(DeclarativeBase):
  pass

class User(Base):
  __tablename__ = "users"

  id: Mapped[int] = mapped_column(primary_key=True)
  name: Mapped[str] = mapped_column(String(32))
  password: Mapped[str] = mapped_column(String(96))

class Book(Base):
  __tablename__ = "books"

  id: Mapped[int] = mapped_column(primary_key=True)
  title: Mapped[str] = mapped_column(String(255))
  summary: Mapped[str] = mapped_column(Text())
  year: Mapped[int] = mapped_column(Integer())
  pages: Mapped[int] = mapped_column(Integer())
  isbn: Mapped[str] = mapped_column(String(13))

  def __str__(self):
    return (
      f"id: {self.id}; "
      f"title: {self.title}; "
      f"summary: {self.summary}; "
      f"year: {self.year}; "
      f"pages: {self.pages}; "
      f"isbn: {self.isbn};"
    )
