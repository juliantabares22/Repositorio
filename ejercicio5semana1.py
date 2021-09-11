#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon May 31 17:09:36 2021

@author: julian
"""

numero= int(input ("Ingrese cualquier número: "))
segundo_digito = numero % 10
primer_digito = numero//10
print ("El inverso es: ", segundo_digito, primer_digito, sep= "")


