from fastapi import FastAPI
from fastapi.responses import PlainTextResponse
from Blogs.routes.post_router import posts

app = FastAPI()

app.include_router(posts, prefix="/posts")


