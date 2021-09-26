from sqlalchemy import Column, String, Integer, DateTime
from sqlalchemy.sql import func
from sqlalchemy.future import select

from src.config import Base, async_database_session
from .base_model import BaseModel

class User(Base, BaseModel):
  __tablename__ = 'users'
  __mapper_args__ = { "eager_defaults": True }

  id = Column(Integer, primary_key=True, autoincrement=True)
  fullname = Column(String, nullable=False)
  email = Column(String, nullable=False)
  password = Column(String, nullable=False)
  created_at = Column(DateTime(timezone=True), server_default=func.now())
  updated_at = Column(DateTime(timezone=True), onupdate=func.now())

  @classmethod
  async def find_by_email(cls, email: str):
    try:
      query = select(cls).where(cls.email == email)
      results = await async_database_session.execute(query)
      (result,) = results.one()
      return result
    except:
      return None


  def __repr__(self) -> str:
      return f'{self.id} {self.fullname} {self.password} {self.updated_at}, {self.created_at}'