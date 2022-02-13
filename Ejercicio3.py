# -*- coding: utf-8 -*-
"""Untitled1.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1FhUxgknOei7EHBR-M23Tccax8L2wGr0m

Instrucciones: Haga un programa en Python que dados dos números ingresados por el usuario, el
primero mayor que el segundo, calcular y mostrar la suma de todos los números
comprendidos entre ambos.
"""

#Se coloca un Try para enviar un mensaje si se ingresan letras
try:

#Se solicitan los dos números:

  numero_mayor = int(input("Ingrese el número mayor: "))
  numero_menor = int(input("Ingrese el número menor: "))

#Se utiliza un if para validar si el primer dato ingresado es mayor al segundo, si cumple hace el for con la suma, de lo contrario arroja un mensaje de error.

  if numero_mayor > numero_menor:

    suma = 0  #Le asignamos 0 a la variable que guardará la suma para evitar que traiga otros valores de calculos previos

    for i in range(numero_menor, numero_mayor+1, 1): #Se utiliza un ciclo for para sumar desde el número menor al número mayor +1 (para incluir el número mayor), de 1 en 1
      suma = suma + i

  else:
    print("Error: El primer número debe de ser el mayor")

  if numero_mayor > numero_menor:  #Este if se usa para mostrar la suma solo si el primer número ingresado es mayor al segundo.
    print(suma)

except(ValueError):
  print("Error: Debe de ingresar números") #Mensaje que arrojará si el dato ingresado no es un número.