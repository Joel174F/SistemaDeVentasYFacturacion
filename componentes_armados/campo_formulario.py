"""
campo_formulario.py  (COMPONENTE ARMADO)
Junta una Etiqueta y un CampoTexto en una sola pieza.
Se usa asi:
    nombre = CampoFormulario(self, "Nombre")
    nombre.pack()
    valor = nombre.obtener()
"""
import tkinter as tk
import estilos
from componentes_pequenos.etiqueta import Etiqueta
from componentes_pequenos.campo_texto import CampoTexto


class CampoFormulario(tk.Frame):
    def __init__(self, padre, texto, ancho=25):
        super().__init__(padre, bg=estilos.COLORES["fondo"])

        self.etiqueta = Etiqueta(self, texto)
        self.etiqueta.pack(fill="x")

        self.campo = CampoTexto(self, ancho)
        self.campo.pack(fill="x", pady=(0, estilos.ESPACIOS["medio"]))

    # Estas funciones solo "pasan" la orden al campo de texto de adentro
    def obtener(self):
        return self.campo.obtener()

    def escribir(self, texto):
        self.campo.escribir(texto)

    def limpiar(self):
        self.campo.limpiar()
