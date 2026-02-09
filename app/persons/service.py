from fastapi import APIRouter, HTTPException, status, Depends
from sqlalchemy.orm import Session
from app.models import Hola
from .schemas import UserCreate, UserResponse
from app.db import get_db

def create_person(person: UserCreate, db: Session = Depends(get_db)):
    print("Creando persona...")
    try:

        # Lógica para crear una persona
        print("Persona creada exitosamente.")
    except Exception as e:
        print(f"Error al crear persona: {e}")


def get_persons():
    print("Obteniendo personas...")
    try:
        # Lógica para obtener personas
        print("Personas obtenidas exitosamente.")
    except Exception as e:
        print(f"Error al obtener personas: {e}")

def get_person(person_id: int):
    print("Obteniendo una persona...")
    try:
        # Lógica para obtener una persona
        print("Persona obtenida exitosamente.")
    except Exception as e:
        print(f"Error al obtener persona: {e}")