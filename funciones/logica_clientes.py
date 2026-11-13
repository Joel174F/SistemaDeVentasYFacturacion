"""
logica_clientes.py
RESPONSABLE: Companiero C
Aca va la LOGICA de clientes (sin pantallas): validar, agregar, modificar,
eliminar y buscar. La pantalla (pantalla_clientes.py) llama a estas funciones.

Cada cliente es un diccionario:
    {"codigo": 1, "nombre": "Ana", "telefono": "555-1234", "email": "ana@mail.com"}

Los clientes se guardan en datos/clientes.json con las funciones de archivos.py.

REGLA: las funciones que modifican datos devuelven una tupla (ok, mensaje):
    return True, "Cliente agregado"
    return False, "El nombre no puede estar vacio"

COMO TRABAJAR: reemplaza cada "return False, 'Falta implementar...'" por tu codigo,
una funcion por vez, y proba con la pantalla.
"""
from funciones.archivos import leer_json, guardar_json, siguiente_codigo

ARCHIVO = "clientes.json"


def cargar_clientes():
    """Devuelve la lista de clientes guardados. (YA ESTA HECHA)"""
    return leer_json(ARCHIVO)


def agregar_cliente(nombre, telefono, email):
    """
    Valida los datos y agrega un cliente nuevo.
    Pasos sugeridos:
      1. Verificar que el nombre no este vacio.
      2. Verificar que el email contenga "@" (si lo escribieron).
      3. Leer la lista, agregar el diccionario (codigo con siguiente_codigo) y guardar.
    """
    return False, "Falta implementar: agregar_cliente"


def modificar_cliente(codigo, nombre, telefono, email):
    """Cambia los datos del cliente con ese codigo (validar igual que al agregar)."""
    return False, "Falta implementar: modificar_cliente"


def eliminar_cliente(codigo):
    """Elimina el cliente con ese codigo."""
    return False, "Falta implementar: eliminar_cliente"


def buscar_cliente(texto):
    """
    Devuelve la lista de clientes cuyo nombre CONTIENE el texto
    (sin importar mayusculas). Si el texto esta vacio, devuelve todos.
    Pista: usar texto.lower() in cliente["nombre"].lower()
    """
    return cargar_clientes()   # por ahora devuelve todos; C lo mejora


def ventas_de_cliente(codigo):
    """
    Devuelve la lista de ventas de ese cliente, leyendo datos/ventas.json.
    Cada venta (la arma Joel) tiene esta forma:
        {"numero": 1, "fecha": "2026-11-10 15:30", "cliente_codigo": 2,
         "items": [...], "totales": {"total": 8750.0, ...}}
    Pista: recorrer las ventas y quedarse con las que tengan ese cliente_codigo.
    """
    return []
