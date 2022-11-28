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


def insertar(nuevo_jugador):

    conexion = db.connect(host='localhost',
                          port=3306,
                          database='comuniazo',
                          user='root',
                          password='1234',
                          autocommit=True)


    cursor = conexion.cursor()

    script_insert = "insert into jugador (posicion, equipo, nombre , puntos_totales, valor)" \
                    "values (%s,%s,%s,%s,%s)"


    cursor.execute(script_insert,(nuevo_jugador["pos"],
                                  "https://sin_equipo.es",
                                  nuevo_jugador["nombre"],
                                  nuevo_jugador["puntos"],
                                  nuevo_jugador["valor"]))

    print("Nuevo Jugador creado con éxito")


def consultar_datos():

    #Abrir conexion
    conexion = db.connect(host='localhost',
                          port=3306,
                          database='comuniazo',
                          user='root',
                          password='1234',
                          autocommit=True)

    #Lista
    list_jugadores = []

    #Abrir cursor
    cursor = conexion.cursor()

    #Script de bd
    consulta = "select * from jugador"

    #Ejecuto la consulta
    cursor.execute(consulta)

    for dato in cursor.fetchall():
        jugador = tuple([dato[0],dato[3],dato[1],dato[4],dato[5]])
        list_jugadores.append(jugador)

    return list_jugadores




