from sqlalchemy import Column, Integer, String, ForeignKey, DateTime, Float

from app.database import Base



class Usuario(Base):
    __tablename__ = "usuarios"

    id = Column(Integer, primary_key=True, index=True)
    nombre = Column(String, index=True)
    correo = Column(String, unique=True)
    contrasena = Column(String)
    rol = Column(String)  # 'Administrador', 'Recepción', 'Mesero', 'Cajero'


class Mesa(Base):
    __tablename__ = "mesas"
    id = Column(Integer, primary_key=True, index=True)
    numero_mesa = Column(Integer)
    estado = Column(String)  # 'Libre', 'Ocupada', 'Reservada'
    capacidad = Column(Integer)


class Reserva(Base):
    __tablename__ = "reservas"
    id = Column(Integer, primary_key=True, index=True)
    usuario_id = Column(Integer, ForeignKey("usuarios.id"))
    mesa_id = Column(Integer, ForeignKey("mesas.id"))
    hora_reserva = Column(DateTime)
    estado = Column(String)  # 'Pendiente', 'Completada', 'Cancelada'


class Factura(Base):
    __tablename__ = "facturas"
    id = Column(Integer, primary_key=True, index=True)
    usuario_id = Column(Integer, ForeignKey("usuarios.id"))
    mesa_id = Column(Integer, ForeignKey("mesas.id"))
    monto_total = Column(Float)
    fecha_factura = Column(DateTime)
