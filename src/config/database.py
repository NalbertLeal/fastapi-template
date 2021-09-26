from typing import Any

from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.orm import declarative_base, sessionmaker

Base = declarative_base()

class AsyncDatabaseSession:
  def __init__(self, user: str, password: str, db_name: str):
    self._engine = None
    self._session = None
    self.conn_str = f'postgresql+asyncpg://{user}:{password}@127.0.0.1:5432/{db_name}'

  def __getattr__(self, name: str) -> Any:
    return getattr(self._session, name)

  async def init(self):
    self._engine = create_async_engine(self.conn_str)
    self._session = sessionmaker(bind=self._engine, expire_on_commit=False, class_=AsyncSession)()

  async def create_all(self):
    async with self._engine.begin() as conn:
      await conn.run_sync(Base.metadata.create_all)

async_database_session = AsyncDatabaseSession('postgres', 'admin', 'tutorial_sqlalchemy')