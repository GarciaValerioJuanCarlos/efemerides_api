import pandas as pd
from app.schemas.fecha import FechaRead
from typing import List

def load_efemerides_from_csv(file_path: str) -> List[FechaRead]:
    df = pd.read_csv(file_path)
    # Convertimos el DataFrame a una lista de objetos de nuestro esquema
    return [FechaRead(id=i, **row) for i, row in df.iterrows()]