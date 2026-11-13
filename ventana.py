"""
ventana.py
La ventana principal. Junta el menu (izquierda) con la pantalla actual (derecha)
y se encarga de cambiar de pantalla cuando se elige una opcion del menu.
"""
import tkinter as tk
import estilos
from componentes_armados.barra_menu import BarraMenu
from pantallas.pantalla_ventas import PantallaVentas
from pantallas.pantalla_productos import PantallaProductos
from pantallas.pantalla_clientes import PantallaClientes

# Diccionario: clave -> clase de la pantalla.
# Para agregar una pantalla nueva, se agrega una linea aca y una en OPCIONES.
PANTALLAS = {
    "ventas": PantallaVentas,
    "productos": PantallaProductos,
    "clientes": PantallaClientes,
}

# Lista de tuplas (clave, texto del boton). Define el orden del menu.
OPCIONES = [
    ("ventas", "Ventas"),
    ("productos", "Productos"),
    ("clientes", "Clientes"),
]


class Ventana(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Sistema de Ventas y Facturacion")
        self.geometry("1100x700")
        self.config(bg=estilos.COLORES["fondo"])

        # Menu a la izquierda. Le pasamos la funcion que cambia de pantalla.
        self.menu = BarraMenu(self, OPCIONES, self.mostrar_pantalla)
        self.menu.pack(side="left", fill="y")

        # Zona de la derecha donde se dibuja la pantalla actual
        self.contenedor = tk.Frame(self, bg=estilos.COLORES["fondo"])
        self.contenedor.pack(side="right", fill="both", expand=True)

        self.pantalla_actual = None
        self.mostrar_pantalla("ventas")   # pantalla inicial

    def mostrar_pantalla(self, clave):
        # 1) Borramos la pantalla anterior (si habia una)
        if self.pantalla_actual is not None:
            self.pantalla_actual.destroy()

        # 2) Creamos la nueva buscando su clase en el diccionario
        clase = PANTALLAS[clave]
        self.pantalla_actual = clase(self.contenedor)
        self.pantalla_actual.pack(fill="both", expand=True)

        # 3) Marcamos el boton del menu
        self.menu.marcar_activo(clave)
