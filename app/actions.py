from fastapi import APIRouter

from app.schemas import UserCreate, UserUpdate
from app.models import User

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
async def user_create(user_body: UserCreate):
  user = await User.find_by_email(email=user_body.email)
  if user:
    return { 'error': 'User already exists' }
  new_user = user_body.dict()
  new_user = { k: v for (k, v) in new_user.items() if v is not None }
  return await User.create(**new_user)

@user_router.put("/")
async def user_update(user_body: UserUpdate):
  user_dict = user_body.dict(exclude={'id'})
  user_dict = { k: v for (k, v) in user_dict.items() if v is not None }
  user = await User.update(user_body.id, **user_dict)
  if not user:
    return { 'error': 'User not updated' }
  return user