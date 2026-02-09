from fastapi import APIRouter, HTTPException, status, Depends
from sqlalchemy.orm import Session
from app.models import Hola
from .schemas import UserCreate, UserResponse
# Asegúrate de importar get_db desde tu archivo de configuración de base de datos
from app.db import get_db 

router = APIRouter()

@router.post("/", response_model=UserResponse, status_code=status.HTTP_201_CREATED)
def crear_usuario(user: UserCreate, db: Session = Depends(get_db)):
    # 1. Verificar si el usuario ya existe en la DB real
    usuario_existente = db.query(Hola).filter(Hola.username == user.username).first()
    if usuario_existente:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=f"El usuario {user.username} ya está registrado."
        )
    
    # 2. Crear instancia del modelo e insertar
    nuevo_usuario = Hola(**user.model_dump())
    db.add(nuevo_usuario)
    db.commit()      # Guarda los cambios
    db.refresh(nuevo_usuario)  # Trae el ID generado
    return nuevo_usuario

@router.get("/{user_id}", response_model=UserResponse)
def get_user(user_id: int, db: Session = Depends(get_db)):
    # Buscamos el registro por ID
    usuario = db.query(Hola).filter(Hola.id == user_id).first()
    
    if not usuario:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Usuario no encontrado"
        )
    return usuario

@router.get("/debug/all")
def test_connection(db: Session = Depends(get_db)):
    # Esto soluciona tu error de Session.query(Hola).all()
    try:
        return db.query(Hola).all()
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))