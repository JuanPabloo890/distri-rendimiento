FROM python:3.10
#Crear un directorio de trabajo
WORKDIR /servidor2
COPY servidor2.py .
EXPOSE 5000

#Instalar las dependencias necesarias
RUN pip install flask

#Ejecutar la aplicacion
CMD ["python", "servidor2.py"]