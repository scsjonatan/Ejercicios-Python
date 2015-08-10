#!/usr/bin/env python
# -*- coding: utf-8 -*-
 

cantidad_dolares = input("Ingresa una cantidad de dolares: ")
tasa_interes = input("Ingresa la tasa de interes: ")
numero_anos = input("Ingresa el total de anos: ")


capital_final = float((cantidad_dolares * (1 + pow(numero_anos, tasa_interes/100))))
print(capital_final)