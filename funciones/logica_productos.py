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


def agregar_producto(nombre, precio, stock):
    """
    Valida los datos y agrega un producto nuevo.
    Pasos sugeridos:
      1. Verificar que el nombre no este vacio.
      2. Convertir precio a float y stock a int (usar try/except ValueError).
      3. Verificar que precio y stock no sean negativos.
      4. Leer la lista, agregar el diccionario (codigo con siguiente_codigo) y guardar.
    """
    return False, "Falta implementar: agregar_producto"


def modificar_producto(codigo, nombre, precio, stock):
    """
    Cambia los datos del producto con ese codigo.
    Pasos sugeridos: validar igual que al agregar, buscar el producto en la
    lista por su codigo, actualizar sus campos y guardar.
    """
    return False, "Falta implementar: modificar_producto"


def eliminar_producto(codigo):
    """
    Elimina el producto con ese codigo.
    Pista: armar una lista nueva con todos los productos menos ese y guardarla.
    """
    return False, "Falta implementar: eliminar_producto"
