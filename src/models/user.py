from sqlalchemy import Column, String, Integer, DateTime
from sqlalchemy.sql import func

from ..config import Base
from .base_model import BaseModel

class User(Base, BaseModel):
  __tablename__ = 'users'
  __mapper_args__ = { "eager_defaults": True }

  id = Column(Integer, primary_key=True, autoincrement=True)
  fullname = Column(String)
  password = Column(String)
  created_at = Column(DateTime(timezone=True), server_default=func.now())
  updated_at = Column(DateTime(timezone=True), onupdate=func.now())

  def __repr__(self) -> str:
      return f'{self.id} {self.fullname} {self.password} {self.updated_at}, {self.created_at}'