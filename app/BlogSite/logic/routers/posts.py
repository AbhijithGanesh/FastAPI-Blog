from typing import Text
from fastapi import APIRouter
from pydantic import BaseModel, AnyHttpUrl
import uuid
from datetime import date

posts_fetcher = APIRouter()

class Blog(BaseModel):
    id: int
    Title: str
    Identifier: Text
    SubTitle: str
    # Date_of_creation: date
    Content: str
    URL: AnyHttpUrl

@posts_fetcher.get("/get-all-objects/")
def get_all_obj():
    from Logic.models import BlogTable

    objs: list = BlogTable.objects.all()
    return objs


@posts_fetcher.get("/{post_id}")
def query_posts(post_id: str):
    from Logic.models import BlogTable
    query = BlogTable.objects.get(id=post_id)
    return [query]


@posts_fetcher.post("/post/{Title}")
def post_obj(Title: str, item: Blog):
    from Logic.models import BlogTable
    val = BlogTable(**dict(item))
    if val:
        val.save()