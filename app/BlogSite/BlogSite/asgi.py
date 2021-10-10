import os
from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles

from django.core.asgi import get_asgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'BlogSite.settings')


from logic.routes import posts_fetcher

fastapi = FastAPI()
fastapi.include_router(posts_fetcher, prefix = "/posts")

app = get_asgi_application()
