#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
Definir una lista con un conjunto de nombres, 
imprimir la cantidad de comienzan con la letra a.
También se puede hacer elegir al usuario la letra a buscar.  (Un poco mas emocionante)
'''


nombres = []
for x in xrange(1,10):
	nombres.append(raw_input("Escribe un nombre: ").lower())

letra_buscada = raw_input("Qué letra buscas?: ")
cantidad = 0

for nombre in nombres:
	for letra in nombre:
		if letra == letra_buscada:
			cantidad = cantidad + 1
			break
		else:
			cantidad = cantidad
print cantidad