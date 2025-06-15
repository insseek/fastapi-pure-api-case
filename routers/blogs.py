from fastapi import APIRouter
from typing import Union

router = APIRouter(prefix="/blogs", tags=["blogs"])


@router.get("/")
def read_blogs(q: Union[str, None] = None):
    return {"blogs": [{"title": "title1"}, {"title": "title2"}], "q": q}


@router.get("/{blog_id}")
def read_blog(blog_id: int):
    return {"blog_id": blog_id, "title": "title{blog_id}".format_map({"blog_id": blog_id})}
