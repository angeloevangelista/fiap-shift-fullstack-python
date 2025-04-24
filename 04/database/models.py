import json
from sqlalchemy import String
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column

class Base(DeclarativeBase):
  pass

class User(Base):
  __tablename__ = "users"

  id: Mapped[int] = mapped_column(primary_key=True)
  name: Mapped[str] = mapped_column(String(16))
  email: Mapped[str] = mapped_column(String(42), nullable=True)

  def __str__(self):
    return f"id: {self.id}; name: {self.name}; email: {self.email};"
