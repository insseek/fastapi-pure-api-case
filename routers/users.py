from typing import Union

from fastapi import FastAPI, APIRouter
from pydantic import BaseModel

router = APIRouter(prefix="/users", tags=["users"])


class User(BaseModel):
    name: str
    age: int
    is_resigned: Union[bool, None] = None


@router.get("/")
def read_users(q: Union[str, None] = None):
    return {"users": [{"name": "name1"}, {"name": "name2"}], "q": q}


@router.get("/{user_id}")
def read_user(user_id: int, q: Union[str, None] = None):
    return {"user_id": user_id, "q": q}


@router.put("/users/{user_id}")
def update_user(user_id: int, user: User):
    return {"use_name": user.name, "user_id": user_id}
