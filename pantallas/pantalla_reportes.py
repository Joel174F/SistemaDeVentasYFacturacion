"""
pantalla_reportes.py
RESPONSABLE: Joel
Muestra estadisticas de las ventas. Esta pantalla solo MUESTRA datos:
los calculos estan en funciones/logica_reportes.py
"""
import tkinter as tk
import estilos
from componentes_pequenos.etiqueta import Etiqueta
from componentes_armados.tabla import Tabla
from componentes_armados.tarjeta import Tarjeta
from componentes_armados.encabezado_pagina import EncabezadoPagina
from funciones import logica_reportes

COLUMNAS_DIAS = [
    ("fecha", "Fecha", 90),
    ("cantidad", "Ventas", 55),
    ("total", "Total", 100),
    ("grafico", "Gráfico", 150),
]
COLUMNAS_PRODUCTOS = [
    ("puesto", "#", 35),
    ("nombre", "Producto", 150),
    ("unidades", "Unidades", 70),
    ("importe", "Importe", 100),
]


class PantallaReportes(tk.Frame):
    def __init__(self, padre):
        super().__init__(padre, bg=estilos.COLORES["fondo"], padx=24, pady=16)

        EncabezadoPagina(
            self, "Reportes", "Resumen de ventas y productos más vendidos",
            icono=estilos.ICONOS["reportes"],
        ).pack(fill="x", pady=(0, 14))

        ventas = logica_reportes.cargar_ventas()
        productos = logica_reportes.cargar_productos()

        self._armar_tarjetas(ventas, productos)
        self._armar_tablas(ventas)

    def _armar_tarjetas(self, ventas, productos):
        """Cuatro numeros destacados arriba."""
        resumen = logica_reportes.resumen_general(ventas)
        stock_bajo = logica_reportes.productos_stock_bajo(productos)

        datos = [
            ("Ventas realizadas", str(resumen["cantidad"])),
            ("Total facturado", f"$ {resumen['total']:.2f}"),
            ("Ticket promedio", f"$ {resumen['promedio']:.2f}"),
            ("Productos con stock bajo", str(len(stock_bajo))),
        ]

        fila = tk.Frame(self, bg=estilos.COLORES["fondo"])
        fila.pack(fill="x", pady=(0, 14))
        for titulo, valor in datos:
            tarjeta = Tarjeta(fila, titulo)
            tarjeta.pack(side="left", fill="x", expand=True, padx=(0, 10))
            Etiqueta(tarjeta, valor, "total", color=estilos.COLORES["primario"]).pack(anchor="w")

    def _armar_tablas(self, ventas):
        """Ventas por dia (izquierda) y productos mas vendidos (derecha)."""
        fila = tk.Frame(self, bg=estilos.COLORES["fondo"])
        fila.pack(fill="both", expand=True)

        # --- Ventas por dia ---
        tarjeta_dias = Tarjeta(fila, "Ventas por día", estilos.ICONOS["reportes"])
        tarjeta_dias.pack(side="left", fill="both", expand=True, padx=(0, 10))
        tabla_dias = Tabla(tarjeta_dias, COLUMNAS_DIAS, mensaje_vacio="Todavía no hay ventas")
        tabla_dias.arbol.config(height=8)
        tabla_dias.pack(fill="both", expand=True)

        filas_dias = []
        for dia in logica_reportes.ventas_por_dia(ventas):
            filas_dias.append({
                "fecha": dia["fecha"],
                "cantidad": dia["cantidad"],
                "total": f"$ {dia['total']:.2f}",
                "grafico": dia["grafico"],
            })
        tabla_dias.cargar(filas_dias)

        # --- Productos mas vendidos ---
        tarjeta_prod = Tarjeta(fila, "Productos más vendidos", estilos.ICONOS["productos"])
        tarjeta_prod.pack(side="left", fill="both", expand=True)
        tabla_prod = Tabla(tarjeta_prod, COLUMNAS_PRODUCTOS, mensaje_vacio="Todavía no hay ventas")
        tabla_prod.arbol.config(height=8)
        tabla_prod.pack(fill="both", expand=True)

        filas_prod = []
        for producto in logica_reportes.productos_mas_vendidos(ventas):
            filas_prod.append({
                "puesto": producto["puesto"],
                "nombre": producto["nombre"],
                "unidades": producto["unidades"],
                "importe": f"$ {producto['importe']:.2f}",
            })
        tabla_prod.cargar(filas_prod)
