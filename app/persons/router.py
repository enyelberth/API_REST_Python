from fastapi import APIRouter, HTTPException, status, Depends
from sqlalchemy.orm import Session
from app.models import Hola
from .schemas import UserCreate, UserResponse
from app.db import get_db
from app.persons.service import create_person
router = APIRouter()



@router.post("/", response_model=UserResponse, status_code=status.HTTP_201_CREATED)
def create_person(person: UserCreate):
    print("Creando persona...")
    try:
        create_person()
        # Lógica para crear una persona
        print("Persona creada exitosamente.")
    except Exception as e:
        print(f"Error al crear persona: {e}")