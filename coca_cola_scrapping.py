import requests
import bs4

#Paso 1 -> buscar la pagina
pagina = requests.get("https://www.cocacola.es/productos-coca-cola")

#Paso 2 -> convertir la pagina en sopa
soup = bs4.BeautifulSoup(pagina.content)

#Paso 3 -> creamos el diccionario plantilla
plantilla = {
    "imagen": None,
    "titulo": None,
    "decripcion" : None
}

#Paso 4 -> Montar un findAll que me busque todos los elementos
coca_colas = soup.find("div",{"class": "aem-Grid aem-Grid--12 aem-Grid--default--12"}).find_all("div")


#Paso 5 -> empezamos a hacer scrapping
lista_coca_colas = []

indice = 0
for coca_cola in coca_colas:

    if indice != 0:

        #Copia del diccionario
        diccionario = plantilla.copy()
        #Buscar los campos
        descripcion = coca_cola.find()

    indice+=1

