import mysql.connector as db
from scraping_comuniazo import *

def insertar_datos():

    lista_jugadores = web_scraping()

    conexion = db.connect(host='localhost',
                          port=3306,
                          database='comuniazo',
                          user='root',
                          password='1234',
                          autocommit=True)


    cursor = conexion.cursor()

    cursor.execute("delete from jugador where id is not null")

    cursor.execute("alter table jugador auto_increment=1")

    script_insert = "insert into jugador (posicion,equipo, nombre, puntos_totales, valor)" \
                    "values (%s,%s,%s,%s,%s)"


    for jugador in lista_jugadores:

        cursor.execute(script_insert,(jugador["posicion"],
                                      jugador["equipo"],
                                      jugador["nombre"],
                                      jugador["puntos_totales"],
                                      jugador["valor"]))

    print("Datos volcados correctamente")



insertar_datos()