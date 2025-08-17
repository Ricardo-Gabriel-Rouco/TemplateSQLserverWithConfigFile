# Repositorio template para proyectos que usen sql server (u otra db) y uv como gestor de paquetes

## Comandos utiles

iniciar: uv run .\main.py

crear entorno de ejecucion: uv venv

iniciar entorno: usar la devolucion del comando anterior

usar pyinstaller: uv pip install pyinstaller

compilar: pyinstaller --onefile --hidden-import pyodbc main.py

## Importante:
Recordar que el config.mock.ini es un mock como tal, hay que crear un ´config.ini´ usando ese como base