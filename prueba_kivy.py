from kivy.metrics import dp
from kivymd.app import MDApp
from kivy.uix.button import Button
from kivymd.uix.label import MDLabel
from kivymd.uix.screen import Screen
from kivymd.uix.fitimage import FitImage
from kivymd.uix.gridlayout import GridLayout
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.boxlayout import  BoxLayout
from kivymd.uix.datatables import MDDataTable
from kivymd.uix.textfield import MDTextField

from metodos_bbdd import *



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



def restaurar_menu(ventana, panel_botones):
    ventana.clear_widgets()
    ventana.add_widget(panel_botones)



def cargar_datos_tabla(tabla):
    #Cargar los datos
    list_jugadores = consultar_datos()

    tabla.row_data= []

    for jugador in list_jugadores:
        tabla.row_data.append(jugador)



def muestra_formulario(panel_informacion):

    #1 Limpiar el panel
    panel_informacion.clear_widgets()

    # 2 Crear formulario

    input_nombre = MDTextField(
        hint_text= "Nombre",
        mode="round",
        max_text_length=50
    )

    input_posicion = MDTextField(
        hint_text="Posición",
        mode="round",
        max_text_length=3
    )

    input_puntos = MDTextField(
        hint_text="Puntos",
        mode="round",
        max_text_length=4
    )

    input_valor = MDTextField(
        hint_text="Valor",
        mode="round",
        max_text_length=10
    )

    #3 Mostrar el formulario
    panel_informacion.add_widget(input_posicion)
    panel_informacion.add_widget(input_nombre)
    panel_informacion.add_widget(input_puntos)
    panel_informacion.add_widget(input_valor)


def guardar_en_bbdd(panel_informacion):

    nuevo_jugador = dict()
    nuevo_jugador["pos"] = panel_informacion.children[3].text
    nuevo_jugador["nombre"] = panel_informacion.children[2].text
    nuevo_jugador["puntos"] = int(panel_informacion.children[1].text)
    nuevo_jugador["valor"] = int(panel_informacion.children[0].text)

    insertar(nuevo_jugador)



def crear_panel_botones(ventana,
                        tabla,
                        panel_informacion):

    panel_botones = GridLayout(cols=6, row_force_default=True, row_default_height=70)

    boton1 = Button(text ="Cargar",
                font_size ="20sp",
                background_color =(1, 0, 0, 1),)
    boton1.bind(on_press=lambda a: restaurar_menu(ventana, panel_botones))

    boton2 = Button(text="Mostrar")
    boton2.bind(on_press=lambda a: cargar_datos_tabla(tabla))

    boton3 = Button(text="Nuevo")
    boton3.bind(on_press = lambda a: muestra_formulario(panel_informacion))

    boton5 = Button(text="Guardar")
    boton5.bind(on_press = lambda a: guardar_en_bbdd(panel_informacion))



    boton7 = Button(text="Ver")
    boton8 = Button(text="Buscar")

    panel_botones.add_widget(boton1)
    panel_botones.add_widget(boton2)
    panel_botones.add_widget(boton3)
    panel_botones.add_widget(boton5)
    panel_botones.add_widget(boton7)
    panel_botones.add_widget(boton8)

    return panel_botones






class Aplication(MDApp):
    def build(self):

        registros_seleccionados= []

        ventana = Screen()

        panel_informacion = BoxLayout()

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

        panel_botones = crear_panel_botones(ventana,
                                            tabla,
                                            panel_informacion)
        ventana.add_widget(panel_botones)
        panel_informacion.add_widget(tabla)
        ventana.add_widget(panel_informacion)




        return ventana




Aplication().run()
