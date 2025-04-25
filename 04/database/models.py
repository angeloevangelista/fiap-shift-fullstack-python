from typing import List
from sqlalchemy import String, ForeignKey
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship

class Base(DeclarativeBase):
  pass

class User(Base):
  __tablename__ = "users"

  id: Mapped[int] = mapped_column(primary_key=True)
  name: Mapped[str] = mapped_column(String(16))
  email: Mapped[str] = mapped_column(String(42), nullable=True)

  todos: Mapped[List["Todo"]] = relationship(
    back_populates="user",
    cascade="all, delete-orphan",
  )

  def __str__(self):
    return f"id: {self.id}; name: {self.name}; email: {self.email};"


class Todo(Base):
  __tablename__ = "todos"

  id: Mapped[int] = mapped_column(primary_key=True)
  title: Mapped[str] = mapped_column(String(32))
  user_id: Mapped[int] = mapped_column(ForeignKey("users.id"))

  user: Mapped["User"] = relationship(back_populates="todos")
