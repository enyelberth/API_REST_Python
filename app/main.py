from fastapi import APIRouter
from app.users.router import router as users_router
from app.persons.router import router as persons_router
from app.currency.router import router as currency_router

# Importamos los modelos para asegurarnos de que SQLAlchemy los registre
from app.currency.models import Currency, PairCurrency, CurrencyPrice

main_router = APIRouter()

# Registro de rutas
main_router.include_router(users_router, prefix="/users", tags=["users"])
main_router.include_router(persons_router, prefix="/persons", tags=["persons"])
main_router.include_router(currency_router, prefix="/currency", tags=["currency"])

# NOTA: La creación de tablas y la apertura de sesión NO se hacen aquí.
# Se gestionan en el archivo principal de la app (el que tiene FastAPI())
# o mediante inyección de dependencias (Depends(get_db)).