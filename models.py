from enum import Enum
import random
from time import gmtime

from typing import Optional ,List
from pydantic import BaseModel


class Gender(str,Enum):
    male = "male"
    female = "female"

class Role(str,Enum):
    admin = "admin"
    user = "user"
    

class User(BaseModel):
    id: Optional[int] = random.randint(100000, 999900);
    first_name: str
    last_name: str
    middle_name: Optional[str]
    gender: Gender
    roles: Optional[List[Role]] = [Role.user]

