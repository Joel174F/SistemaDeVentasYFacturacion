"""
pantalla_productos.py
RESPONSABLE: Companiero B
La pantalla YA ESTA ARMADA como ejemplo de como se usan los componentes.
Tu trabajo: completar funciones/logica_productos.py (las funciones que
devuelven "Falta implementar"). Despues podes mejorar esta pantalla.
Solo edita este archivo y funciones/logica_productos.py.
"""
import tkinter as tk
from tkinter import messagebox
import estilos
from componentes_pequenos.etiqueta import Etiqueta
from componentes_pequenos.boton import Boton
from componentes_armados.campo_formulario import CampoFormulario
from componentes_armados.tabla import Tabla
from funciones import logica_productos

COLUMNAS = [
    ("codigo", "Codigo", 70),
    ("nombre", "Nombre", 220),
    ("precio", "Precio", 90),
    ("stock", "Stock", 70),
]


class PantallaProductos(tk.Frame):
    def __init__(self, padre):
        super().__init__(padre, bg=estilos.COLORES["fondo"], padx=20, pady=20)

        Etiqueta(self, "Productos", "titulo").pack(fill="x", pady=(0, 10))

        # --- Formulario a la izquierda ---
        izquierda = tk.Frame(self, bg=estilos.COLORES["fondo"])
        izquierda.pack(side="left", fill="y", padx=(0, 20))

        self.campo_nombre = CampoFormulario(izquierda, "Nombre")
        self.campo_nombre.pack(fill="x")
        self.campo_precio = CampoFormulario(izquierda, "Precio")
        self.campo_precio.pack(fill="x")
        self.campo_stock = CampoFormulario(izquierda, "Stock")
        self.campo_stock.pack(fill="x")

        Boton(izquierda, "Agregar", self.agregar).pack(fill="x", pady=2)
        Boton(izquierda, "Modificar", self.modificar).pack(fill="x", pady=2)
        Boton(izquierda, "Eliminar", self.eliminar, tipo="peligro").pack(fill="x", pady=2)

        # --- Tabla a la derecha ---
        self.tabla = Tabla(self, COLUMNAS, al_seleccionar=self.al_elegir_fila)
        self.tabla.pack(side="right", fill="both", expand=True)

        self.recargar_tabla()

    # ---------- Funciones auxiliares ----------
    def recargar_tabla(self):
        self.tabla.cargar(logica_productos.cargar_productos())

    def limpiar_formulario(self):
        self.campo_nombre.limpiar()
        self.campo_precio.limpiar()
        self.campo_stock.limpiar()

    def al_elegir_fila(self, fila):
        """Cuando se hace clic en una fila, sus datos pasan al formulario."""
        self.campo_nombre.escribir(fila["nombre"])
        self.campo_precio.escribir(fila["precio"])
        self.campo_stock.escribir(fila["stock"])

    def mostrar_resultado(self, ok, mensaje):
        """Muestra el mensaje que devolvio la logica."""
        if ok:
            messagebox.showinfo("Listo", mensaje)
            self.recargar_tabla()
            self.limpiar_formulario()
        else:
            messagebox.showwarning("Atencion", mensaje)

    # ---------- Botones ----------
    def agregar(self):
        ok, mensaje = logica_productos.agregar_producto(
            self.campo_nombre.obtener(),
            self.campo_precio.obtener(),
            self.campo_stock.obtener(),
        )
        self.mostrar_resultado(ok, mensaje)

    def modificar(self):
        fila = self.tabla.obtener_seleccion()
        if fila is None:
            messagebox.showwarning("Atencion", "Elegi un producto de la tabla.")
            return
        ok, mensaje = logica_productos.modificar_producto(
            fila["codigo"],
            self.campo_nombre.obtener(),
            self.campo_precio.obtener(),
            self.campo_stock.obtener(),
        )
        self.mostrar_resultado(ok, mensaje)

    def eliminar(self):
        fila = self.tabla.obtener_seleccion()
        if fila is None:
            messagebox.showwarning("Atencion", "Elegi un producto de la tabla.")
            return
        if messagebox.askyesno("Confirmar", f"Eliminar '{fila['nombre']}'?"):
            ok, mensaje = logica_productos.eliminar_producto(fila["codigo"])
            self.mostrar_resultado(ok, mensaje)
