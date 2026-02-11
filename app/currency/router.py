from app.currency import services
from sqlalchemy.ext.asyncio import AsyncSession
from app.db import get_db
from app.currency.schemas import CurrencyResponse,CurrencyCreate
from fastapi import APIRouter, HTTPException, status, Depends

router = APIRouter()

@router.post("/", response_model=CurrencyResponse, status_code=status.HTTP_201_CREATED)
async def create_currency_endpoint(
    currency: CurrencyCreate,
    db: AsyncSession = Depends(get_db),
):
    print("Creando moneda...")
    try:
        print(currency)
        result = await services.create_currency(currency, db)  # llama a la función del servicio
        print(result)
        print("Moneda creada exitosamente.")
        return result
    except Exception as e:
        print(f"Error al crear moneda: {e}")
        # IMPORTANTE: devolver algo o relanzar la excepción
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Error al crear moneda: {e}",
        )
@router.get("/",response_model=list[CurrencyResponse],status_code=status.HTTP_200_OK,)
async def get_currency_endpoint(db: AsyncSession = Depends(get_db),):
    try:
        print("Obteniendo monedas...")
        currencies = await services.test_connection(db)  # o tu service de listado
        return currencies
    except Exception as e:
        print(f"Error al obtener monedas: {e}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Error al obtener monedas: {e}",
        )