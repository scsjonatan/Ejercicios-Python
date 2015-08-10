'''
Definir una tupla con 10 edades de personas. 
Imprimir la cantidad de personas con edades superiores a 20.
Puedes variar el ejercicio para que sea el usuario 
quien ingrese las edades.
'''

tupla = (23,23,46,3,2,54,23,34,24,64)

array = []

for x in xrange(1,11):
	array.append(input("Escribe una edad: "))



cantidad = 0
for elemento in array:
	if elemento >= 20:
		cantidad = cantidad + 1
	else:
		cantidad = cantidad
print(cantidad)