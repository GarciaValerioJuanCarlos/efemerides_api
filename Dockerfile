# Imagen sobre la que nos basaremos
FROM python:3.8.19-alpine3.20

# Carpeta de trabajo dentro del contenedor
WORKDIR /app

# Copiamos el archivo con las librerías que usaremos
COPY requirements.txt .

# Instalamos dependencias
RUN pip install --no-cache-dir -r requirements.txt

# Copiamos archivos del proyecto (Los que debe de ignorar se ponen en el .dockerignore)
COPY . .

# Exponemos el puerto por el cual accederemos desde DOCKER, EXTERNO:INTERNO_DOCKER
EXPOSE 8000

# Comando para ejecutar el proyecto
CMD ["fastapi","dev", "main.py", "--host", "0.0.0.0","--port", "8000"]