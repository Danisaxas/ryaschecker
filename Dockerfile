# Usar una imagen base de Python
FROM python:3.9

# Establecer el directorio de trabajo dentro del contenedor
WORKDIR /app

# Copiar el archivo requirements.txt al contenedor
COPY requirements.txt /app/

# Actualizar pip antes de instalar las dependencias
RUN pip install --upgrade pip

# Instalar las dependencias de Python desde requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Copiar el resto de los archivos de la aplicación al contenedor
COPY . /app/

# Establecer la variable de entorno para el path de Nixpacks (si es necesario)
# ENV NIXPACKS_PATH=/opt/venv/bin:$NIXPACKS_PATH

# Comando para ejecutar la aplicación (ajústalo según sea necesario)
CMD ["python", "app.py"]