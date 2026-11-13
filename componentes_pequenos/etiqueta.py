"""
etiqueta.py  (ATOMO)
Un texto fijo en pantalla, con nuestro estilo.
"""
import tkinter as tk
import estilos


class Etiqueta(tk.Label):
    def __init__(self, padre, texto, tipo="normal"):
        # tipo puede ser "normal" o "titulo" (son claves del diccionario FUENTES)
        super().__init__(
            padre,
            text=texto,
            bg=estilos.COLORES["fondo"],
            fg=estilos.COLORES["texto"],
            font=estilos.FUENTES[tipo],
            anchor="w",
        )
