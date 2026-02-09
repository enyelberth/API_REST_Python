from fastapi import APIRouter, HTTPException, status, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
# Importamos el modelo correcto
from app.currency.models import Currency 
from .schemas import CurrencyCreate, CurrencyResponse
from app.db import get_db 

router = APIRouter()

# 1. Crear moneda (POST)
@router.post("/", response_model=CurrencyResponse, status_code=status.HTTP_201_CREATED)
async def create_currency(currency: CurrencyCreate, db: AsyncSession = Depends(get_db)):
    # Verificamos si ya existe usando select
    query = select(Currency).where(Currency.name == currency.name)
    result = await db.execute(query)
    currency_existente = result.scalars().first()
    
    if currency_existente:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=f"La moneda {currency.name} ya está registrada."
        )
    
    nueva_moneda = Currency(**currency.model_dump())
    
    db.add(nueva_moneda)
    await db.commit()      
    await db.refresh(nueva_moneda) 
    return nueva_moneda

# 2. Obtener moneda por ID (GET)
@router.get("/{currency_id}", response_model=CurrencyResponse)
async def get_currency(currency_id: int, db: AsyncSession = Depends(get_db)):
    # En async, siempre usamos select
    query = select(Currency).where(Currency.id == currency_id)
    result = await db.execute(query)
    currency = result.scalars().first()
    
    if not currency:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Moneda no encontrada"
        )
    return currency

# 3. Listar todas las monedas (Debug)
@router.get("/debug/all")
async def test_connection(db: AsyncSession = Depends(get_db)):
    try:
        query = select(Currency)
        result = await db.execute(query)
        return result.scalars().all()
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, 
            detail=f"Error de conexión: {str(e)}"
        )