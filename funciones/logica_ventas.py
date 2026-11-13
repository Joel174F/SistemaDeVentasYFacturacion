"""
logica_ventas.py
RESPONSABLE: Joel
La logica de registrar una venta (sin pantallas): revisar stock, descontar
stock, guardar la venta y generar el comprobante en texto.

Esta pantalla NO depende de los archivos de tus companieros: lee
productos.json y clientes.json directamente con archivos.py.

Cada venta se guarda como un diccionario:
    {"numero": 1, "fecha": "2026-11-10 15:30:00",
     "cliente_codigo": 2, "cliente_nombre": "Ana Gomez",
     "items": [ ...productos del carrito... ],
     "totales": {"subtotal": ..., "descuento": ..., "iva": ..., "total": ...}}
(El Companiero C usa "cliente_codigo" para buscar las compras de un cliente.)
"""
import os
from datetime import datetime
from funciones.archivos import leer_json, guardar_json
from funciones.calculos import calcular_totales

ARCHIVO_VENTAS = "ventas.json"
ARCHIVO_PRODUCTOS = "productos.json"
ARCHIVO_CLIENTES = "clientes.json"

CARPETA_COMPROBANTES = os.path.join(
    os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "comprobantes"
)


def listar_productos():
    return leer_json(ARCHIVO_PRODUCTOS)


def listar_clientes():
    return leer_json(ARCHIVO_CLIENTES)


def siguiente_numero(ventas):
    """Numero correlativo de la proxima venta (1, 2, 3...)."""
    if not ventas:
        return 1
    return max(v["numero"] for v in ventas) + 1


def hay_stock_suficiente(carrito, productos):
    """
    Revisa cada item del carrito contra el stock actual guardado.
    Devuelve (True, "") o (False, "mensaje con el problema").
    """
    for item in carrito:
        for producto in productos:
            if producto["codigo"] == item["codigo"]:
                if item["cantidad"] > producto["stock"]:
                    return False, (f"Stock insuficiente de '{item['nombre']}' "
                                   f"(disponible: {producto['stock']}).")
                break
        else:   # el for termino sin encontrar el producto
            return False, f"El producto '{item['nombre']}' ya no existe."
    return True, ""


def descontar_stock(carrito, productos):
    """Resta del stock lo vendido y guarda la lista de productos."""
    for item in carrito:
        for producto in productos:
            if producto["codigo"] == item["codigo"]:
                producto["stock"] -= item["cantidad"]
    guardar_json(ARCHIVO_PRODUCTOS, productos)


def generar_comprobante(venta):
    """Crea un .txt con el detalle de la venta y devuelve su ruta."""
    os.makedirs(CARPETA_COMPROBANTES, exist_ok=True)
    ruta = os.path.join(CARPETA_COMPROBANTES, f"comprobante_{venta['numero']:06d}.txt")
    t = venta["totales"]

    lineas = [
        "=" * 52,
        "            COMPROBANTE DE VENTA",
        "=" * 52,
        f"N°: {venta['numero']:06d}",
        f"Fecha: {venta['fecha']}",
        f"Cliente: {venta['cliente_nombre']}",
        "-" * 52,
        f"{'Producto':<22}{'Cant':>5}{'Precio':>11}{'Subtotal':>12}",
    ]
    for i in venta["items"]:
        lineas.append(f"{i['nombre']:<22}{i['cantidad']:>5}{i['precio']:>11.2f}{i['subtotal']:>12.2f}")
    lineas += [
        "-" * 52,
        f"{'Subtotal:':<40}{t['subtotal']:>12.2f}",
        f"{'Descuento (' + str(t['porcentaje_descuento']) + '%):':<40}{-t['descuento']:>12.2f}",
        f"{'Neto:':<40}{t['neto']:>12.2f}",
        f"{'IVA (21%):':<40}{t['iva']:>12.2f}",
        f"{'TOTAL:':<40}{t['total']:>12.2f}",
        "=" * 52,
        "        Gracias por su compra!",
    ]
    with open(ruta, "w", encoding="utf-8") as archivo:
        archivo.write("\n".join(lineas) + "\n")
    return ruta


def registrar_venta(carrito, cliente_codigo, cliente_nombre, porcentaje_descuento):
    """
    Registra la venta completa. Devuelve (ok, mensaje).
    Pasos: validar -> descontar stock -> guardar venta -> generar comprobante.
    """
    if not carrito:
        return False, "El carrito esta vacio."

    productos = listar_productos()
    hay, problema = hay_stock_suficiente(carrito, productos)
    if not hay:
        return False, problema

    ventas = leer_json(ARCHIVO_VENTAS)
    venta = {
        "numero": siguiente_numero(ventas),
        "fecha": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "cliente_codigo": cliente_codigo,
        "cliente_nombre": cliente_nombre,
        "items": list(carrito),
        "totales": calcular_totales(carrito, porcentaje_descuento),
    }

    descontar_stock(carrito, productos)
    ventas.append(venta)
    guardar_json(ARCHIVO_VENTAS, ventas)

    try:
        ruta = generar_comprobante(venta)
    except OSError:
        return True, f"Venta N° {venta['numero']:06d} registrada (no se pudo crear el comprobante)."

    return True, f"Venta N° {venta['numero']:06d} registrada.\nComprobante guardado en:\n{ruta}"
