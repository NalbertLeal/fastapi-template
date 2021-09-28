from fastapi import FastAPI

from app.db import async_database_session
from app.actions import user_router

app = FastAPI()

app.include_router(user_router)

@app.on_event('startup')
async def startup_event():
  await async_database_session.init()
  await async_database_session.create_all()