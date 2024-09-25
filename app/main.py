import fastapi

from app.database import engine, Base
from routers import users, mesa

Base.metadata.create_all(bind=engine)

app = fastapi.FastAPI()
app.include_router(users.router, prefix="/api")
app.include_router(mesa.router, prefix="/api")


@app.get("/")
def read_root():
    return {"message": "Sistema de Restaurante"}
