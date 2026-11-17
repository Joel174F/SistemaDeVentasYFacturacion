"""
campo_formulario.py  (COMPONENTE ARMADO)
Junta una Etiqueta y un CampoTexto en una sola pieza.
    nombre = CampoFormulario(self, "Nombre")
    nombre.pack()
    valor = nombre.obtener()
horizontal=True pone la etiqueta a la izquierda y el campo a la derecha.
"""
import tkinter as tk
import estilos
from componentes_pequenos.etiqueta import Etiqueta
from componentes_pequenos.campo_texto import CampoTexto


class CampoFormulario(tk.Frame):
    def __init__(self, padre, texto, ancho=25, horizontal=False):
        super().__init__(padre, bg=estilos.fondo_de(padre))

        self.etiqueta = Etiqueta(self, texto)
        self.campo = CampoTexto(self, ancho)

        if horizontal:
            self.etiqueta.pack(side="left")
            self.campo.pack(side="right", ipady=4)
        else:
            self.etiqueta.pack(fill="x", pady=(0, 3))
            self.campo.pack(fill="x", ipady=5, pady=(0, estilos.ESPACIOS["medio"]))

    # Estas funciones solo "pasan" la orden al campo de texto de adentro
    def obtener(self):
        return self.campo.obtener()

    def escribir(self, texto):
        self.campo.escribir(texto)

    def limpiar(self):
        self.campo.limpiar()
