import os
from fastapi import FastAPI
from django.conf import settings
from fastapi.staticfiles import StaticFiles
from starlette.staticfiles import StaticFiles
from starlette.routing import Mount
from django.core.asgi import get_asgi_application
from pathlib import Path

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'BlogSite.settings')


from Logic.routers import get_posts



DESIGN_DIR = str(Path(__file__).resolve().parent.parent.parent) + "\design\static"
app = get_asgi_application()

if settings.MOUNT_DJANGO:
    routes: list = [
        Mount("/Master-Application", app),
        Mount("/static", StaticFiles(directory = DESIGN_DIR), name = "static")
    ]
    fastapi = FastAPI(routes = routes)

else:  
    fastapi = FastAPI()

fastapi.include_router(get_posts, prefix = "/posts")
