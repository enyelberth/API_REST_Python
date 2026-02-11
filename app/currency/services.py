from fastapi import HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select, text

from app.currency.models import Currency
from .schemas import CurrencyCreate, CurrencyResponse


# 1. Crear moneda
async def create_currency(currency: CurrencyCreate, db: AsyncSession) -> CurrencyResponse:
    # Verificar existencia con SQL crudo
    sql = text("SELECT id, name, code FROM currency WHERE name = :name")
    result = await db.execute(sql, {"name": currency.name})
    row = result.first()

    if row:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=f"La moneda {currency.name} ya está registrada."
        )

    # Insert con SQL crudo
    insert_sql = text("""
        INSERT INTO currency (name, code,description)
        VALUES (:name, :code,:description)
        RETURNING id, name, code,description
    """)
    result_insert = await db.execute(
        insert_sql,
        {"name": currency.name, "code": currency.code,"description": currency.description}
    )
    await db.commit()

    nueva_moneda = result_insert.first()

    if not nueva_moneda:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="No se pudo crear la moneda."
        )

    # Devolver dict / schema compatible con CurrencyResponse
    return CurrencyResponse(
        id=nueva_moneda.id,
        name=nueva_moneda.name,
        code=nueva_moneda.code,
    )


# 2. Obtener moneda por ID (GET)
async def get_currency(currency_id: int, db: AsyncSession) -> Currency:
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
async def test_connection(db: AsyncSession):
    try:
        query = select(Currency)
        result = await db.execute(query)
        return result.scalars().all()
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Error de conexión: {str(e)}"
        )
