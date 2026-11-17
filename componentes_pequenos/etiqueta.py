"""
etiqueta.py  (ATOMO)
Un texto fijo en pantalla. Toma el color de fondo de donde se coloca,
asi se ve bien tanto sobre el fondo gris como dentro de una tarjeta blanca.
tipo: "normal", "titulo", "subtitulo", "chica", "tarjeta", "total"
color: opcional, para cambiar el color del texto
"""
import tkinter as tk
import estilos


class Etiqueta(tk.Label):
    def __init__(self, padre, texto, tipo="normal", color=None):
        if color is None:
            if tipo in ("subtitulo", "chica"):
                color = estilos.COLORES["texto_suave"]
            else:
                color = estilos.COLORES["texto"]
        super().__init__(
            padre,
            text=texto,
            bg=estilos.fondo_de(padre),
            fg=color,
            font=estilos.FUENTES[tipo],
            anchor="w",
        )
