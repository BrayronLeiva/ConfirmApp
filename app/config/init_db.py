from app.config.database import Base, engine
from app.entities.user import User  # importa todos los modelos
from app.entities.session import Session
from app.entities.attendance import Attendance

# Crea las tablas en la base de datos
Base.metadata.drop_all(bind=engine)
Base.metadata.create_all(bind=engine)
