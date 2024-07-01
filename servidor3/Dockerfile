FROM python:3.10
#Crear un directorio de trabajo
WORKDIR /servidor3
COPY servidor3.py .
EXPOSE 5000

#Instalar las dependencias necesarias
RUN pip install flask

#Ejecutar la aplicacion
CMD ["python", "servidor3.py"]