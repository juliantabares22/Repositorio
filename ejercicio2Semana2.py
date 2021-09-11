"""Elabore un programa en Python que lea un entero de dos 
dígitos y produzca como salida los dígitos del número leído 
con su correspondiente mensaje. Por ejemplo, si el número leído 
es 27, la salida deberá ser:(sin texto adicional):
2
7"""

entero = int (input(" Ingrese un número de dos digitos: "))
for digito in str(entero):
    print(digito)



