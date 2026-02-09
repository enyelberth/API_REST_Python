from contextlib import asynccontextmanager
from fastapi import FastAPI
import logging
from app.main import main_router
from app.db import engine, create_tables  # Asegúrate de importar create_tables

# Configuración básica de logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# 1. Definimos el ciclo de vida (Lifespan)
@asynccontextmanager
async def lifespan(app: FastAPI):
    # --- CÓDIGO AL ARRANCAR ---
    logger.info("Iniciando aplicación y creando tablas...")
    try:
        await create_tables()  # Ahora sí se crearán tus tablas al encender
        logger.info("Tablas verificadas/creadas con éxito.")
    except Exception as e:
        logger.error(f"Error al crear tablas: {e}")
    
    yield  # Aquí es donde la aplicación "vive" y atiende peticiones
    
    # --- CÓDIGO AL APAGAR ---
    logger.info("Cerrando motor de base de datos...")
    await engine.dispose()
    logger.info("Conexiones cerradas correctamente.")

# 2. Inicializamos FastAPI con el lifespan
app = FastAPI(title="Mi API Multimodular", lifespan=lifespan)

app.include_router(main_router)

@app.get("/")
async def home():
    return {"status": "Servidor funcionando correctamente"}