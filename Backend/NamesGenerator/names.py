from typing import Optional ,List
from pydantic import BaseModel


class Name(BaseModel):
    first_name: str
    last_name: str


DataNames: List[Name] = [
    Name(first_name="jam",
        last_name="Ahmed"
    ),
    Name(first_name="Ty",
        last_name="Abbott",
    ),
    Name(first_name="Zack",
        last_name="Phillips"
    ),
    Name(first_name="Tyrese",
        last_name="Coleman",
    ),
    Name(first_name="Dylan ",
        last_name="Raymond"
    ),
    Name(first_name="Beth ",
        last_name="Casey",
    ),
    Name(first_name="Ava ",
        last_name="Barry"
    ),
    Name(first_name="Noelle",
        last_name="Pruitt"
    ),
    Name(first_name="Jenna ",
        last_name="Kaufman",
    ),
    Name(first_name="Cailyn",
        last_name="Cuevas"
    ),
    Name(first_name="Carley",
        last_name="Thalia",
    ),
    Name(first_name="Huynh",
        last_name="Keenan"
    ),
    Name(first_name="Justine",
        last_name="Ramirez",
    ),
    Name(first_name="Ari",
        last_name="Andrews"
    ),














]  