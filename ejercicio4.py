# -*- coding: utf-8 -*-
"""Ejercicio4

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1T50U6A3AurS-9Sp1ZEJODZjLfzUeHkOU

Instrucciones: Haga un programa en Python que lea un número mayor que 0 y despliegue todos sus
factores.
"""

#Se coloca un try para dar un mensaje en dado caso se ingrese una letra

try:
  numero = int(input("Ingrese un número: ")) #Se pide el ingreso de un número
  
  #Se asignan valores iniciales a las variables
  i = 1 
  texto = 0


  #Se crea el ciclo While para que repita mientras i sea menor o igual al número ingresado
  while i <= numero:
  
    #Se hace un primer condicional debido a que 1 es multiplo de todos los números y esto facilita el concatenado con la ","
    if i == 1:
      texto = str(i)
    else:
      
      #Aca se hace el otro condicional para que vaya concatenando los valores donde el residuo es 0, lo que quiere decir que es factor
      if numero%i == 0:
        texto = str(texto)+","+str(i) #Para concatenarlos se convierten los números a texto
    
    i = i+1 #Se suma 1 a nuestra variable i para que el ciclo While siga trabajando.

  #Al finalizar el ciclo While se muestran los valores que se concatenaron, es decir los factores. 

  print("Factores: {"+str(texto)+"}")

#Este es el mensaje a mostrar si en dado caso se ingresa una letra. 
except(ValueError):
  print("Error: Debe de ingresar un número")