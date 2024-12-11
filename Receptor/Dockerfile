# Imagen base para Python
FROM python:3.9-slim

# Configurar directorio de trabajo
WORKDIR /app

# Copiar dependencias
COPY requirements.txt .
RUN pip install -r requirements.txt

# Copiar el código
COPY server.py .

# Exponer el puerto 5001
EXPOSE 5001

# Comando para ejecutar la aplicación
CMD ["python", "server.py"]
