from fastapi import APIRouter, Request
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse
from pathlib import Path


TEMPLATES = (
    str(Path(__file__).resolve().parent.parent.parent.parent) + r"\design\templates"
)
templates_view = APIRouter()

templates = Jinja2Templates(directory=TEMPLATES)


@templates_view.get("/base_html")
def base_html(request: Request, response_class=HTMLResponse):
    return templates.TemplateResponse("index.html", {"request": request})
