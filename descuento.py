'''
 Este programa pide primeramente la cantidad total de compras de una persona. 
 Si la cantidad es inferior a 100.00,elprogramadiráqueelclientenoaplicaalapromoción.
 Pero si la persona ingresa una cantidad en compras igual o superior a 100.00, 
 el programa genera de forma aleatoria un número entero del cero al cinco. 
 Cada número corresponderá a un color diferente de cinco colores de bolas 
 que hay para determinar el descuento que el cliente recibirá como premio. 
 
 Si la bola aleatoria es color blanco, no hay descuento, pero si es uno de 
 los otros cuatro colores, sí se aplicará un descuento determinado 
 según la tabla que  aparecerá, y ese descuento se aplicará sobre el total de 
 compra que introdujo inicialmente el usuario, de manera que el programa mostrará 
 un nuevo valor a pagar luego de haber aplicado el descuento.
'''

import random
x = 0 
while x == 0:

	cantidad_compra = input("Introduzca la cantidad total de la compra: ")
	if cantidad_compra >= 100:

		descuentos = [1, .9, .8, .75, .5]
		descuento = descuentos[random.randint(0, 4)]
		nuevo_precio = cantidad_compra * descuento
		print ("Tienes un descuento de " +  str(100 - descuento*100) + " porciento de descuento, total a pagar: ")
		print(nuevo_precio)

	else:
		print("Tienes que hacer una compra de 100 pesos o mas para aplicar al descuento: ")
	x = input("1 para salir o 0 para seguir: ")