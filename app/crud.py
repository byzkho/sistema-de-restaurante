from sqlalchemy.orm import Session
from app import models, schemas


def crear_usuario(db: Session, usuario: schemas.UsuarioCreate):
    db_usuario = models.Usuario(**usuario.dict())
    db.add(db_usuario)
    db.commit()
    db.refresh(db_usuario)
    return db_usuario


def get_users(db: Session, skip, limit):
    users = db.query(models.Usuario).all()
    return users


def crear_mesa(db: Session, mesa: schemas.MesaBase):
    db_mesa = models.Mesa(**mesa.dict())
    db.add(db_mesa)
    db.commit()
    db.refresh(db_mesa)
    return db_mesa

def get_mesas(db: Session):
    return db.query(models.Mesa).all()
