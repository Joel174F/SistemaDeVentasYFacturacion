"""
campo_texto.py  (ATOMO)
La cajita donde el usuario escribe. Le agregamos tres funciones utiles
para no tener que repetirlas en cada pantalla.
"""
import tkinter as tk
import estilos


class CampoTexto(tk.Entry):
    def __init__(self, padre, ancho=25):
        super().__init__(
            padre,
            width=ancho,
            font=estilos.FUENTES["normal"],
            bg="white",
            fg=estilos.COLORES["texto"],
            relief="solid",
            bd=1,
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
