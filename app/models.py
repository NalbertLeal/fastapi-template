from sqlalchemy import Column, String, Integer, DateTime, update as sqlalchemy_update
from sqlalchemy.sql import func
from sqlalchemy.future import select

from app.db import Base, async_database_session

class BaseModel:
  @classmethod
  async def create(cls, **kwargs):
    try:
      new_obj = cls(**kwargs)
      async_database_session.add(new_obj)
      await async_database_session.commit()
      return new_obj
    except:
      return None

  @classmethod
  async def find_by_id(cls, id):
    try:
      query = select(cls).where(cls.id == id)
      results = await async_database_session.execute(query)
      (result,) = results.one()
      return result
    except:
      return None

  @classmethod
  async def update(cls, id, **kwargs):
    try:
      query = (
        sqlalchemy_update(cls)
          .where(cls.id == id)
          .values(**kwargs)
          .execution_options(synchronize_session=False)
      )
      await async_database_session.execute(query)
      await async_database_session.commit()
      return await cls.find_by_id(id)
    except:
      return None

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