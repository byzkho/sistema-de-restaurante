from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app import schemas, crud
from app.database import SessionLocal

router = APIRouter()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.get("/mesas/", response_model=list[schemas.MesaBase])
def read_mesas(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    mesas = crud.get_mesas(db, skip=skip, limit=limit)
    return mesas


@router.post("/mesas/reservar/", response_model=schemas.MesaBase)
def reservar_mesa(mesa: schemas.ReservaBase, db: Session = Depends(get_db)):
    db_mesa = crud.get_mesa_by_id(db, id=mesa.id)
    if not db_mesa:
        raise HTTPException(status_code=404, detail="Mesa no encontrada")
    if db_mesa.estado == "reservada":
        raise HTTPException(status_code=400, detail="La mesa ya está reservada")
    return crud.reservar_mesa(db=db, mesa=mesa)
