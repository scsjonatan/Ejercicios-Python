'''
Crear una función contar_vocales(),
que reciba una palabra y cuente 
cuantas letras "a" tiene, cuantas letras "e" tiene 
y así hasta completar todas las vocales.
Se puede hacer que el usuario sea quien elija la palabra.
'''

def contar_vocales(palabra):
	palabra_min = palabra.lower()
	cant_a = 0
	cant_e = 0
	cant_i = 0
	cant_o = 0
	cant_u = 0
	
	for letra in palabra_min:
		if letra == "a":
			cant_a = cant_a + 1
		elif letra == "e":
			cant_e = cant_e + 1
		elif letra == "i":
			cant_i = cant_i + 1
		elif letra == "o":
			cant_o = cant_o + 1
		elif letra == "u":
			cant_u = cant_u + 1		

	print("Hay "+ str(cant_a)+ " a")
	print("Hay "+ str(cant_e)+ " e")
	print("Hay "+ str(cant_i)+ " i")
	print("Hay "+ str(cant_o)+ " o")
	print("Hay "+ str(cant_u)+ " u")



palabra = raw_input("Escribe una palabra: ")
contar_vocales(palabra)	