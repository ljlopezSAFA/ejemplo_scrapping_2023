import bs4
import requests



def web_scraping():

    #Paso 1 -> Tomar el código HTML de la página
    html = requests.get("https://www.comuniazo.com/comunio-apuestas/jugadores")

    #Paso 2 -> Convertir nuestro html en una sopa
    soup = bs4.BeautifulSoup(html.content)


    #Paso 3 -> Crearnos un diccionario con la estructura de datos
    plantilla_jugador = {
        "posicion": None,
        "equipo": None,
        "nombre": None,
        "puntos_totales":None,
        "valor":None
    }

    lista_jugadores = []

    #Paso 4 -> Utilizar los métodos de bs4 (Encontrar los datos que quiero obtener)
    filas_tabla = soup.find_all("tr",{"class":"btn"})

    for fila in filas_tabla:

        #Creamos una copia del diccionario plantilla
        jugador = plantilla_jugador.copy()

        #Buscar los campos y asignarlos dentro del diccionario

        #NOMBRE
        jugador["nombre"] = fila.find("div", {"class":"player"}).strong.text

        #POSICION
        if fila.find("span", {"class":"player-position pos-1"}) != None:
            jugador["posicion"] = "PT"
        elif fila.find("span", {"class":"player-position pos-2"}) != None:
            jugador["posicion"] = "DF"
        elif fila.find("span", {"class": "player-position pos-3"}) != None:
            jugador["posicion"] = "MC"
        else:
            jugador["posicion"] = "DL"

        #EQUIPO
        jugador["equipo"] = fila.find("img", {"class":"team-logo"})["src"]

        #PUNTOS
        jugador["puntos_totales"] = int(fila.find_all("td", {"class":"tac"})[0].text)

        #VALOR
        jugador["valor"] = int(fila.find_all("td", {"class": "tac"})[6].text.replace(".", ""))


        #Añadir el jugador a mi lista de jugadores
        lista_jugadores.append(jugador)
        print(jugador)





web_scraping()