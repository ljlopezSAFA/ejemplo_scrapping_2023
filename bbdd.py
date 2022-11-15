def insertar_datos():

    list_jugadores = web_scraping()

    conexion = db.connect(host='localhost',
                          port=3306,
                          database='comuniazo',
                          user='root',
                          password='1234', autocommit=True)


    cursor = conexion.cursor()

    cursor.execute("delete from jugador where id > 0")
    cursor.execute("ALTER TABLE jugador auto_increment = 0")


    for jugador in list_jugadores:
        script = "insert into jugador (posicion, equipo, nombre, puntos_totales,valor)  VALUES (%s, %s, %s, %s, %s)"
        cursor.execute(script,(jugador["posicion"], jugador["equipo"], jugador["nombre"], jugador["puntos_totales"], jugador["valor"]))


    conexion.close()

    print("Datos insertados correctamente")






insertar_datos()
