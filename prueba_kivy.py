from kivy.metrics import dp
from kivymd.app import MDApp
from kivy.uix.button import Button
from kivymd.uix.screen import Screen
from kivymd.uix.fitimage import FitImage
from kivymd.uix.gridlayout import GridLayout
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.boxlayout import  BoxLayout
from kivymd.uix.datatables import MDDataTable

from metodos_bbdd import *
from scraping_comuniazo import web_scraping


def obtener_datos_tabla():
    list_jugadores = consultar_datos()
    datos = []

    for jug in list_jugadores:
        datos_jugador = [jug["id"],
                         jug["posicion"],
                         jug["nombre"],
                         jug["puntos_totales"],
                         jug["valor"]]

        datos.append(tuple(datos_jugador))

    return datos


# def rellenar_tabla(tabla,ventana):
#     tabla = MDDataTable(
#             pos_hint={'center_x': 0.5 ,'center_y':0.5},
#             size_hint=(0.7, 0.7),
#             check=True,
#             use_pagination=True,
#             column_data=[
#                 ("ID", dp(22)),
#                 ("POS",dp(22)),
#                 ("NOMBRE",dp(22)),
#                 ("PUNTOS",dp(22)),
#                 ("VALOR",dp(22)),]
#         )
#     for jug in obtener_datos_tabla():
#         tabla.row_data.append(jug)
#         # tabla.row_data[0][1] = FitImage(source=tabla.row_data[0][1])
#     ventana.add_widget(tabla)

def restaurar_menu(ventana, panel_botones):
    ventana.clear_widgets()
    ventana.add_widget(panel_botones)



def cargar_datos_tabla(tabla):
    #Cargar los datos
    list_jugadores = consultar_datos()

    for jugador in list_jugadores:
        tabla.row_data.append(jugador)










def crear_panel_botones(ventana, tabla):
    panel_botones = GridLayout(cols=4, row_force_default=True, row_default_height=70)
    boton1 = Button(text ="Cargar",
                font_size ="20sp",
                background_color =(1, 0, 0, 1),)
    boton1.bind(on_press=lambda a: restaurar_menu(ventana, panel_botones))
    boton2 = Button(text="Mostrar")
    boton2.bind(on_press=lambda a: cargar_datos_tabla(tabla))
    boton3 = Button(text="Nuevo")
    boton4 = Button(text="Buscar")

    panel_botones.add_widget(boton1)
    panel_botones.add_widget(boton2)
    panel_botones.add_widget(boton3)
    panel_botones.add_widget(boton4)

    return panel_botones





class Aplication(MDApp):
    def build(self):

        ventana = Screen()

        tabla = MDDataTable(
            pos_hint={'center_x': 0.5, 'center_y': 0.5},
            size_hint=(0.7, 0.7),
            use_pagination=True,
            check=True,
            column_data=[
                ("id", dp(20)),
                ("nombre", dp(35)),
                ("posicion", dp(20)),
                ("puntos", dp(20)),
                ("valor", dp(30)),
            ]
        )


        # tabla = MDDataTable(
        #     pos_hint={'center_x': 0.5 ,'center_y':0.5},
        #     size_hint=(0.7, 0.7),
        #     check=True,
        #     use_pagination=True,
        #     column_data=[
        #         ("ID", dp(22)),
        #         ("POS",dp(22)),
        #         ("NOMBRE",dp(22)),
        #         ("PUNTOS",dp(22)),
        #         ("VALOR",dp(22)),]
        # )

        panel_botones = crear_panel_botones(ventana, tabla)
        ventana.add_widget(panel_botones)

        ventana.add_widget(tabla)
        return ventana




Aplication().run()
