

"""Elabore un algoritmo que lea el nombre de una persona, 
la estatura (en cm) y el peso (en kg) y que muestre los 
datos leidos y la relacion estatura peso 
(IMC: Indice de masa corporal) cuya formula es: """

estatura= float (input ("Ingrese su estatura en cm: "))
peso= float (input ("Ingrese su peso en kilogramos: "))
estatura =estatura/100
imc= (peso/estatura**2)
print ("El índice de masa corporal IMC es: ", imc)