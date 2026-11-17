"""
encabezado_pagina.py  (COMPONENTE ARMADO)
Cabecera de cada pantalla: icono en circulo azul, titulo, subtitulo y una linea.
    EncabezadoPagina(self, "Nueva venta", "Subtitulo", icono="🛒").pack(fill="x")
"""
import tkinter as tk
import estilos
from componentes_pequenos.etiqueta import Etiqueta


class EncabezadoPagina(tk.Frame):
    def __init__(self, padre, titulo, subtitulo="", icono=""):
        fondo = estilos.fondo_de(padre)
        super().__init__(padre, bg=fondo)

        fila = tk.Frame(self, bg=fondo)
        fila.pack(fill="x")

        circulo = tk.Canvas(fila, width=52, height=52, bg=fondo, highlightthickness=0)
        circulo.create_oval(2, 2, 50, 50, fill=estilos.COLORES["primario"],
                            outline=estilos.COLORES["primario"])
        circulo.create_text(26, 26, text=icono, fill=estilos.COLORES["texto_claro"],
                            font=("Segoe UI", 18))
        circulo.pack(side="left", padx=(0, 14))

        textos = tk.Frame(fila, bg=fondo)
        textos.pack(side="left")
        Etiqueta(textos, titulo, "titulo").pack(anchor="w")
        if subtitulo:
            Etiqueta(textos, subtitulo, "subtitulo").pack(anchor="w")

        tk.Frame(self, bg=estilos.COLORES["borde"], height=1).pack(fill="x", pady=(10, 0))
