from enum import Enum
from typing import Optional ,List
from pydantic import BaseModel
from uuid import UUID


class Gender(str,Enum):
    male = "male"
    female = "female"

class Role(str,Enum):
    admin = "admin"
    user = "user"
    

class User(BaseModel):
    id: Optional[UUID]
    first_name: Optional[str] 
    last_name: Optional[str]  
    gender: Optional[Gender]
    roles: Optional[List[Role]] = [Role.user]
    password: Optional[str] 



