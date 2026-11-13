"""
tabla.py  (COMPONENTE ARMADO)
Muestra una lista de diccionarios como una tabla.

Se usa asi:
    columnas = [("codigo", "Codigo", 70), ("nombre", "Nombre", 200)]
    tabla = Tabla(self, columnas, al_seleccionar=mi_funcion)
    tabla.pack()
    tabla.cargar([{"codigo": 1, "nombre": "Yerba"}])

    fila = tabla.obtener_seleccion()   # diccionario de la fila elegida, o None
"""
import tkinter as tk
from tkinter import ttk
import estilos


class Tabla(tk.Frame):
    def __init__(self, padre, columnas, al_seleccionar=None):
        """
        columnas: lista de tuplas (clave, titulo, ancho)
        al_seleccionar: funcion opcional; se llama con la fila (diccionario)
                        cada vez que el usuario hace clic en una fila
        """
        super().__init__(padre, bg=estilos.COLORES["fondo"])

        self.columnas = columnas
        self.al_seleccionar = al_seleccionar
        self.filas = []   # lista de diccionarios que se estan mostrando

        self._aplicar_estilo()

        claves = [clave for clave, titulo, ancho in columnas]
        self.arbol = ttk.Treeview(
            self, columns=claves, show="headings",
            style="Mi.Treeview", selectmode="browse",
        )
        for clave, titulo, ancho in columnas:
            self.arbol.heading(clave, text=titulo)
            self.arbol.column(clave, width=ancho)

        barra = ttk.Scrollbar(self, orient="vertical", command=self.arbol.yview)
        self.arbol.configure(yscrollcommand=barra.set)

        self.arbol.pack(side="left", fill="both", expand=True)
        barra.pack(side="right", fill="y")

        self.arbol.bind("<<TreeviewSelect>>", self._al_hacer_clic)

    def _aplicar_estilo(self):
        """Colores de la tabla, tomados de estilos.py."""
        estilo = ttk.Style()
        estilo.theme_use("clam")   # tema que respeta los colores en Windows
        estilo.configure(
            "Mi.Treeview",
            background="white", fieldbackground="white",
            foreground=estilos.COLORES["texto"],
            font=estilos.FUENTES["normal"], rowheight=28,
        )
        estilo.configure(
            "Mi.Treeview.Heading",
            background=estilos.COLORES["menu"],
            foreground=estilos.COLORES["texto_claro"],
            font=estilos.FUENTES["boton"],
        )
        estilo.map("Mi.Treeview", background=[("selected", estilos.COLORES["primario"])])

    def cargar(self, filas):
        """Borra la tabla y la llena con la lista de diccionarios recibida."""
        self.arbol.delete(*self.arbol.get_children())
        self.filas = list(filas)
        for posicion, fila in enumerate(self.filas):
            # Por cada columna, buscamos su valor en el diccionario de la fila
            valores = [fila.get(clave, "") for clave, titulo, ancho in self.columnas]
            self.arbol.insert("", "end", iid=str(posicion), values=valores)

    def obtener_seleccion(self):
        """Devuelve el diccionario de la fila elegida, o None si no hay ninguna."""
        elegidas = self.arbol.selection()
        if not elegidas:
            return None
        return self.filas[int(elegidas[0])]

    def _al_hacer_clic(self, evento):
        fila = self.obtener_seleccion()
        if fila is not None and self.al_seleccionar is not None:
            self.al_seleccionar(fila)
