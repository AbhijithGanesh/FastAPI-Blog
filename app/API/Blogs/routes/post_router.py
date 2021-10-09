from fastapi import APIRouter
from pathlib import Path
import os

posts = APIRouter()


@posts.get("/get-all-objects/")
def all_posts():
    return "Hello World"