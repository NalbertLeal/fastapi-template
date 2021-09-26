from pydantic import BaseModel

class UserCreate(BaseModel):
  #id: int
  fullname: str
  email: str
  password: str