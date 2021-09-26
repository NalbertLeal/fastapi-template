from fastapi import APIRouter
from pydantic import BaseModel

from ..models import User

class UserBody(BaseModel):
  fullname: str
  email: str
  password: str

user_router = APIRouter(
  prefix="/user",
  tags=["user"],
  #dependencies=[Depends(get_token_header)],
  responses={404: {"description": "Not found"}},
)

@user_router.get("/")
async def user_get():
  return { 'name': 'Nalbert' }

@user_router.post("/")
async def user_create(userBody: UserBody):
  try:
    await User.find_by_email(email=userBody.email)
    return { 'error': 'User already exists' }
  except:
    new_user = await User.create(
      fullname=userBody.fullname,
      email=userBody.email,
      password=userBody.password
    )
    return new_user