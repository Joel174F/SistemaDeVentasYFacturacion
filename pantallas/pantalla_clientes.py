
"""
pantalla_clientes.py
RESPONSABLE: Companiero C
Pantalla de gestion de clientes.
"""

import tkinter as tk
from tkinter import messagebox
import estilos

from componentes_pequenos.etiqueta import Etiqueta
from componentes_pequenos.boton import Boton
from componentes_armados.campo_formulario import CampoFormulario
from componentes_armados.tabla import Tabla
from funciones import logica_clientes


COLUMNAS = [
    ("codigo", "Codigo", 70),
    ("nombre", "Nombre", 180),
    ("telefono", "Telefono", 120),
    ("email", "Email", 180),
]


class PantallaClientes(tk.Frame):

    def __init__(self, padre):
        super().__init__(
            padre,
            bg=estilos.COLORES["fondo"],
            padx=20,
            pady=20
        )

        Etiqueta(self, "Clientes", "titulo").pack(
            fill="x", pady=(0, 10)
        )

        # --- Formulario a la izquierda ---
        izquierda = tk.Frame(
            self,
            bg=estilos.COLORES["fondo"]
        )
        izquierda.pack(side="left", fill="y", padx=(0, 20))

        # Campos obligatorios
        self.campo_nombre = CampoFormulario(
            izquierda, "Nombre *"
        )
        self.campo_nombre.pack(fill="x")

        self.campo_telefono = CampoFormulario(
            izquierda, "Telefono *"
        )
        self.campo_telefono.pack(fill="x")

        self.campo_email = CampoFormulario(
            izquierda, "Email *"
        )
        self.campo_email.pack(fill="x")

        Etiqueta(
            izquierda,
            "* Todos los campos son obligatorios",
            "normal"
        ).pack(anchor="w", pady=5)

        Boton(
            izquierda, "Agregar", self.agregar
        ).pack(fill="x", pady=2)

        Boton(
            izquierda, "Modificar", self.modificar
        ).pack(fill="x", pady=2)

        Boton(
            izquierda, "Eliminar", self.eliminar,
            tipo="peligro"
        ).pack(fill="x", pady=2)

        # --- Busqueda y tabla a la derecha ---
        derecha = tk.Frame(
            self,
            bg=estilos.COLORES["fondo"]
        )
        derecha.pack(side="right", fill="both", expand=True)

        self.campo_buscar = CampoFormulario(
            derecha, "Buscar por nombre"
        )
        self.campo_buscar.pack(fill="x")

        Boton(
            derecha, "Buscar", self.buscar
        ).pack(anchor="w", pady=(0, 10))

        self.tabla = Tabla(
            derecha,
            COLUMNAS,
            al_seleccionar=self.al_elegir_fila
        )
        self.tabla.pack(fill="both", expand=True)

        self.recargar_tabla()

    # ---------- Funciones auxiliares ----------

    def recargar_tabla(self):
        self.tabla.cargar(
            logica_clientes.cargar_clientes()
        )

    def limpiar_formulario(self):
        self.campo_nombre.limpiar()
        self.campo_telefono.limpiar()
        self.campo_email.limpiar()

    def obtener_datos_validos(self):
        """Comprueba que todos los campos obligatorios tengan datos."""

        nombre = self.campo_nombre.obtener().strip()
        telefono = self.campo_telefono.obtener().strip()
        email = self.campo_email.obtener().strip()

        if not nombre:
            messagebox.showwarning(
                "Campo obligatorio",
                "Debes ingresar el nombre del cliente."
            )
            return None

        if not telefono:
            messagebox.showwarning(
                "Campo obligatorio",
                "Debes ingresar el telefono del cliente."
            )
            return None

        if not email:
            messagebox.showwarning(
                "Campo obligatorio",
                "Debes ingresar el email del cliente."
            )
            return None

        return nombre, telefono, email

    def al_elegir_fila(self, fila):
        """Carga los datos del cliente seleccionado."""

        self.campo_nombre.escribir(fila["nombre"])
        self.campo_telefono.escribir(fila["telefono"])
        self.campo_email.escribir(fila["email"])

    def mostrar_resultado(self, ok, mensaje):
        """Muestra el resultado de la operacion."""

        if ok:
            messagebox.showinfo("Listo", mensaje)
            self.recargar_tabla()
            self.limpiar_formulario()
        else:
            messagebox.showwarning("Atencion", mensaje)

    # ---------- Boton Agregar ----------

    def agregar(self):

        datos = self.obtener_datos_validos()

        if datos is None:
            return

        nombre, telefono, email = datos

        confirmar = messagebox.askyesno(
            "Confirmar registro",
            "¿Estas seguro de que deseas guardar este nuevo cliente?"
        )

        if not confirmar:
            return

        ok, mensaje = logica_clientes.agregar_cliente(
            nombre,
            telefono,
            email
        )

        self.mostrar_resultado(ok, mensaje)

    # ---------- Boton Modificar ----------

    def modificar(self):

        fila = self.tabla.obtener_seleccion()

        if fila is None:
            messagebox.showwarning(
                "Atencion",
                "Elegi un cliente de la tabla."
            )
            return

        datos = self.obtener_datos_validos()

        if datos is None:
            return

        nombre, telefono, email = datos

        confirmar = messagebox.askyesno(
            "Confirmar cambios",
            "¿Estas seguro de que deseas modificar este cliente?"
        )

        if not confirmar:
            return

        ok, mensaje = logica_clientes.modificar_cliente(
            fila["codigo"],
            nombre,
            telefono,
            email
        )

        self.mostrar_resultado(ok, mensaje)

    # ---------- Boton Eliminar ----------

    def eliminar(self):

        fila = self.tabla.obtener_seleccion()

        if fila is None:
            messagebox.showwarning(
                "Atencion",
                "Elegi un cliente de la tabla."
            )
            return

        confirmar = messagebox.askyesno(
            "Confirmar eliminacion",
            f"¿Deseas eliminar a '{fila['nombre']}'?"
        )

        if not confirmar:
            return

        ok, mensaje = logica_clientes.eliminar_cliente(
            fila["codigo"]
        )

        self.mostrar_resultado(ok, mensaje)

    # ---------- Boton Buscar ----------

    def buscar(self):

        texto = self.campo_buscar.obtener()

        resultados = logica_clientes.buscar_cliente(texto)

        self.tabla.cargar(resultados)
