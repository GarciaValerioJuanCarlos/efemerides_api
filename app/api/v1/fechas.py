from fastapi import APIRouter, Query, Request # Importa Request
from app.schemas.fecha import PaginatedFechaResponse

router = APIRouter(prefix="/fechas", tags=["Efemérides"])

@router.get("/", response_model=PaginatedFechaResponse)
async def get_fechas(
    request: Request, # <--- Agrega el parámetro request
    page: int = Query(1, ge=1),
    size: int = Query(10, le=100)
):
    # Accedemos a los datos desde el estado de la aplicación
    efemerides = getattr(request.app.state, "efemerides", [])
    
    inicio = (page - 1) * size
    fin = inicio + size
    
    data_paginada = efemerides[inicio:fin]
    total_records = len(efemerides)
    
    return {
        "total": total_records,
        "page": page,
        "size": size,
        "data": data_paginada
    }