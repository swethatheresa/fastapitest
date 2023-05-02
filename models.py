from uuid import UUID, uuid4
from pydantic import BaseModel
from enum import Enum

class Gender(str, Enum):
    male = "male"
    female = "female"

class Role(str, Enum):
    admin = "admin"
    user = "user"

class User(BaseModel):
    id: UUID | None = uuid4()
    first_name: str
    last_name: str
    gender: Gender
    roles: list[Role]

class UpdateUser(BaseModel):
    first_name: str | None = None
    last_name:str | None = None
    roles: list[Role] | None = None