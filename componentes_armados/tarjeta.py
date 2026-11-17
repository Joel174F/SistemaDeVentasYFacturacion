"""
tarjeta.py  (COMPONENTE ARMADO)
Un recuadro blanco con borde fino y un titulo opcional.
Lo que se coloque dentro (pack) queda debajo del titulo.
    tarjeta = Tarjeta(self, "Productos", estilos.ICONOS["productos"])
    tarjeta.pack()
    Tabla(tarjeta, ...).pack()
"""
import tkinter as tk
import estilos


class Tarjeta(tk.Frame):
    def __init__(self, padre, titulo="", icono=""):
        super().__init__(
            padre, bg=estilos.COLORES["blanco"],
            highlightthickness=1, highlightbackground=estilos.COLORES["borde"],
            highlightcolor=estilos.COLORES["borde"], padx=14, pady=12,
        )
        if titulo:
            cabecera = tk.Frame(self, bg=estilos.COLORES["blanco"])
            cabecera.pack(fill="x", pady=(0, 8))
            if icono:
                tk.Label(
                    cabecera, text=icono, bg=estilos.COLORES["blanco"],
                    fg=estilos.COLORES["primario"], font=("Segoe UI", 14),
                ).pack(side="left", padx=(0, 8))
            tk.Label(
                cabecera, text=titulo, bg=estilos.COLORES["blanco"],
                fg=estilos.COLORES["texto"], font=estilos.FUENTES["tarjeta"],
            ).pack(side="left")
