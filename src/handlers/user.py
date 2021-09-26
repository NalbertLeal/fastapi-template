from fastapi import APIRouter

from src.models.requests_body.user_create import UserCreate
from src.models.requests_body.user_update import UserUpdate
from src.models.database import User

user_router = APIRouter(
  prefix="/user",
  tags=["user"],
  responses={404: {"description": "Not found"}},
)

@user_router.get("/by_id")
async def user_find_by_id(id: int):
  user = await User.find_by_id(id=id)
  if user:
    return user
  return { 'error': 'User not found' }

@user_router.get("/by_email")
async def user_find_by_email(email: str):
  user = await User.find_by_email(email=email)
  if user:
    return user
  return { 'error': 'User not found' }

@user_router.post("/")
async def user_create(userBody: UserCreate):
  user = await User.find_by_email(email=userBody.email)
  if user:
    return { 'error': 'User already exists' }
  return await User.create(
    fullname=userBody.fullname,
    email=userBody.email,
    password=userBody.password
  )

@user_router.put("/")
async def user_update(userBody: UserUpdate):
  user_dict = userBody.dict(exclude={'id'})
  user_dict = {k: v for (k, v) in user_dict.items() if v is not None}
  user = await User.update(userBody.id, **user_dict)
  if not user:
    return user
  return { 'error': 'User not updated' }