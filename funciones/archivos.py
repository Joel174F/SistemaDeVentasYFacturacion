"""
archivos.py
Funciones para leer y guardar los datos en archivos JSON.
Todos usan ESTAS funciones, asi nadie escribe su propio codigo de archivos.

Ejemplo:
    productos = leer_json("productos.json")      # devuelve una lista
    productos.append({"codigo": 1, "nombre": "Yerba"})
    guardar_json("productos.json", productos)
"""
import json
import os

# Carpeta "datos", ubicada al lado de la carpeta "funciones"
CARPETA_DATOS = os.path.join(
    os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "datos"
)


def leer_json(nombre_archivo):
    """
    Lee un archivo de la carpeta datos y devuelve su contenido (una lista).
    Si el archivo no existe o esta danado, devuelve una lista vacia.
    """
    ruta = os.path.join(CARPETA_DATOS, nombre_archivo)
    if not os.path.exists(ruta):
        return []
    try:
        with open(ruta, "r", encoding="utf-8") as archivo:
            return json.load(archivo)
    except (json.JSONDecodeError, OSError):
        return []


def guardar_json(nombre_archivo, datos):
    """Guarda una lista en un archivo de la carpeta datos."""
    os.makedirs(CARPETA_DATOS, exist_ok=True)
    ruta = os.path.join(CARPETA_DATOS, nombre_archivo)
    with open(ruta, "w", encoding="utf-8") as archivo:
        json.dump(datos, archivo, indent=2, ensure_ascii=False)


def siguiente_codigo(lista):
    """Devuelve el proximo codigo libre para una lista de diccionarios."""
    if not lista:
        return 1
    return max(item["codigo"] for item in lista) + 1
