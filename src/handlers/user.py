from fastapi import APIRouter

user_router = APIRouter(
  prefix="/user",
  tags=["user"],
  #dependencies=[Depends(get_token_header)],
  responses={404: {"description": "Not found"}},
)

@user_router.get("/")
async def user_get():
  return { 'name': 'Nalbert' }