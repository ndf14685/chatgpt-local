# Usa una imagen base de Python
FROM python:3.9-slim

# Establece el directorio de trabajo
WORKDIR /app

# Copiar requirements.txt primero para aprovechar la caché de Docker
COPY ./requirements.txt /app/requirements.txt

# Instala las dependencias
RUN pip install --no-cache-dir -r /app/requirements.txt

RUN pip install --upgrade openai
# Copiar el resto de la aplicación al contenedor
COPY ./src /app/src
#COPY ./scripts /app/scripts

# Establecer la variable de entorno PYTHONPATH para que Python busque módulos en /app/src
ENV PYTHONPATH "${PYTHONPATH}:/app/src"

# Expone el puerto del contenedor
EXPOSE 5000

# Comando para ejecutar Gunicorn
CMD ["gunicorn", "--bind", "0.0.0.0:5000", "--workers", "4", "--timeout", "120", "src.app:app"]


