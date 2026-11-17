"""
boton.py  (ATOMO)
Boton moderno con esquinas redondeadas, dibujado sobre un Canvas.
Se usa igual que antes:  Boton(padre, "Texto", funcion, tipo="primario")
tipo: "primario" (azul), "exito" (verde) o "peligro" (rojo)
icono: texto opcional que se muestra antes del texto
"""
import tkinter as tk
from tkinter import font as tkfont
import estilos


class Boton(tk.Canvas):
    def __init__(self, padre, texto, comando, tipo="primario", icono=""):
        self.color = estilos.COLORES[tipo]
        self.color_hover = estilos.COLORES[tipo + "_hover"]
        self.comando = comando
        self.texto = f"{icono}  {texto}" if icono else texto
        self.fuente = estilos.FUENTES["boton"]
        self.actual = self.color

        ancho_texto = tkfont.Font(font=self.fuente).measure(self.texto)
        super().__init__(
            padre, width=ancho_texto + 48, height=40,
            bg=estilos.fondo_de(padre), highlightthickness=0, bd=0, cursor="hand2",
        )

        self.bind("<Configure>", lambda evento: self._dibujar())
        self.bind("<Enter>", lambda evento: self._pintar(self.color_hover))
        self.bind("<Leave>", lambda evento: self._pintar(self.color))
        self.bind("<Button-1>", lambda evento: self.comando())

    def _pintar(self, color):
        self.actual = color
        self._dibujar()

    def _dibujar(self):
        self.delete("all")
        ancho = self.winfo_width()
        alto = self.winfo_height()
        if ancho < 10:
            ancho = int(float(self.cget("width")))
        self._rect_redondeado(1, 1, ancho - 1, alto - 1, 10, fill=self.actual, outline=self.actual)
        self.create_text(
            ancho / 2, alto / 2, text=self.texto,
            fill=estilos.COLORES["texto_claro"], font=self.fuente,
        )

    def _rect_redondeado(self, x1, y1, x2, y2, r, **opciones):
        """Rectangulo con esquinas redondeadas (poligono suavizado)."""
        puntos = [
            x1 + r, y1, x1 + r, y1, x2 - r, y1, x2 - r, y1, x2, y1,
            x2, y1 + r, x2, y1 + r, x2, y2 - r, x2, y2 - r, x2, y2,
            x2 - r, y2, x2 - r, y2, x1 + r, y2, x1 + r, y2, x1, y2,
            x1, y2 - r, x1, y2 - r, x1, y1 + r, x1, y1 + r, x1, y1,
        ]
        return self.create_polygon(puntos, smooth=True, **opciones)
