from fastapi import FastAPI
from fastapi.concurrency import asynccontextmanager
from app.api.v1.fechas import router as fechas_router
from app.services.csv_loader import load_efemerides_from_csv

@asynccontextmanager
async def lifespan(app: FastAPI):
    # Guardamos los datos directamente en el estado de la 'app'
    app.state.efemerides = load_efemerides_from_csv("app/data/efemerides_mexico.csv")
    yield

app = FastAPI(lifespan=lifespan)
app.include_router(fechas_router)

@app.get("/")
def read_root():
    return {"message": "¡Hola Mundo!"}