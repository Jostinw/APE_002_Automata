# Script para ejecutar Backend y Frontend simultáneamente

Write-Host " Iniciando el sistema de Análisis de Estructuras Formales..." -ForegroundColor Cyan

# 1. Iniciar el Backend en una nueva ventana
Write-Host " Levantando Backend (FastAPI) en el puerto 8050..." -ForegroundColor Yellow
Start-Process powershell -ArgumentList "-NoExit", "-Command", "cd backend; uvicorn main:app --reload --port 8050"

# 2. Esperar un momento para que el backend cargue
Start-Sleep -Seconds 2

# 3. Iniciar el Frontend en la ventana actual
Write-Host " Levantando Frontend (Streamlit)..." -ForegroundColor Green
cd frontend
streamlit run app.py