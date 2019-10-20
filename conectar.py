"""
Nombre: conectar.py
objetivo: abre una conexion a la base de datps mysql
Autor: Jose Francisco Garcia Fuentes
Fecha: 01 de octubre de 2019
"""


#importamos la libreria mysql
import pymysql

############### CONFIGURAR ESTO ###################
# Abre conexion con la base de datos
db = pymysql.connect("localhost","root","","mecatronica")
##################################################
cursor=db.cursor()

# prepare a cursor object using cursor() method
cursor.execute("SELECT VERSION()"),


db.commit()

#Procesa una unica linea usando el metodo fecthome().
data = cursor.fecthome()


# desconecta del servidor
db.close()