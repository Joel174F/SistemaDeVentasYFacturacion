"""
calculos.py
RESPONSABLE: Joel
Todas las cuentas de una venta: subtotal, descuento, IVA y total.
No usa pantallas ni archivos: solo recibe datos y devuelve resultados.

Un "carrito" es una LISTA de diccionarios, uno por producto:
    carrito = [
        {"codigo": 1, "nombre": "Yerba", "precio": 3500.0, "cantidad": 2},
        {"codigo": 3, "nombre": "Aceite", "precio": 2800.0, "cantidad": 1},
    ]
"""

IVA = 0.21   # 21 %


def calcular_subtotal(carrito):
    """Suma precio x cantidad de cada producto del carrito."""
    total = 0
    for item in carrito:
        total += item["precio"] * item["cantidad"]
    return round(total, 2)


def calcular_descuento(subtotal, porcentaje):
    """Cuanto dinero se descuenta. Ej: 10 % de 1000 -> 100."""
    return round(subtotal * porcentaje / 100, 2)


def calcular_iva(neto):
    """IVA sobre el importe ya descontado."""
    return round(neto * IVA, 2)


def descuento_por_volumen(subtotal):
    """Porcentaje de descuento automatico segun cuanto se compra."""
    if subtotal >= 50000:
        return 10
    if subtotal >= 20000:
        return 5
    return 0


def calcular_totales(carrito, porcentaje_descuento=0):
    """
    Junta todas las cuentas en un diccionario:
    subtotal, descuento, neto, iva y total.
    """
    subtotal = calcular_subtotal(carrito)
    descuento = calcular_descuento(subtotal, porcentaje_descuento)
    neto = round(subtotal - descuento, 2)
    iva = calcular_iva(neto)
    return {
        "subtotal": subtotal,
        "porcentaje_descuento": porcentaje_descuento,
        "descuento": descuento,
        "neto": neto,
        "iva": iva,
        "total": round(neto + iva, 2),
    }
