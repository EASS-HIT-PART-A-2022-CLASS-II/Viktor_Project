from typing import List
from uuid import uuid4
from models import Gender, Role, User


db: List[User] = [
    User(id = "1b09ce2e-66b0-4278-8cbb-9132b40ff6e3",
        first_name="jam",
        last_name="Ahmed",
        gender= Gender.female,
        roles=[Role.user]
    ),
    User(id = "e18ac920-08d9-4c90-9c24-154eda4a48d6",
        first_name="Alex",
        last_name="Jines",
        gender= Gender.male,
        roles=[Role.admin,Role.user]
    )
]
