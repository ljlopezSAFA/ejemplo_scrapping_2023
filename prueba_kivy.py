from kivy.metrics import dp
from kivymd.app import MDApp
from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.boxlayout import  BoxLayout
from kivymd.uix.datatables import MDDataTable

from bbdd import insertar_datos
from scraping_comuniazo import web_scraping


def obtener_datos_tabla():
    list_jugadores = web_scraping()
    datos = []

    for jug in list_jugadores:
        datos_jugador = [jug["posicion"],
                         jug["equipo"],
                         jug["nombre"],
                         jug["puntos_totales"],
                         jug["valor"]]

        datos.append(tuple(datos_jugador))

    return datos







class Aplication(MDApp):
    def build(self):



        ventana = GridLayout(cols=1)
        panel_botones = GridLayout(cols=4, row_force_default=True, row_default_height=70)
        panel_tabla = GridLayout(cols=1,row_force_default=True, row_default_height=500, spacing=1)

        boton1 = Button(text="Cargar")
        boton1.bind(on_press=lambda a: insertar_datos())

        boton2 = Button(text="Mostrar")

        boton3 = Button(text="Nuevo")

        boton4 = Button(text="Buscar")

        tabla = MDDataTable(
            size_hint=(0.7, 0.6),
            use_pagination=True,
            column_data=[
                ("posicion", dp(30)),
                ("equipo",dp(30)),
                ("nombre",dp(30)),
                ("puntos",dp(30)),
                ("valor",dp(30)),]
        )

        for jug in obtener_datos_tabla():
            tabla.row_data.append(jug)

        panel_tabla.add_widget(tabla)


        panel_botones.add_widget(boton1)
        panel_botones.add_widget(boton2)
        panel_botones.add_widget(boton3)
        panel_botones.add_widget(boton4)
        ventana.add_widget(panel_botones)
        ventana.add_widget(panel_tabla)
        return ventana


Aplication().run()
