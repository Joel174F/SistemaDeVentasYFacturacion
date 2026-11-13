"""
barra_menu.py  (COMPONENTE ARMADO)
El menu lateral. Esta hecho con varios botones juntos.
No decide que pantalla mostrar: solo AVISA cual se eligio.
"""
import tkinter as tk
import estilos


class BarraMenu(tk.Frame):
    def __init__(self, padre, opciones, al_elegir):
        """
        opciones: lista de tuplas (clave, texto). Ej: [("ventas", "Ventas")]
        al_elegir: funcion que se llama con la clave de la opcion elegida
        """
        super().__init__(padre, bg=estilos.COLORES["menu"], width=200)
        self.pack_propagate(False)   # mantiene el ancho fijo de 200 px

        self.al_elegir = al_elegir
        self.botones = {}            # diccionario: clave -> boton

        tk.Label(
            self, text="MI NEGOCIO",
            bg=estilos.COLORES["menu"], fg=estilos.COLORES["texto_claro"],
            font=estilos.FUENTES["titulo"],
        ).pack(pady=estilos.ESPACIOS["grande"])

        # Recorremos la lista y creamos un boton por cada opcion
        for clave, texto in opciones:
            boton = tk.Button(
                self, text=texto, anchor="w",
                bg=estilos.COLORES["menu"], fg=estilos.COLORES["texto_claro"],
                font=estilos.FUENTES["normal"],
                relief="flat", cursor="hand2",
                padx=estilos.ESPACIOS["grande"], pady=estilos.ESPACIOS["medio"],
                command=lambda c=clave: self.al_elegir(c),
            )
            boton.pack(fill="x")
            self.botones[clave] = boton

    def marcar_activo(self, clave):
        """Pinta de azul el boton de la pantalla actual y deja los otros normales."""
        for k, boton in self.botones.items():
            if k == clave:
                boton.config(bg=estilos.COLORES["menu_activo"])
            else:
                boton.config(bg=estilos.COLORES["menu"])
