
"""
logica_clientes.py
RESPONSABLE: Companiero C
Logica de gestion de clientes.
"""

from funciones.archivos import leer_json, guardar_json, siguiente_codigo

ARCHIVO = "clientes.json"


def cargar_clientes():
    """Devuelve todos los clientes guardados."""
    return leer_json(ARCHIVO)


def verificar_duplicado(clientes, telefono, email, codigo_excluir=None):
    """Verifica si el telefono o email ya pertenecen a otro cliente."""

    telefono = telefono.strip()
    email = email.strip().lower()

    for cliente in clientes:

        if codigo_excluir is not None:
            if str(cliente.get("codigo")) == str(codigo_excluir):
                continue

        telefono_existente = str(cliente.get("telefono", "")).strip()
        email_existente = str(cliente.get("email", "")).strip().lower()

        if telefono == telefono_existente:
            return "Ya existe un cliente con ese telefono"

        if email == email_existente:
            return "Ya existe un cliente con ese email"

    return None


def validar_datos(nombre, telefono, email):
    """Valida que todos los campos sean obligatorios."""

    nombre = nombre.strip()
    telefono = telefono.strip()
    email = email.strip()

    if not nombre:
        return False, "El nombre es obligatorio"

    if not telefono:
        return False, "El telefono es obligatorio"

    if not email:
        return False, "El email es obligatorio"

    if "@" not in email:
        return False, "El email no es valido"

    return True, "Datos correctos"


def agregar_cliente(nombre, telefono, email):
    """Registra un cliente nuevo."""

    nombre = nombre.strip()
    telefono = telefono.strip()
    email = email.strip()

    # Validar los campos obligatorios.
    ok, mensaje = validar_datos(nombre, telefono, email)

    if not ok:
        return False, mensaje

    clientes = cargar_clientes()

    # Verificar datos duplicados.
    error = verificar_duplicado(clientes, telefono, email)

    if error:
        return False, error

    # Generar clave primaria.
    codigo = siguiente_codigo(clientes)

    # Comprobar que el codigo no exista.
    for cliente in clientes:
        if str(cliente.get("codigo")) == str(codigo):
            return False, "Error: el codigo del cliente ya existe"

    # Crear cliente.
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
    """Modifica los datos de un cliente existente."""

    nombre = nombre.strip()
    telefono = telefono.strip()
    email = email.strip()

    # Validar los campos obligatorios.
    ok, mensaje = validar_datos(nombre, telefono, email)

    if not ok:
        return False, mensaje

    clientes = cargar_clientes()

    # Buscar cliente por su clave primaria.
    for cliente in clientes:

        if str(cliente.get("codigo")) == str(codigo):

            # Comprobar datos duplicados.
            error = verificar_duplicado(
                clientes,
                telefono,
                email,
                codigo_excluir=codigo
            )

            if error:
                return False, error

            # Actualizar informacion.
            cliente["nombre"] = nombre
            cliente["telefono"] = telefono
            cliente["email"] = email

            guardar_json(ARCHIVO, clientes)

            return True, "Cliente modificado correctamente"

    return False, "Cliente no encontrado"


def eliminar_cliente(codigo):
    """Elimina un cliente utilizando su clave primaria."""

    clientes = cargar_clientes()

    nuevos_clientes = [
        cliente for cliente in clientes
        if str(cliente.get("codigo")) != str(codigo)
    ]

    if len(clientes) == len(nuevos_clientes):
        return False, "Cliente no encontrado"

    guardar_json(ARCHIVO, nuevos_clientes)

    return True, "Cliente eliminado correctamente"


def buscar_cliente(texto):
    """Busca clientes por nombre sin importar mayusculas."""

    clientes = cargar_clientes()

    texto = texto.strip().lower()

    if not texto:
        return clientes

    resultado = []

    for cliente in clientes:
        nombre = cliente.get("nombre", "").lower()

        if texto in nombre:
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

