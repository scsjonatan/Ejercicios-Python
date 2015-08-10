#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
Escribir un pequeño programa donde:
- Se ingresa el año en curso.
- Se ingresa el nombre y el año de nacimiento de tres personas.
- Se calcula cuántos años cumplirán durante el año en curso.
- Se imprime en pantalla.
'''


ano_curso = input("Escribe el ano en curso: ")
nombre_uno = raw_input("Primer nombre: ")
ano_uno = input("Primer ano: ")
nombre_dos = raw_input("Segundo nombre: ")
ano_dos = input("Segundo ano: ")
nombre_tres = raw_input("Tercer nombre: ")
ano_tres = input("Tercer ano: ")

cumple_uno = ano_curso - ano_uno
cumple_dos = ano_curso - ano_dos
cumple_tres = ano_curso - ano_tres

print(nombre_uno + " cumplira " + str(cumple_uno))
print(nombre_dos + " cumplira " + str(cumple_dos))
print(nombre_tres + " cumplira "+ str(cumple_tres))