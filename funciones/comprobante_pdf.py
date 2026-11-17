"""
comprobante_pdf.py
RESPONSABLE: Joel
Genera el comprobante de una venta en PDF, con formato de factura simple.
Usa la libreria fpdf2 (se instala con:  pip install fpdf2).
Recibe la venta (diccionario) y la ruta donde guardar el archivo.
"""
from fpdf import FPDF

# Colores en formato RGB (rojo, verde, azul)
AZUL_OSCURO = (23, 39, 70)
AZUL = (40, 120, 240)
GRIS = (107, 122, 153)
CLARO = (243, 246, 252)
BLANCO = (255, 255, 255)

ANCHOS = [90, 25, 30, 35]            # ancho de cada columna (suman 180 mm)
ALINEACIONES = ["L", "C", "R", "R"]  # izquierda, centro, derecha, derecha


def _texto(valor):
    """El PDF usa una fuente basica: cambia por '?' lo que no pueda mostrar."""
    return str(valor).encode("latin-1", "replace").decode("latin-1")


def _dinero(valor):
    """1234.5 -> '$ 1.234,50' (formato argentino)."""
    texto = f"{valor:,.2f}"
    texto = texto.replace(",", "X").replace(".", ",").replace("X", ".")
    return "$ " + texto


def generar_comprobante_pdf(venta, ruta):
    pdf = FPDF(format="A4")
    pdf.set_auto_page_break(auto=True, margin=15)
    pdf.set_margins(15, 15, 15)
    pdf.c_margin = 2.5               # espacio interno de cada celda
    pdf.add_page()

    # --- Banda superior con el nombre del negocio ---
    pdf.set_fill_color(*AZUL_OSCURO)
    pdf.rect(0, 0, 210, 38, style="F")
    pdf.set_text_color(*BLANCO)
    pdf.set_font("Helvetica", "B", 22)
    pdf.set_xy(15, 10)
    pdf.cell(100, 10, "MI NEGOCIO")
    pdf.set_font("Helvetica", "", 10)
    pdf.set_xy(15, 21)
    pdf.cell(100, 6, "Sistema de Ventas y Facturacion")

    pdf.set_font("Helvetica", "B", 14)
    pdf.set_xy(95, 10)
    pdf.cell(100, 8, "COMPROBANTE DE VENTA", align="R")
    pdf.set_font("Helvetica", "", 10)
    pdf.set_xy(95, 20)
    pdf.cell(100, 6, _texto(f"N° {venta['numero']:06d}"), align="R")
    pdf.set_xy(95, 26)
    pdf.cell(100, 6, _texto(f"Fecha: {venta['fecha']}"), align="R")

    # --- Datos del cliente ---
    pdf.set_text_color(*AZUL_OSCURO)
    pdf.set_xy(15, 46)
    pdf.set_font("Helvetica", "B", 11)
    pdf.cell(22, 7, "Cliente:")
    pdf.set_font("Helvetica", "", 11)
    pdf.cell(0, 7, _texto(venta["cliente_nombre"]))
    pdf.ln(14)

    # --- Encabezado de la tabla de productos ---
    pdf.set_fill_color(*AZUL_OSCURO)
    pdf.set_text_color(*BLANCO)
    pdf.set_font("Helvetica", "B", 10)
    titulos = ["Producto", "Cant.", "Precio", "Subtotal"]
    for ancho, titulo, alineacion in zip(ANCHOS, titulos, ALINEACIONES):
        pdf.cell(ancho, 9, titulo, fill=True, align=alineacion)
    pdf.ln(9)

    # --- Una fila por cada producto (con color alternado) ---
    pdf.set_text_color(*AZUL_OSCURO)
    pdf.set_font("Helvetica", "", 10)
    pdf.set_fill_color(*CLARO)
    for numero, item in enumerate(venta["items"]):
        con_fondo = numero % 2 == 1
        valores = [
            item["nombre"][:45],
            str(item["cantidad"]),
            _dinero(item["precio"]),
            _dinero(item["subtotal"]),
        ]
        for ancho, valor, alineacion in zip(ANCHOS, valores, ALINEACIONES):
            pdf.cell(ancho, 8, _texto(valor), fill=con_fondo, align=alineacion)
        pdf.ln(8)

    pdf.set_draw_color(*GRIS)
    pdf.line(15, pdf.get_y() + 1, 195, pdf.get_y() + 1)
    pdf.ln(6)

    # --- Totales ---
    t = venta["totales"]
    pdf.set_font("Helvetica", "", 11)
    filas = [
        ("Subtotal", _dinero(t["subtotal"])),
        (f"Descuento ({t['porcentaje_descuento']:g}%)", "- " + _dinero(t["descuento"])),
        ("Neto", _dinero(t["neto"])),
        ("IVA (21%)", _dinero(t["iva"])),
    ]
    for etiqueta, valor in filas:
        pdf.cell(130, 8, _texto(etiqueta), align="R")
        pdf.cell(50, 8, _texto(valor), align="R")
        pdf.ln(8)

    pdf.ln(2)
    pdf.set_fill_color(*AZUL)
    pdf.set_text_color(*BLANCO)
    pdf.set_font("Helvetica", "B", 14)
    pdf.cell(130, 12, "TOTAL", fill=True, align="R")
    pdf.cell(50, 12, _texto(_dinero(t["total"])), fill=True, align="R")
    pdf.ln(20)

    # --- Pie ---
    pdf.set_text_color(*GRIS)
    pdf.set_font("Helvetica", "I", 10)
    pdf.cell(0, 8, "Gracias por su compra!", align="C")

    pdf.output(ruta)
    return ruta
