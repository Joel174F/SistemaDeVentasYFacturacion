"""
logica_reportes.py
RESPONSABLE: Joel
Estadisticas calculadas a partir de ventas.json y productos.json.
Solo CALCULA y devuelve listas/diccionarios: no tiene nada visual.
"""
from funciones.archivos import leer_json


def cargar_ventas():
    return leer_json("ventas.json")


def cargar_productos():
    return leer_json("productos.json")


def resumen_general(ventas):
    """Cantidad de ventas, total facturado y ticket promedio."""
    cantidad = len(ventas)
    total = 0
    for venta in ventas:
        total += venta["totales"]["total"]
    promedio = total / cantidad if cantidad > 0 else 0
    return {
        "cantidad": cantidad,
        "total": round(total, 2),
        "promedio": round(promedio, 2),
    }


def ventas_por_dia(ventas):
    """
    Agrupa las ventas por fecha. Devuelve una lista de diccionarios,
    del dia mas reciente al mas antiguo:
        {"fecha": "2026-11-16", "cantidad": 3, "total": 25748.8, "grafico": "████"}
    """
    por_dia = {}
    for venta in ventas:
        dia = venta["fecha"][:10]          # "2026-11-16 08:02:12" -> "2026-11-16"
        if dia not in por_dia:
            por_dia[dia] = {"fecha": dia, "cantidad": 0, "total": 0.0}
        por_dia[dia]["cantidad"] += 1
        por_dia[dia]["total"] += venta["totales"]["total"]

    lista = sorted(por_dia.values(), key=por_fecha, reverse=True)

    # Barras de texto: la mas larga corresponde al dia que mas vendio
    mayor = max((d["total"] for d in lista), default=0)
    for dia in lista:
        dia["total"] = round(dia["total"], 2)
        largo = round(dia["total"] / mayor * 12) if mayor > 0 else 0
        dia["grafico"] = "█" * max(1, largo)
    return lista


def productos_mas_vendidos(ventas, limite=10):
    """
    Suma las unidades vendidas de cada producto y devuelve los mas vendidos:
        {"puesto": 1, "nombre": "Yerba", "unidades": 6, "importe": 21000.0}
    """
    acumulado = {}
    for venta in ventas:
        for item in venta["items"]:
            codigo = item["codigo"]
            if codigo not in acumulado:
                acumulado[codigo] = {
                    "codigo": codigo, "nombre": item["nombre"],
                    "unidades": 0, "importe": 0.0,
                }
            acumulado[codigo]["unidades"] += item["cantidad"]
            acumulado[codigo]["importe"] += item["subtotal"]

    lista = sorted(acumulado.values(), key=por_unidades, reverse=True)[:limite]
    for puesto, producto in enumerate(lista, start=1):
        producto["puesto"] = puesto
        producto["importe"] = round(producto["importe"], 2)
    return lista


def productos_stock_bajo(productos, minimo=10):
    """Productos cuyo stock es igual o menor al minimo."""
    return [p for p in productos if p["stock"] <= minimo]


# Funciones auxiliares para ordenar (sorted las usa como criterio)
def por_fecha(dia):
    return dia["fecha"]


def por_unidades(producto):
    return producto["unidades"]
