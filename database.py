from typing import List
from models import Gender, Role, User


db: List[User] = [
    User(id=154548,
        first_name="jam",
        last_name="Ahmed",
        gender= Gender.female,
        roles=[Role.user]
    ),
    User(id=385348,
        first_name="Alex",
        last_name="Jines",
        gender= Gender.male,
        roles=[Role.admin,Role.user]
    )
]