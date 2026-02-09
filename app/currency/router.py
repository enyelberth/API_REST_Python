from fastapi import APIRouter, HTTPException, status, Depends
from sqlalchemy.orm import Session
from app.models import Hola
from .schemas import CurrencyResponse, CurrencyCreate
from app.db import get_db
from app.currency.services import create_currency
router = APIRouter()



@router.post("/", response_model=CurrencyResponse, status_code=status.HTTP_201_CREATED)
async def create_currency(currency: CurrencyCreate):
    print("Creando moneda...")
    try:
        print(currency)
        result = await create_currency(currency)
        # Lógica para crear una moneda
        print("Moneda creada exitosamente.")
        return result
    except Exception as e:
        print(f"Error al crear moneda: {e}")