"""Elabore un algoritmo que solicite un numero de dos 
digitos y que devuelva como salida el numero invertido. 
Por ejemplo, si el usuario ingresa 23, el programa deberá 
mostrar 32. """

#entrada 23
#salida = El inverso de 23 es 32

numero= int(input ("Ingrese cualquier número: "))
numero1 = str (numero)[::-1]
print ("El inverso de", numero, "es: ", numero1)


