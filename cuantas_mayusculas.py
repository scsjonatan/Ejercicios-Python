#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
Escribir un programa que le diga al 
usuario que ingrese una cadena. 
El programa tiene que evaluar la cadena 
y decir cuantas letras mayúsculas tiene. 
'''
frase = "Hola Como Estas Jonatan"
cantidad = 0

for letra in frase:
	letrita = letra.lower()
	if letra == letrita:
		cantidad = cantidad
	else:
		cantidad = cantidad + 1
print cantidad	