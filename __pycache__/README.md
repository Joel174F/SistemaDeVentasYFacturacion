# Sistema de Ventas y Facturación

Este proyecto es un programa de escritorio para llevar las ventas de un comercio chico. Lo
hicimos con **Python** y **Tkinter** para practicar lo que vimos en clase: listas,
diccionarios, funciones, cálculos y archivos.

Con él se pueden cargar productos y clientes, armar el carrito de una venta, aplicarle un
descuento, registrarla y sacar el comprobante en TXT y en PDF. También tiene una sección de
reportes para ver cuánto se vendió y qué productos salen más.

Toda la información se guarda en archivos JSON, así que no hace falta instalar ninguna base de
datos.

## Cómo está organizado

```
Sistema_Ventas/
├── principal.py            # Abre el programa
├── ventana.py              # Ventana principal y cambio de pantallas
├── estilos.py              # Colores, fuentes e iconos
├── requirements.txt        # Librerías necesarias (fpdf2)
│
├── componentes_pequenos/   # Piezas básicas: botón, etiqueta, campo de texto
├── componentes_armados/    # Piezas combinadas: menú, tabla, tarjeta, formulario, encabezado
├── pantallas/              # Ventas, Productos, Clientes y Reportes
├── funciones/              # La lógica: cálculos, archivos, ventas, productos, clientes, reportes y PDF
├── datos/                  # Archivos JSON donde se guarda todo
└── comprobantes/           # Acá aparecen los comprobantes de cada venta
```

La idea fue separar **lo que se ve** de **lo que se calcula**. Las carpetas de componentes y
pantallas se encargan de la parte visual, y la carpeta `funciones` hace el trabajo de verdad.
Una pantalla nunca hace cuentas ni abre archivos por su cuenta: le pide a una función que lo
haga. Gracias a eso cada uno pudo trabajar en su parte sin romper la de los demás.

## Qué hace cada parte

**Para arrancar y darle estilo**
- `principal.py` abre el programa.
- `ventana.py` arma la ventana principal y cambia de pantalla cuando se elige una opción del menú.
- `estilos.py` guarda todos los colores y fuentes en un solo lugar. Si queremos cambiar el
  aspecto del sistema, tocamos solamente este archivo.

**Las piezas de la interfaz**
- En `componentes_pequenos` están las piezas más simples, como el botón, el texto y la caja
  donde se escribe. Se usan en todas las pantallas.
- En `componentes_armados` están las piezas que juntan varias de las anteriores: el menú
  lateral, la tabla, las tarjetas y los formularios.

**Las pantallas**
- **Ventas:** se elige un producto y un cliente, se arma el carrito, se aplica el descuento y
  se finaliza la venta.
- **Productos:** permite agregar, modificar y eliminar productos, con su precio y su stock.
- **Clientes:** lo mismo para los clientes, y además tiene un buscador por nombre.
- **Reportes:** muestra cuántas ventas hubo, el total facturado, las ventas por día y los
  productos más vendidos.

**La lógica (carpeta `funciones`)**
- `archivos.py` lee y guarda los archivos JSON.
- `calculos.py` hace las cuentas: subtotal, descuento, IVA y total.
- `logica_ventas.py` revisa que haya stock, lo descuenta, guarda la venta y crea los comprobantes.
- `comprobante_pdf.py` arma el comprobante en PDF con formato de factura.
- `logica_productos.py` y `logica_clientes.py` tienen las reglas y validaciones de cada módulo.
- `logica_reportes.py` calcula los números que se muestran en Reportes.

## Cómo funciona una venta

1. Elegimos un producto y la cantidad, y lo agregamos al carrito. El sistema controla que
   alcance el stock.
2. Elegimos el cliente y, si hace falta, escribimos un descuento.
3. Al finalizar, el sistema vuelve a verificar el stock, lo descuenta, guarda la venta en
   `datos/ventas.json` y genera el comprobante dentro de `comprobantes/`.

Para los números usamos estas reglas: hay un descuento automático del 5 % si la compra llega a
$20.000 y del 10 % si llega a $50.000. Si además se escribe un descuento a mano, se aplica el
que sea mayor (no se suman). Después se calcula el IVA del 21 % sobre el importe ya
descontado, y ese total es lo que paga el cliente.

## Conceptos que practicamos

- **Listas:** el carrito y los listados de productos, clientes y ventas.
- **Diccionarios:** cada producto, cliente y venta, y también los colores y fuentes.
- **Funciones:** toda la carpeta `funciones` y los métodos de cada pantalla.
- **Cálculos:** subtotales, descuentos, IVA y totales en `calculos.py`.
- **Archivos:** los JSON donde se guardan los datos y los comprobantes en TXT y PDF.