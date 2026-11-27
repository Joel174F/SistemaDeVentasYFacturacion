"""
logica_productos.py
RESPONSABLE: Companiero B
Aca va la LOGICA de productos (sin pantallas): validar, agregar, modificar
y eliminar. La pantalla (pantalla_productos.py) llama a estas funciones.

Cada producto es un diccionario:
    {"codigo": 1, "nombre": "Yerba", "precio": 3500.0, "stock": 50}

Los productos se guardan en datos/productos.json con las funciones de archivos.py.

REGLA: las funciones que modifican datos devuelven una tupla (ok, mensaje):
    return True, "Producto agregado"
    return False, "El precio debe ser un numero"
Asi la pantalla sabe si salio bien y que mensaje mostrar.

COMO TRABAJAR: reemplaza cada "return False, 'Falta implementar...'" por tu codigo,
una funcion por vez, y proba con la pantalla.
"""
from funciones.archivos import leer_json, guardar_json, siguiente_codigo

ARCHIVO = "productos.json"


def cargar_productos():
    """Devuelve la lista de productos guardados. (YA ESTA HECHA)"""
    return leer_json(ARCHIVO)


def validar_datos(nombre, precio, stock):
    """
    Revisa nombre, precio y stock (la usan agregar y modificar).
    Devuelve (ok, mensaje, nombre, precio, stock) con los valores ya convertidos.
    """
    # 1. El nombre no puede estar vacio
    nombre = str(nombre).strip()
    if nombre == "":
        return False, "El nombre no puede estar vacío", nombre, 0.0, 0

    # 2. Convertir precio a float y stock a int
    try:
        precio = float(str(precio).strip().replace(",","."))
    except ValueError:
        return False, "El precio debe ser un número", nombre, 0.0, 0

    try:
        stock = int(stock)
    except ValueError:
        return False, "El stock debe ser un número entero", nombre, precio, 0

    # 3. No pueden ser negativos
    if precio < 0:
        return False, "El precio no puede ser negativo", nombre, precio, stock
    if stock < 0:
        return False, "El stock no puede ser negativo", nombre, precio, stock

    return True, "", nombre, precio, stock


def agregar_producto(nombre, precio, stock):
    """Valida los datos y agrega un producto nuevo."""
    ok, mensaje, nombre, precio, stock = validar_datos(nombre, precio, stock)
    if not ok:
        return False, mensaje

    # 4. Leer la lista, agregar el diccionario y guardar
    productos = cargar_productos()
    nuevo = {
        "codigo": siguiente_codigo(productos),
        "nombre": nombre,
        "precio": precio,
        "stock": stock,
    }
    productos.append(nuevo)
    guardar_json(ARCHIVO, productos)
    return True, "Producto agregado"


def modificar_producto(codigo, nombre, precio, stock):
    """Cambia los datos del producto con ese codigo."""
    ok, mensaje, nombre, precio, stock = validar_datos(nombre, precio, stock)
    if not ok:
        return False, mensaje

    # El codigo puede llegar como texto desde la pantalla
    try:
        codigo = int(codigo)
    except ValueError:
        return False, "El código no es válido"

    productos = cargar_productos()
    for producto in productos:
        if producto["codigo"] == codigo:
            producto["nombre"] = nombre
            producto["precio"] = precio
            producto["stock"] = stock
            guardar_json(ARCHIVO, productos)
            return True, "Producto modificado"

    return False, "Producto no encontrado"


def eliminar_producto(codigo):
    """Elimina el producto con ese codigo."""
    try:
        codigo = int(codigo)
    except ValueError:
        return False, "El código no es válido"

    productos = cargar_productos()

    # Lista nueva con todos los productos menos el que se quiere borrar
    nueva_lista = []
    for producto in productos:
        if producto["codigo"] != codigo:
            nueva_lista.append(producto)

    if len(nueva_lista) == len(productos):
        return False, "Producto no encontrado"

    guardar_json(ARCHIVO, nueva_lista)
    return True, "Producto eliminado"