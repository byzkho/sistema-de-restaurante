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


@router.get("/users/", response_model=list[schemas.UsuarioBase])
def read_users(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    users = crud.get_users(db, skip=skip, limit=limit)
    return users


@router.post("/users/", response_model=schemas.UsuarioBase)
def create_user(user: schemas.UsuarioCreate, db: Session = Depends(get_db)):
    db_user = crud.get_user_by_name(db, name=user.name)
    if db_user:
        raise HTTPException(status_code=400, detail="El usuario ya existe")
    return crud.create_user(db=db, user=user)
