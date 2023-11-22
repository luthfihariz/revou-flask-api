from dataclasses import dataclass

@dataclass
class UserDomain:
    id: int
    email: str
    password: str
    username: str    