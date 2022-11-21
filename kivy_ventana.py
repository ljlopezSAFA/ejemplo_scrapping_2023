from kivymd.app import MDApp
from kivymd.uix.screen import Screen
from kivy.uix.button import Button
from kivymd.uix.button import *
from kivymd.uix.gridlayout import GridLayout
from metodos_bbdd import insertar_datos
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.button import MDIconButton
from kivymd.uix.datatables import MDDataTable
from kivy.metrics import dp





def mostrar_etiqueta(panel):
    boton1 = Button(text="Hola")
    panel.add_widget(boton1)

def desaparecer(panel):
    panel.clear_widgets()


class Aplicacion(MDApp):
    def build(self):

        ventana = Screen(name="Jugadores APP")

        panel_principal = GridLayout(cols=1, rows=2)
        panel = GridLayout(cols=4,rows=3,row_force_default=True, row_default_height=40)
        panel_tabla = MDBoxLayout()

        boton1 = Button(text="Cargar")
        boton1.bind(on_press= lambda a: insertar_datos() )
        boton2 = Button(text="Buscar" )
        boton3 = Button(text="Mostrar" )
        boton3.bind(on_press=lambda a: mostrar_etiqueta(panel))
        boton4 = Button(text="Desaparecer" )
        boton4.bind(on_press=lambda a: desaparecer(panel))
        boton5 = Button(text="Cargar")
        boton6 = Button(text="Buscar")
        boton7 = Button(text="Mostrar")
        boton8 = Button(text="Eliminar")

        panel.add_widget(boton1)
        panel.add_widget(boton2)
        panel.add_widget(boton3)
        panel.add_widget(boton4)
        panel.add_widget(boton5)
        panel.add_widget(boton6)
        panel.add_widget(boton7)
        panel.add_widget(boton8)


        tabla = MDDataTable(
            column_data=[
                ("Nombre", dp(30)),
                ("Equipo", dp(30)),
                ("Valor", dp(30)),
                ("Puntos", dp(30)),
            ],
        )

        panel_tabla.add_widget(tabla)
        panel_principal.add_widget(panel)
        panel_principal.add_widget(panel_tabla)

        ventana.add_widget(panel_principal)

        return ventana




Aplicacion().run()

