import os
from dotenv import load_dotenv
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession, async_sessionmaker
from sqlalchemy.orm import declarative_base

load_dotenv()

# 1. Variables de entorno
DB_USER = os.getenv("DB_USER")
DB_PASS = os.getenv("DB_PASSWORD")
DB_HOST = os.getenv("DB_HOST")
DB_PORT = os.getenv("DB_PORT")
DB_NAME = os.getenv("DB_NAME")

# 2. Construcción de la URL ASÍNCRONA (postgresql+asyncpg)
# Es vital añadir "+asyncpg" para que SQLAlchemy sepa que debe ser asíncrono
SQLALCHEMY_DATABASE_URL = (
    f"postgresql+asyncpg://{DB_USER}:{DB_PASS}@{DB_HOST}:{DB_PORT}/{DB_NAME}"
)

# 3. Engine Asíncrono
# echo=True es útil en desarrollo para ver las consultas SQL en consola
engine = create_async_engine(SQLALCHEMY_DATABASE_URL, echo=False)

# 4. Generador de sesiones asíncronas
AsyncSessionLocal = async_sessionmaker(
    bind=engine,
    class_=AsyncSession,
    expire_on_commit=False,  # Recomendado para evitar errores de objetos expirados tras commit
    autocommit=False,
    autoflush=False
)

Base = declarative_base()

# 5. Dependency Injection para FastAPI (Asíncrona)
async def get_db():
    async with AsyncSessionLocal() as db:
        try:
            yield db
        finally:
            await db.close() # Importante usar await al cerrar

# 6. Creación de tablas (Especial en Async)
# SQLAlchemy no permite create_all directamente en un motor asíncrono de forma sencilla
async def create_tables():
    async with engine.begin() as conn:
        # Se requiere run_sync para ejecutar comandos síncronos de metadata
        await conn.run_sync(Base.metadata.create_all)