import requests
import bs4

pagina = requests.get("https://www.comuniazo.com/comunio-apuestas/jugadores")


soup = bs4.BeautifulSoup(pagina.content)

jugadores = soup.find_all("tr", {"class":"btn"})

plantilla = {
    "posicion": None,
    "nombre": None,
    "equipo":None,
    "puntos":None,
    "media":None
}

list_jugadores = []

for jugador in jugadores:

    #Hacer copia del diccionario
    dic_jugador = plantilla.copy()

    #Sacais los campos
    nombre = jugador.find("div", {"class":"player"}).strong.text
    puntos = int(jugador.find("td", {"class":"tac"}).text)

    #Rellenar el diccionario
    dic_jugador["nombre"] = nombre
    dic_jugador["puntos"] = puntos

    #Meter el diccionario en la lista
    list_jugadores.append(dic_jugador)

print(list_jugadores)