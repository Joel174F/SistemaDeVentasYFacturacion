"""
prueba_componentes.py
Ventana de PRUEBA para ver los componentes nuevos funcionando.
Se ejecuta con:  python prueba_componentes.py
(No forma parte del sistema final: se puede borrar cuando ya no haga falta.)
"""
import tkinter as tk
import estilos
from componentes_pequenos.etiqueta import Etiqueta
from componentes_pequenos.boton import Boton
from componentes_armados.campo_formulario import CampoFormulario
from componentes_armados.tabla import Tabla
from funciones.archivos import leer_json, guardar_json, siguiente_codigo

ARCHIVO = "prueba.json"

ventana = tk.Tk()
ventana.title("Prueba de componentes")
ventana.geometry("800x450")
ventana.config(bg=estilos.COLORES["fondo"], padx=20, pady=20)

Etiqueta(ventana, "Prueba de componentes", "titulo").pack(fill="x")

# Formulario a la izquierda
izquierda = tk.Frame(ventana, bg=estilos.COLORES["fondo"])
izquierda.pack(side="left", fill="y", padx=(0, 20))

campo_nombre = CampoFormulario(izquierda, "Nombre")
campo_nombre.pack(fill="x")
campo_precio = CampoFormulario(izquierda, "Precio")
campo_precio.pack(fill="x")

# Tabla a la derecha
columnas = [("codigo", "Codigo", 70), ("nombre", "Nombre", 200), ("precio", "Precio", 90)]


def al_elegir_fila(fila):
    campo_nombre.escribir(fila["nombre"])
    campo_precio.escribir(fila["precio"])


tabla = Tabla(ventana, columnas, al_seleccionar=al_elegir_fila)
tabla.pack(side="right", fill="both", expand=True)


def agregar():
    lista = leer_json(ARCHIVO)
    lista.append({
        "codigo": siguiente_codigo(lista),
        "nombre": campo_nombre.obtener(),
        "precio": campo_precio.obtener(),
    })
    guardar_json(ARCHIVO, lista)
    tabla.cargar(lista)
    campo_nombre.limpiar()
    campo_precio.limpiar()


def borrar():
    fila = tabla.obtener_seleccion()
    if fila is None:
        return
    lista = [x for x in leer_json(ARCHIVO) if x["codigo"] != fila["codigo"]]
    guardar_json(ARCHIVO, lista)
    tabla.cargar(lista)


Boton(izquierda, "Agregar", agregar).pack(fill="x", pady=2)
Boton(izquierda, "Borrar", borrar, tipo="peligro").pack(fill="x", pady=2)

tabla.cargar(leer_json(ARCHIVO))   # al abrir, mostramos lo guardado
ventana.mainloop()
