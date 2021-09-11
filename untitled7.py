from vector import vector
import random
import math

"""Esta funcion invierte un número, osea, 3456 invertido sería 6543"""
def invierteNumero(n): 
    nunu = 0
    m = n
    while m > 0:
        digito = m % 10
        nunu = nunu * 10 + digito
        m = m // 10
    return nunu
    
"""Esta función retorna el primer digito de el número x"""
def comienzaCon(x):
    pd = x
    while pd > 9:
        pd = pd // 10
    return pd

"""Funcion que contiene la solución al problema que será calificado"""
def solucion():
    """Se genera aleatoriamente un número entero entre 15 y 30"""
    n = random.randint(15,30)
    
    
   