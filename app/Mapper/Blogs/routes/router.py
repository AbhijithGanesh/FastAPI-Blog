import os
from pathlib import Path
from starlette.routing import Route, Mount
from .post_router import posts



def routes():
    Routes = [
        Route("/posts/", posts)
    ]
    return Routes
