from pydantic import BaseModel

class UserCreate(BaseModel):
  fullname: str
  email: str
  password: str