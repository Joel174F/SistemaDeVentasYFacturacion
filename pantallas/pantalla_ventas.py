"""
pantalla_ventas.py
RESPONSABLE: Joel
Pantalla de nueva venta:
  izquierda -> catalogo de productos + cantidad + "Agregar al carrito"
  derecha   -> cliente, carrito, descuento, totales y "Finalizar venta"
"""
import tkinter as tk
from tkinter import ttk, messagebox
import estilos
from componentes_pequenos.etiqueta import Etiqueta
from componentes_pequenos.boton import Boton
from componentes_armados.campo_formulario import CampoFormulario
from componentes_armados.tabla import Tabla
from funciones import calculos, logica_ventas

COLUMNAS_PRODUCTOS = [
    ("codigo", "Cod", 50),
    ("nombre", "Producto", 170),
    ("precio", "Precio", 80),
    ("stock", "Stock", 60),
]
COLUMNAS_CARRITO = [
    ("nombre", "Producto", 160),
    ("precio", "Precio", 80),
    ("cantidad", "Cant", 50),
    ("subtotal", "Subtotal", 90),
]


class PantallaVentas(tk.Frame):
    def __init__(self, padre):
        super().__init__(padre, bg=estilos.COLORES["fondo"], padx=20, pady=20)

        self.carrito = []                              # lista de diccionarios
        self.clientes = logica_ventas.listar_clientes()

        Etiqueta(self, "Nueva venta", "titulo").pack(fill="x", pady=(0, 10))

        self._armar_lado_izquierdo()
        self._armar_lado_derecho()

        self.recargar_productos()
        self.actualizar_totales()

    # ---------- Armado de la pantalla ----------
    def _armar_lado_izquierdo(self):
        izquierda = tk.Frame(self, bg=estilos.COLORES["fondo"])
        izquierda.pack(side="left", fill="both", expand=True, padx=(0, 20))

        Etiqueta(izquierda, "1. Elegi un producto").pack(fill="x")
        self.tabla_productos = Tabla(izquierda, COLUMNAS_PRODUCTOS)
        self.tabla_productos.arbol.config(height=8)
        self.tabla_productos.pack(fill="both", expand=True)

        self.campo_cantidad = CampoFormulario(izquierda, "Cantidad")
        self.campo_cantidad.pack(fill="x", pady=(10, 0))
        self.campo_cantidad.escribir(1)

        Boton(izquierda, "Agregar al carrito", self.agregar_al_carrito).pack(fill="x")

    def _armar_lado_derecho(self):
        derecha = tk.Frame(self, bg=estilos.COLORES["fondo"])
        derecha.pack(side="right", fill="both", expand=True)

        Etiqueta(derecha, "2. Cliente").pack(fill="x")
        self.lista_clientes = ttk.Combobox(
            derecha, state="readonly", font=estilos.FUENTES["normal"],
            values=self.nombres_clientes(),
        )
        self.lista_clientes.current(0)   # por defecto: Consumidor Final
        self.lista_clientes.pack(fill="x", pady=(0, 10))

        Etiqueta(derecha, "3. Carrito").pack(fill="x")
        self.tabla_carrito = Tabla(derecha, COLUMNAS_CARRITO)
        self.tabla_carrito.arbol.config(height=5)
        self.tabla_carrito.pack(fill="both", expand=True)

        Boton(derecha, "Quitar seleccionado", self.quitar_del_carrito,
              tipo="peligro").pack(fill="x", pady=(5, 0))

        self.campo_descuento = CampoFormulario(derecha, "Descuento manual (%)")
        self.campo_descuento.pack(fill="x", pady=(5, 0))
        self.campo_descuento.escribir(0)
        # Cada vez que se escribe algo en el descuento, se recalculan los totales
        self.campo_descuento.campo.bind("<KeyRelease>", lambda e: self.actualizar_totales())

        self.etiqueta_subtotal = Etiqueta(derecha, "")
        self.etiqueta_subtotal.pack(fill="x")
        self.etiqueta_descuento = Etiqueta(derecha, "")
        self.etiqueta_descuento.pack(fill="x")
        self.etiqueta_iva = Etiqueta(derecha, "")
        self.etiqueta_iva.pack(fill="x")
        self.etiqueta_total = Etiqueta(derecha, "", "titulo")
        self.etiqueta_total.pack(fill="x", pady=(0, 5))

        Boton(derecha, "Finalizar venta", self.finalizar).pack(fill="x")

    # ---------- Funciones auxiliares ----------
    def nombres_clientes(self):
        """Texto de cada opcion de la lista desplegable."""
        opciones = ["0 - Consumidor Final"]
        for c in self.clientes:
            opciones.append(f"{c['codigo']} - {c['nombre']}")
        return opciones

    def cliente_elegido(self):
        """Devuelve (codigo, nombre) del cliente seleccionado."""
        posicion = self.lista_clientes.current()
        if posicion <= 0:
            return 0, "Consumidor Final"
        cliente = self.clientes[posicion - 1]
        return cliente["codigo"], cliente["nombre"]

    def recargar_productos(self):
        self.tabla_productos.cargar(logica_ventas.listar_productos())

    def porcentaje_descuento(self):
        """El mayor entre el descuento manual y el automatico por volumen."""
        try:
            manual = float(self.campo_descuento.obtener() or 0)
        except ValueError:
            manual = 0
        manual = max(0, min(100, manual))   # siempre entre 0 y 100
        automatico = calculos.descuento_por_volumen(calculos.calcular_subtotal(self.carrito))
        return max(manual, automatico)

    def actualizar_totales(self):
        porcentaje = self.porcentaje_descuento()
        t = calculos.calcular_totales(self.carrito, porcentaje)
        self.etiqueta_subtotal.config(text=f"Subtotal: $ {t['subtotal']:.2f}")
        self.etiqueta_descuento.config(text=f"Descuento ({porcentaje:g}%): - $ {t['descuento']:.2f}")
        self.etiqueta_iva.config(text=f"IVA (21%): $ {t['iva']:.2f}")
        self.etiqueta_total.config(text=f"TOTAL: $ {t['total']:.2f}")

    def recargar_carrito(self):
        self.tabla_carrito.cargar(self.carrito)
        self.actualizar_totales()

    # ---------- Botones ----------
    def agregar_al_carrito(self):
        producto = self.tabla_productos.obtener_seleccion()
        if producto is None:
            messagebox.showwarning("Atencion", "Elegi un producto de la tabla.")
            return

        try:
            cantidad = int(self.campo_cantidad.obtener())
        except ValueError:
            messagebox.showwarning("Atencion", "La cantidad debe ser un numero entero.")
            return
        if cantidad <= 0:
            messagebox.showwarning("Atencion", "La cantidad debe ser mayor a 0.")
            return

        # Buscamos si el producto ya estaba en el carrito
        item_existente = None
        for item in self.carrito:
            if item["codigo"] == producto["codigo"]:
                item_existente = item

        ya_agregado = item_existente["cantidad"] if item_existente else 0
        if cantidad + ya_agregado > producto["stock"]:
            disponible = producto["stock"] - ya_agregado
            messagebox.showwarning("Stock insuficiente", f"Solo quedan {disponible} unidades disponibles.")
            return

        if item_existente:
            item_existente["cantidad"] += cantidad
            item_existente["subtotal"] = round(item_existente["precio"] * item_existente["cantidad"], 2)
        else:
            self.carrito.append({
                "codigo": producto["codigo"],
                "nombre": producto["nombre"],
                "precio": producto["precio"],
                "cantidad": cantidad,
                "subtotal": round(producto["precio"] * cantidad, 2),
            })

        self.campo_cantidad.escribir(1)
        self.recargar_carrito()

    def quitar_del_carrito(self):
        fila = self.tabla_carrito.obtener_seleccion()
        if fila is None:
            messagebox.showwarning("Atencion", "Elegi un item del carrito.")
            return
        # Nos quedamos con todos los items menos el elegido
        self.carrito = [i for i in self.carrito if i["codigo"] != fila["codigo"]]
        self.recargar_carrito()

    def finalizar(self):
        if not self.carrito:
            messagebox.showwarning("Atencion", "El carrito esta vacio.")
            return

        codigo, nombre = self.cliente_elegido()
        ok, mensaje = logica_ventas.registrar_venta(
            self.carrito, codigo, nombre, self.porcentaje_descuento()
        )

        if ok:
            messagebox.showinfo("Venta registrada", mensaje)
            self.carrito = []
            self.campo_descuento.escribir(0)
            self.recargar_carrito()
            self.recargar_productos()   # el stock cambio
        else:
            messagebox.showwarning("No se pudo registrar", mensaje)
