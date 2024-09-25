from pydantic import BaseModel
from datetime import datetime


class UsuarioBase(BaseModel):
    nombre: str
    correo: str
    rol: str


class UsuarioCreate(UsuarioBase):
    contrasena: str


class MesaBase(BaseModel):
    numero_mesa: int
    estado: str
    capacidad: int


class ReservaBase(BaseModel):
    usuario_id: int
    mesa_id: int
    hora_reserva: datetime


class FacturaBase(BaseModel):
    usuario_id: int
    mesa_id: int
    monto_total: float
