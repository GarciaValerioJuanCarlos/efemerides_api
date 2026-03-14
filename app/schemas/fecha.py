from pydantic import BaseModel
from typing import List

class FechaBase(BaseModel):
    Fecha : str
    Categoría : str 
    Efemeride: str 
    esDiaFestivoMéxico : str

class FechaRead(FechaBase):
    id: int  # El ID lo calculamos al leer el CSV

# Esquema para la respuesta paginada
class PaginatedFechaResponse(BaseModel):
    total: int
    page: int
    size: int
    data: List[FechaRead]