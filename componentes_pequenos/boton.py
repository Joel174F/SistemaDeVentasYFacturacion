"""
boton.py  (ATOMO)
Un boton con nuestro estilo. Es la pieza mas chica: no sabe nada de pantallas.
"""
import tkinter as tk
import estilos


class Boton(tk.Button):
    def __init__(self, padre, texto, comando, tipo="primario"):
        # "tipo" puede ser "primario" o "peligro" (define los colores)
        self.color = estilos.COLORES[tipo]
        self.color_hover = estilos.COLORES[tipo + "_hover"]

        super().__init__(
            padre,
            text=texto,
            command=comando,
            bg=self.color,
            fg=estilos.COLORES["texto_claro"],
            font=estilos.FUENTES["boton"],
            relief="flat",        # sin borde 3D
            cursor="hand2",       # manito al pasar el mouse
            padx=estilos.ESPACIOS["grande"],
            pady=estilos.ESPACIOS["chico"],
        )

        # Efecto: cambia de color cuando el mouse entra y sale
        self.bind("<Enter>", lambda evento: self.config(bg=self.color_hover))
        self.bind("<Leave>", lambda evento: self.config(bg=self.color))
