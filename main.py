from fastapi import FastAPI

# Creamos la instancia de la aplicación
app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "¡Hola Mundo desde FastAPI!"}

@app.get("/items/{item_id}")
def read_item(item_id: int, q: str = None):
    return {"item_id": item_id, "query": q}