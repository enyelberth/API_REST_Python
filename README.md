# Proyecto FastAPI - Prueba Python

Este proyecto es una API básica construida con FastAPI.

## 🚀 Requisitos Previos

Asegúrate de tener instalado:
* Python 3.12 o superior
* `pip` (gestor de paquetes de Python)

## 🛠️ Instalación y Configuración

Sigue estos pasos para configurar el entorno local:

1. **Clonar el repositorio:**
   ```bash
   git clone <url-del-repositorio>
   cd prueba_Phython
2. **Crear el entorno virtual:**
   ```bash
   python3 -m venv .venv

3. **Activar el entorno virtual:**
   ```bash
   source .venv/bin/activate #Linux
   .venv\Scripts\activate #Windows
4. **Instalar Depedencias:**
   ```bash
   pip install -r requirements.txt

5. **Ejecucion:**
   ```bash
   python3 -m uvicorn main:app --reload
