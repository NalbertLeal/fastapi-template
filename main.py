'''import asyncio'''
from fastapi import FastAPI

from src.config import async_database_session
from src.handlers.user import user_router

app = FastAPI()

app.include_router(user_router)

@app.on_event('startup')
async def startup_event():
  await async_database_session.init()
  await async_database_session.create_all()

'''
from src.models import User

async def init_app():
  await async_database_session.init()
  await async_database_session.create_all()

async def async_main():
  await init_app()
  user = await User.create(fullname='Nalbert', password='123456')
  print(user)
  user = await User.update(1, fullname='Nalbert Gabriel')
  print(user)

asyncio.run(async_main())
'''