"""
estilos.py
Aca viven TODOS los colores, fuentes y tamanios del sistema.
Si queres cambiar el aspecto de la aplicacion, solo tocas este archivo.
"""

# Diccionario de colores: nombre -> codigo hexadecimal
COLORES = {
    "fondo": "#F4F6FA",          # fondo general de la ventana
    "menu": "#1F2A44",           # fondo del menu lateral
    "menu_activo": "#3B82F6",    # boton del menu seleccionado
    "menu_hover": "#2C3A5E",     # boton del menu cuando pasas el mouse
    "texto": "#1F2A44",          # texto principal
    "texto_claro": "#FFFFFF",    # texto sobre fondos oscuros
    "primario": "#3B82F6",       # botones principales
    "primario_hover": "#2563EB",
    "peligro": "#EF4444",        # botones de borrar
    "peligro_hover": "#DC2626",
}

# Fuentes: (tipo de letra, tamanio, estilo)
FUENTES = {
    "titulo": ("Segoe UI", 20, "bold"),
    "normal": ("Segoe UI", 11),
    "boton": ("Segoe UI", 11, "bold"),
}

# Espacios (en pixeles) para que todo quede alineado igual
ESPACIOS = {
    "chico": 5,
    "medio": 10,
    "grande": 20,
}
