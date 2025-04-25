from typing import List
from sqlalchemy import String, ForeignKey
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship

class Base(DeclarativeBase):
  pass

class User(Base):
  __tablename__ = "users"

  id: Mapped[int] = mapped_column(primary_key=True)
  name: Mapped[str] = mapped_column(String(32))
  password: Mapped[str] = mapped_column(String(96))
