from fastapi import FastAPI
from fastapi.responses import PlainTextResponse
from routes.router import routes

app = FastAPI(routes=routes())


@app.get("/hello")
def HelloWorld():
    return PlainTextResponse("Hello World")
