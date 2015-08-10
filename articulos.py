'''
De la galería de productos, el usuario introducirá el código 
y el número de unidades del producto que desea comprar. 
El programa determinará el total a pagar, como una factura.
Una variante a este ejercicio que lo haría un poco más complejo 
sería dar la posibilidad de seguir ingresando diferentes códigos de 
productos con sus respectivas cantidades, y cuando el usuario desee 
terminar el cálculo de la factura completa con todas sus compras. Te animas??
'''

print("Elija el producto deseado: ")
print("Producto\t\t\tCodigo")
print("Camisa\t\t\t\t  1")
print("Pantalon\t\t\t  2")
print("Falda\t\t\t\t  3")

cuenta = []
precios = [100, 120, 100]

comprando = 0
while comprando == 0:
	codigo = input("Introduzca el codigo del articulo: ")
	cantidad = input("Introduzca la cantidad de articulos: ")
	cuenta.append((precios[codigo-1])* cantidad)

	comprando = input("Para agregar otro articulo 0 para salir 1: ")
precio_total = 0
for precios in cuenta:
	precio_total = precio_total + precios


print("El precio total a pagar es de " + str(precio_total))
