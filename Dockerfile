FROM python:3.9-slim

# Instalar las dependencias del sistema si es necesario
RUN apt-get update && apt-get install -y python3-pip

# Copiar el código al contenedor
COPY . /app/

# Establecer el directorio de trabajo
WORKDIR /app

# Instalar las dependencias de Python
RUN pip install --no-cache-dir -r requirements.txt

# Comando para ejecutar la aplicación (ajustar según tu caso)
CMD ["python", "app.py"]