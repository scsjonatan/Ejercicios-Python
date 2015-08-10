#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
Escribe un programa que pida dos palabras y diga si riman o no. 
Si coinciden las tres últimas letras tiene que decir que riman.
Si coinciden sólo las dos últimas tiene que decir que riman un poco y si no, que no riman.
'''

palabra_uno = raw_input("Escribe una palabra: ")
palabra_dos = raw_input("Escribe otra palabra: ")

array_uno = []
array_dos = []

for x in xrange(1, 4):
	letra_uno = palabra_uno[(len(palabra_uno)-x)]
	array_uno.append(letra_uno)

for x in xrange(1, 4):
	letra_dos = palabra_dos[(len(palabra_dos)-x)]
	array_dos.append(letra_dos)


if array_uno[0] == array_dos[0]:
	if array_uno[1] == array_dos[1]:
		if array_uno[2] == array_dos[2]:
			print("Riman")
		else:
			print("Riman un poco")
	else:
		print("No riman")
else:
	print("No riman")