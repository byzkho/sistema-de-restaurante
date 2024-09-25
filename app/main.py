from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from fastapi import Request
from routers import users, mesas
from app.database import engine, Base

Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(users.router, prefix="/api")
app.include_router(mesas.router, prefix="/api")

# Configuración para archivos estáticos
app.mount("/static", StaticFiles(directory="static"), name="static")

# Configuración para Jinja2
templates = Jinja2Templates(directory="templates")

@app.get("/listado-mesas", response_class=HTMLResponse)
async def listado_mesas(request: Request):
    return templates.TemplateResponse("listado_mesas.html", {"request": request})

@app.get("/", response_class=HTMLResponse)
async def read_root(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})


