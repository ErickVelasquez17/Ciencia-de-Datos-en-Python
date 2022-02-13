# -*- coding: utf-8 -*-
"""Ejercicio2

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1YNXhF1xQDqldpyB0r6HzGAxVY1K4UW0n
"""



"""Instrucciones: Haga un programa en Python que permita el ingreso de las calificaciones de una
evaluación del curso de Ciencia de Datos en Python, el programa debe desplegar un
mensaje en función de la nota ingresada. Además de eso si la calificación es reprobada
ósea menor a 71, se debe calcular la diferencia entre la nota de aprobación y la calificación
ingresada.
"""

try:  #utilizamos un try para dar un mensaje en dado caso no ingresen números. 

  nota = round(float(input("Ingrese la califiación: ")),0)  # En esta parte solicitamos la calificación, si es decimal que este se redondee. 

  if nota < 0:   #Con esto enviamos un msj de alerta si el número es menor a 0
    print("Nota no valida, debe de ser entre 0 y 100.")
  
#Aca usamos las condicionales para enviar el mensaje y la nota faltante según la califiación:

  elif nota < 50:
    puntos_faltantes = 71-nota
    print("Insuficiente")
    print(f"Faltaron {puntos_faltantes} para aprobar.")
  elif nota <= 60:
    puntos_faltantes = 71-nota
    print("Regular")
    print(f"Faltaron {puntos_faltantes} para aprobar.")
  elif nota <= 70:
    puntos_faltantes = 71-nota
    print("Bien")
    print(f"Faltaron {puntos_faltantes} para aprobar.")
  elif nota <= 90:
    print("Muy Bien")
  elif nota <= 100:
    print("Sobresaliente")
  else:
    print("Nota no valida, debe de ser entre 0 y 100.")  #Con esto enviamos un msj de alerta si el número es mayor a 100
except(ValueError):
  print("Los datos no son validos, debe de ser un número.")