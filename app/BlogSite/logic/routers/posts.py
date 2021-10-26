from datetime import datetime
from typing import Text
from fastapi import APIRouter
from pydantic import BaseModel, AnyHttpUrl
from fastapi.responses import HTMLResponse
import pytz

posts_fetcher = APIRouter()
India = pytz.timezone("Asia/Calcutta")


class Blog(BaseModel):
    id: int
    Title: str
    Identifier: Text
    SubTitle: str
    Date_of_creation: datetime
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
        html = """
        <html>
            <head>
                <title>HTTP Response</title>
            </head>
        <body>
            <h1>Saved successfully</h1>
        </body>
        </html>
        """
        val.save()
        return HTMLResponse(content=html, status_code=200)
