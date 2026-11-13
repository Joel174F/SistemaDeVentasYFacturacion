"""
principal.py
Este es el archivo que se ejecuta para abrir el programa:
    python principal.py
"""
from ventana import Ventana

if __name__ == "__main__":
    app = Ventana()
    app.mainloop()   # mantiene la ventana abierta esperando clicks
