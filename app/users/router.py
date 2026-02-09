from fastapi import APIRouter, HTTPException, status, Depends
from sqlalchemy.orm import Session
from app.models import Hola
from .schemas import UserCreate, UserResponse
# Importa get_db desde donde lo tengas definido (ej: app.database)
from app.db import get_db 

router = APIRouter()

@router.post("/", response_model=UserResponse, status_code=status.HTTP_201_CREATED)
def crear_usuario(user: UserCreate, db: Session = Depends(get_db)):
    # 1. Buscamos en la base de datos real
    usuario_existente = db.query(Hola).filter(Hola.username == user.username).first()
    
    if usuario_existente:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=f"El usuario {user.username} ya está registrado."
        )
    
    # 2. Creamos la instancia del modelo
    nuevo_usuario = Hola(**user.model_dump())
    
    # 3. Guardamos en la DB
    db.add(nuevo_usuario)
    db.commit()
    db.refresh(nuevo_usuario)
    return nuevo_usuario

@router.get("/{user_id}", response_model=UserResponse)
def get_user(user_id: int, db: Session = Depends(get_db)):
    # Buscamos por ID
    usuario = db.query(Hola).filter(Hola.id == user_id).first()
    
    if not usuario:
        raise HTTPException(
            status_code=404,
            detail="Usuario no encontrado"
        )
    return usuario

@router.get("/all/test")
def get_all_test(db: Session = Depends(get_db)):
    # Esto corregirá tu error de Session.query(Hola).all()
    return db.query(Hola).all()