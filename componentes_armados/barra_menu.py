"""
barra_menu.py  (COMPONENTE ARMADO)
El menu lateral. No decide que pantalla mostrar: solo AVISA cual se eligio.
"""
import tkinter as tk
import estilos


class BarraMenu(tk.Frame):
    def __init__(self, padre, opciones, al_elegir):
        """
        opciones: lista de tuplas (clave, texto). Ej: [("ventas", "Ventas")]
        al_elegir: funcion que se llama con la clave de la opcion elegida
        """
        super().__init__(padre, bg=estilos.COLORES["menu"], width=230)
        self.pack_propagate(False)   # mantiene el ancho fijo

        self.al_elegir = al_elegir
        self.botones = {}            # diccionario: clave -> boton
        self.activo = None

        # Logo y nombre del negocio
        cabecera = tk.Frame(self, bg=estilos.COLORES["menu"])
        cabecera.pack(fill="x", pady=(28, 24))
        tk.Label(
            cabecera, text=estilos.ICONOS["logo"], bg=estilos.COLORES["menu"],
            fg=estilos.COLORES["texto_claro"], font=("Segoe UI", 30),
        ).pack()
        tk.Label(
            cabecera, text="MI NEGOCIO", bg=estilos.COLORES["menu"],
            fg=estilos.COLORES["texto_claro"], font=estilos.FUENTES["menu_titulo"],
        ).pack()
        tk.Label(
            cabecera, text="Sistema de Ventas", bg=estilos.COLORES["menu"],
            fg=estilos.COLORES["texto_menu"], font=estilos.FUENTES["chica"],
        ).pack()

        # Un boton por cada opcion de la lista
        for clave, texto in opciones:
            icono = estilos.ICONOS.get(clave, "")
            boton = tk.Button(
                self, text=f"  {icono}   {texto}", anchor="w",
                bg=estilos.COLORES["menu"], fg=estilos.COLORES["texto_claro"],
                activebackground=estilos.COLORES["menu_hover"],
                activeforeground=estilos.COLORES["texto_claro"],
                font=estilos.FUENTES["menu"], relief="flat", bd=0, cursor="hand2",
                padx=18, pady=12,
                command=lambda c=clave: self.al_elegir(c),
            )
            boton.pack(fill="x", padx=14, pady=3)
            boton.bind("<Enter>", lambda evento, c=clave: self._hover(c, True))
            boton.bind("<Leave>", lambda evento, c=clave: self._hover(c, False))
            self.botones[clave] = boton

        # Pie del menu
        pie = tk.Frame(self, bg=estilos.COLORES["menu"])
        pie.pack(side="bottom", fill="x", pady=24)
        tk.Label(
            pie, text=estilos.ICONOS["estadistica"], bg=estilos.COLORES["menu"],
            fg=estilos.COLORES["texto_menu"], font=("Segoe UI", 18),
        ).pack()
        tk.Label(
            pie, text="Tu negocio,\nmás organizado", bg=estilos.COLORES["menu"],
            fg=estilos.COLORES["texto_menu"], font=("Segoe UI", 10, "italic"),
        ).pack()

    def _hover(self, clave, dentro):
        """Resalta el boton al pasar el mouse (salvo el que ya esta activo)."""
        if clave == self.activo:
            return
        color = estilos.COLORES["menu_hover"] if dentro else estilos.COLORES["menu"]
        self.botones[clave].config(bg=color)

    def marcar_activo(self, clave):
        """Pinta de azul el boton de la pantalla actual y deja los otros normales."""
        self.activo = clave
        for k, boton in self.botones.items():
            if k == clave:
                boton.config(bg=estilos.COLORES["menu_activo"])
            else:
                boton.config(bg=estilos.COLORES["menu"])
