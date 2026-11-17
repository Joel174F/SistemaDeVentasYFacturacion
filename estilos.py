"""
estilos.py
Aca viven TODOS los colores, fuentes, iconos y tamanios del sistema.
Si queres cambiar el aspecto de la aplicacion, solo tocas este archivo.
"""

COLORES = {
    "fondo": "#F3F6FC",          # fondo general
    "blanco": "#FFFFFF",         # tarjetas
    "fondo_suave": "#E8F0FD",    # panel de descuento y totales
    "borde": "#DCE4F2",          # bordes de tarjetas, tablas y campos
    "menu": "#172746",           # azul oscuro (menu lateral, encabezados de tabla)
    "menu_activo": "#2878F0",    # opcion del menu seleccionada
    "menu_hover": "#243A63",     # opcion del menu al pasar el mouse
    "texto": "#172746",
    "texto_suave": "#6B7A99",    # subtitulos y textos secundarios
    "texto_claro": "#FFFFFF",    # texto sobre fondos oscuros
    "texto_menu": "#B8C4DD",
    "primario": "#2878F0",       # botones principales
    "primario_hover": "#1D63D1",
    "exito": "#16B978",          # confirmar venta
    "exito_hover": "#119962",
    "peligro": "#EF4444",        # eliminar / quitar
    "peligro_hover": "#DC2626",
}

FUENTES = {
    "titulo": ("Segoe UI", 20, "bold"),
    "normal": ("Segoe UI", 11),
    "boton": ("Segoe UI", 11, "bold"),
    "subtitulo": ("Segoe UI", 11),
    "tarjeta": ("Segoe UI", 13, "bold"),
    "menu": ("Segoe UI", 12),
    "menu_titulo": ("Segoe UI", 18, "bold"),
    "chica": ("Segoe UI", 9),
    "total": ("Segoe UI", 20, "bold"),
}

ESPACIOS = {
    "chico": 5,
    "medio": 10,
    "grande": 20,
}

# Iconos (simbolos de texto). Si alguno se ve como un cuadrado en tu
# computadora, cambialo por "" y desaparece sin romper nada.
ICONOS = {
    "logo": "🛒",
    "ventas": "🛒",
    "productos": "📦",
    "clientes": "👥",
    "cliente": "👤",
    "estadistica": "📊",
    "quitar": "🗑",
    "ok": "✔",
    "buscar": "🔍",
    "agregar": "➕",
    "reportes": "📈",
}


def fondo_de(widget):
    """Devuelve el color de fondo de un widget (para que los hijos lo hereden)."""
    try:
        return widget.cget("bg")
    except Exception:
        return COLORES["fondo"]
