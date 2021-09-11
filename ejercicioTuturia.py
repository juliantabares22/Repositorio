#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jun  2 20:14:02 2021

@author: julian
"""

"""Elabore un algoritmo que cuente la cantidad X 
de letras en un parrafo"""

letra = input ("Ingrese la letra que desea contar: ")
parrafo = input ("Ingrese el texto: ")
acum = 0
acum1 = 0

for i in parrafo: 
    acum1 += 1
    if (letra == (i or i.lower())):
        acum = acum + 1 
        
print ("En este texto la letra", letra, "Se encuentra", acum, "veces y el total de letras en el parrafo es", acum1)
        















#range es solo para enteros

