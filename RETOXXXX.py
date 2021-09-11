# -*- coding: utf-8 -*-
"""
Created on Wed Jun 23 12:59:41 2021

@author: Miguel Angel Zapata
"""

codigo_morse =  {'/':' ' ,'.-': 'A', '-...':'B','-.-.': 'C', '-..':'D','.': 'E' ,
         '..-.':'F','--.': 'G', '....':'H', '..':'I','.---': 'J', '-.-':'K',
         '.-..':'L', '--': 'M', '-.':'N','---': 'O', '.--.': 'P','--.-': 'Q',
         '.-.': 'R', '...': 'S','-': 'T' , '..-': 'U','...-': 'V',  '.--':'W',
         '-..-':'X' ,'-.--':'Y' , '--..':'Z', }
def Trasncriptor(mensaje_creado):
    mensaje_traducido=""
    for libro in mensaje_creado.split():
        mensaje_traducido += codigo_morse[libro]
    return mensaje_traducido
mensaje_creado = input("ingrese su frase ")
print(Trasncriptor(mensaje_creado))
# mensaje_traducido = Trasncriptor(mensaje_creado)
# print(mensaje_traducido)
# codigo_morse =  {' ':'/' ,'A':'.-', 'B':'-...', 'C':'-.-.', 'D':'-..','E':'.' ,
#          'F':'..-.','G':'--.', 'H':'....', 'I':'..','J':'.---', 'K':'-.-',
#          'L':'.-..', 'M':'--', 'N':'-.','O':'---', 'P':'.--.','Q':'--.-',
#          'R':'.-.', 'S':'...','T':'-' , 'U':'..-','V':'...-',  'W':'.--',
#          'X':'-..-' ,'Y':'-.--' , 'Z':'--..', }