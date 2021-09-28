from typing import Optional

from pydantic import BaseModel

class UserCreate(BaseModel):
  fullname: str
  email: str
  password: str

class UserUpdate(BaseModel):
  id: Optional[int]
  fullname: Optional[str]
  email: Optional[str]
  password: Optional[str]