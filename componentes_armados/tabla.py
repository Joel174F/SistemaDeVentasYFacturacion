"""
tabla.py  (COMPONENTE ARMADO)
Muestra una lista de diccionarios como una tabla.

    columnas = [("codigo", "Codigo", 70), ("nombre", "Nombre", 200)]
    tabla = Tabla(self, columnas, al_seleccionar=mi_funcion)
    tabla.pack()
    tabla.cargar([{"codigo": 1, "nombre": "Yerba"}])
    fila = tabla.obtener_seleccion()   # diccionario de la fila elegida, o None

mensaje_vacio (opcional): texto que se muestra cuando la tabla no tiene filas.
"""
import tkinter as tk
from tkinter import ttk
import estilos


class Tabla(tk.Frame):
    def __init__(self, padre, columnas, al_seleccionar=None, mensaje_vacio=""):
        super().__init__(
            padre, bg=estilos.COLORES["blanco"],
            highlightthickness=1, highlightbackground=estilos.COLORES["borde"],
        )

        self.columnas = columnas
        self.al_seleccionar = al_seleccionar
        self.mensaje_vacio = mensaje_vacio
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

        # Cartel que aparece cuando no hay filas
        self.etiqueta_vacia = None
        if mensaje_vacio:
            self.etiqueta_vacia = tk.Label(
                self.arbol, text=mensaje_vacio, justify="center",
                bg=estilos.COLORES["blanco"], fg=estilos.COLORES["texto_suave"],
                font=estilos.FUENTES["normal"],
            )
        self._actualizar_mensaje()

        self.arbol.bind("<<TreeviewSelect>>", self._al_hacer_clic)

    def _aplicar_estilo(self):
        """Colores de la tabla, tomados de estilos.py."""
        estilo = ttk.Style()
        estilo.theme_use("clam")   # tema que respeta los colores en Windows
        estilo.configure(
            "Mi.Treeview",
            background=estilos.COLORES["blanco"],
            fieldbackground=estilos.COLORES["blanco"],
            foreground=estilos.COLORES["texto"],
            font=estilos.FUENTES["normal"], rowheight=32, borderwidth=0,
        )
        estilo.configure(
            "Mi.Treeview.Heading",
            background=estilos.COLORES["menu"],
            foreground=estilos.COLORES["texto_claro"],
            font=estilos.FUENTES["boton"], relief="flat", padding=(6, 8),
        )
        estilo.map(
            "Mi.Treeview",
            background=[("selected", estilos.COLORES["primario"])],
            foreground=[("selected", estilos.COLORES["texto_claro"])],
        )
        estilo.map(
            "Mi.Treeview.Heading",
            background=[("active", estilos.COLORES["menu_hover"])],
        )

    def _actualizar_mensaje(self):
        if self.etiqueta_vacia is None:
            return
        if self.filas:
            self.etiqueta_vacia.place_forget()
        else:
            self.etiqueta_vacia.place(relx=0.5, rely=0.55, anchor="center")

    def cargar(self, filas):
        """Borra la tabla y la llena con la lista de diccionarios recibida."""
        self.arbol.delete(*self.arbol.get_children())
        self.filas = list(filas)
        for posicion, fila in enumerate(self.filas):
            # Por cada columna, buscamos su valor en el diccionario de la fila
            valores = [fila.get(clave, "") for clave, titulo, ancho in self.columnas]
            self.arbol.insert("", "end", iid=str(posicion), values=valores)
        self._actualizar_mensaje()

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
