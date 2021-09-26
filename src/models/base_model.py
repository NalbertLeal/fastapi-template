from sqlalchemy import update as sqlalchemy_update
from sqlalchemy.future import select

from ..config import async_database_session

class BaseModel:
  @classmethod
  async def create(cls, **kwargs):
    new_obj = cls(**kwargs)
    async_database_session.add(new_obj)
    await async_database_session.commit()
    return new_obj

  @classmethod
  async def get(cls, id):
    query = select(cls).where(cls.id == id)
    results = await async_database_session.execute(query)
    (result,) = results.one()
    return result

  @classmethod
  async def update(cls, id, **kwargs):
    query = (
      sqlalchemy_update(cls)
        .where(cls.id == id)
        .values(**kwargs)
        .execution_options(synchronize_session=False)
    )
    await async_database_session.execute(query)
    await async_database_session.commit()
    return await cls.get(id)