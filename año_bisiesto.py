#!/usr/bin/env python
# -*- coding: utf-8 -*-
 
'''
Escriba una funcion es_bisiesto() 
que determine si un año determinado 
es un año bisiesto.Un año bisiesto 
es divisible por 4, pero no por 100.
'''


def es_bisiesto(ano):
	if ano%4 == 0:
		if ano%100 != 0:
			print("Es bisiesto")
	else:
		print("No es bisiesto")

ano = input("Escriba un año para saber si es bisiesto: ")
es_bisiesto(ano)