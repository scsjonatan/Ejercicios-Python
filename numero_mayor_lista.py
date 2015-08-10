
'''
Supongamos que tenemos mas de 3 números o 
no sabemos cuantos números son. Escribir 
una función max_in_list() que tome una lista 
de números y devuelva el mas grande.
'''

def max_in_list(lista):
	numero_mayor = lista[0]

	for numero in lista:
		if numero_mayor <= numero:
			numero_mayor = numero
		else:
			numero_mayor = numero_mayor
	print(numero_mayor)




lista = [0,7,3,1,5,6,3,2,4]

max_in_list(lista)
