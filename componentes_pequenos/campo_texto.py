"""
campo_texto.py  (ATOMO)
La cajita donde el usuario escribe, con borde fino que se pinta de azul
cuando esta seleccionada.
"""
import tkinter as tk
import estilos


class CampoTexto(tk.Entry):
    def __init__(self, padre, ancho=25):
        super().__init__(
            padre,
            width=ancho,
            font=estilos.FUENTES["normal"],
            bg=estilos.COLORES["blanco"],
            fg=estilos.COLORES["texto"],
            insertbackground=estilos.COLORES["texto"],
            relief="flat",
            bd=0,
            highlightthickness=1,
            highlightbackground=estilos.COLORES["borde"],
            highlightcolor=estilos.COLORES["primario"],
        )

    def obtener(self):
        """Devuelve lo que escribio el usuario (sin espacios de mas)."""
        return self.get().strip()

    def escribir(self, texto):
        """Borra lo que habia y escribe el texto nuevo."""
        self.delete(0, tk.END)
        self.insert(0, str(texto))

    def limpiar(self):
        self.delete(0, tk.END)
