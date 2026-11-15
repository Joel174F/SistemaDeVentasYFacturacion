
"""
logica_clientes.py
RESPONSABLE: Companiero C
Aca va la LOGICA de clientes.
"""
from funciones.archivos import leer_json, guardar_json, siguiente_codigo

ARCHIVO = "clientes.json"


def cargar_clientes():
    """Devuelve la lista de clientes guardados."""
    return leer_json(ARCHIVO)


def agregar_cliente(nombre, telefono, email):
    """Agrega un cliente nuevo."""

    if not nombre.strip():
        return False, "El nombre no puede estar vacio"

    if email and "@" not in email:
        return False, "El email no es valido"

    clientes = cargar_clientes()

    codigo = siguiente_codigo(clientes)

    cliente = {
        "codigo": codigo,
        "nombre": nombre,
        "telefono": telefono,
        "email": email
    }

    clientes.append(cliente)

    guardar_json(ARCHIVO, clientes)

    return True, "Cliente agregado correctamente"


def modificar_cliente(codigo, nombre, telefono, email):
    """Modifica los datos de un cliente."""

    if not nombre.strip():
        return False, "El nombre no puede estar vacio"

    if email and "@" not in email:
        return False, "El email no es valido"

    clientes = cargar_clientes()

    for cliente in clientes:
        if str(cliente["codigo"]) == str(codigo):

            cliente["nombre"] = nombre
            cliente["telefono"] = telefono
            cliente["email"] = email

            guardar_json(ARCHIVO, clientes)

            return True, "Cliente modificado correctamente"

    return False, "Cliente no encontrado"


def eliminar_cliente(codigo):
    """Elimina un cliente por su codigo."""

    clientes = cargar_clientes()

    nuevos_clientes = [
        cliente for cliente in clientes
        if str(cliente["codigo"]) != str(codigo)
    ]

    if len(clientes) == len(nuevos_clientes):
        return False, "Cliente no encontrado"

    guardar_json(ARCHIVO, nuevos_clientes)

    return True, "Cliente eliminado correctamente"


def buscar_cliente(texto):
    """Busca clientes por nombre sin importar mayusculas."""

    clientes = cargar_clientes()

    if not texto.strip():
        return clientes

    resultado = []

    for cliente in clientes:
        if texto.lower() in cliente["nombre"].lower():
            resultado.append(cliente)

    return resultado


def ventas_de_cliente(codigo):
    """Devuelve las ventas correspondientes a un cliente."""

    ventas = leer_json("ventas.json")

    resultado = []

    for venta in ventas:
        if str(venta.get("cliente_codigo")) == str(codigo):
            resultado.append(venta)

    return resultado
