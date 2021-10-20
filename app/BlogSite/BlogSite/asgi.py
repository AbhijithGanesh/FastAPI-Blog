import os
from fastapi import FastAPI
from django.conf import settings
from fastapi.staticfiles import StaticFiles
from starlette.staticfiles import StaticFiles
from starlette.routing import Mount
from django.core.asgi import get_asgi_application
from pathlib import Path
from starlette.responses import FileResponse

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "BlogSite.settings")


from Logic.routers import get_posts, template_router


DESIGN_DIR = str(Path(__file__).resolve().parent.parent.parent) + str(
    Path(r"/design/static")
)

app = get_asgi_application()

if settings.MOUNT_DJANGO:
    routes: list = [
        Mount("/Master-Application", app),
        Mount("/static", StaticFiles(directory=DESIGN_DIR), name="static"),
    ]
    fastapi = FastAPI(routes=routes)

else:
    fastapi = FastAPI()


@fastapi.get("/favicon.ico")
def get_logo():
    path_to_file = (
        str(Path(__file__).resolve().parent.parent.parent.parent)
        + r"/app/design/logo/logo.svg"
    )
    return FileResponse(path_to_file)


fastapi.include_router(get_posts, prefix="/posts")
fastapi.include_router(template_router, prefix="/templates")
