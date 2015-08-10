#!/usr/bin/env python
# -*- coding: utf-8 -*-
 

'''
Escribir una función filtrar_palabras()
 que tome una lista de palabras y un entero n, y devuelva las palabras que tengan mas de n caracteres. 
'''


def filtrar_palabras(lista, numero):
	array = []
	for palabra in lista:
		if len(palabra) >= numero:
			array.append(palabra)

	if len(array) == 0:
		print("Ninguna palabra :(")
	else:
		print(array)


lista = ["sa", "sfsaf", "dsfds", "idsids"]
numero = input("Escribe un numero: ")
filtrar_palabras(lista, numero)