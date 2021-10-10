from logging import debug
import os
from fastapi import FastAPI
import uvicorn
from django.conf import settings
from fastapi.staticfiles import StaticFiles
from starlette.staticfiles import StaticFiles
from starlette.routing import Mount
from django.core.asgi import get_asgi_application
from pathlib import Path

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'BlogSite.settings')


from logic.routes import posts_fetcher


DESIGN_DIR = Path(__file__).resolve().parent.parent / "design/static"
app = get_asgi_application()

if settings.MOUNT_DJANGO:
    routes: list = [
        Mount("/Master-Application", app),
        Mount("/static", StaticFiles(directory = DESIGN_DIR), name = "static")
    ]
    fastapi = FastAPI(routes = routes)

else:  
    fastapi = FastAPI()

fastapi.include_router(posts_fetcher, prefix = "/posts")

