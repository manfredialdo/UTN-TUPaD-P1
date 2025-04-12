# -*- coding: utf-8 -*-
"""
manfredi_tp03.py

tecnicatura universitaria en programacion 
#TECNICATURA UNIVERSITARIA
#EN PROGRAMACIÓN
# utn
#Práctico 3: Estructuras condicionales
#Alumno Manfredi Aldo Dario



"""

input('''
1) Escribir un programa que solicite la edad del usuario. Si el usuario es
mayor de 18 a¤os, deber  mostrar un mensaje en pantalla que diga ?Es mayor de edad?.
'''
)
"es mayor" if int(input("ingrese edad: "))>=18 else "es menor"

input('''
2) Escribir un programa que solicite su nota al usuario. Si la nota es mayor o igual a 6, deber  mostrar por pantalla un mensaje que diga ?Aprobado?; en caso contrario deber  mostrar el mensaje ?Desaprobado?.
'''
)
print("aprobado") if int(input("ingrese nota del alumno: "))>=6 else print("desaprobado")

input('''
3) Escribir un programa que permita ingresar solo n£meros pares. Si el usuario ingresa un n£mero par, imprimir por en pantalla el mensaje "Ha ingresado un n£mero par"; en caso contrario, imprimir por pantalla "Por favor, ingrese un n£mero par". Nota: investigar el uso del operador de m¢dulo (%) en Python para evaluar si un n£mero es par o impar.
''')
while True: print("Ha ingresado un número par") if int(input("Ingrese un número par: ")) % 2 == 0 else (print("Por favor, ingrese un número par"), exit())

input('''
4) Escribir un programa que solicite al usuario su edad e imprima por pantalla a cu l de las siguientes categor¡as pertenece:
? Ni¤o/a: menor de 12 a¤os.
? Adolescente: mayor o igual que 12 a¤os y menor que 18 a¤os.
? Adulto/a joven: mayor o igual que 18 a¤os y menor que 30 a¤os.
? Adulto/a: mayor o igual que 30 a¤os.
''')
edad = int(input("ingrese edad: "))

if edad < 12 and edad >= 0:
    print("Ni¤o/a: menor de 12 a¤os.")

elif edad >= 12 and edad < 18:
    print("Adolescente: mayor o igual que 12 a¤os y menor que 18 a¤os.")

elif edad >= 18 and edad < 30:
    print("Adulto/a joven: mayor o igual que 18 a¤os y menor que 30 a¤os.")

elif edad >= 30:
    print("Adulto/a: mayor o igual que 30 a¤os.")

else:
    print("hubo algun error")
input('''
5) Escribir un programa que permita introducir contrase¤as de entre 8 y 14 caracteres (incluyendo 8 y 14). Si el usuario ingresa una contrase¤a de longitud adecuada, imprimir por en pantalla el mensaje "Ha ingresado una contrase¤a correcta"; en caso contrario, imprimir por pantalla "Por favor, ingrese una contrase¤a de entre 8 y 14 caracteres". Nota: investigue el uso de la funci¢n len() en Python para evaluar la cantidad de elementos que tiene un iterable tal como una lista o un string.
''')
print("Ha ingresado una contrase¤a correcta") if 15>=len(input("ingrese contraseña: "))=<8 else print("Por favor, ingrese una contrasea de entre 8 y 14 caracteres")

input('''
6) El paquete statistics de python contiene funciones que permiten tomar una lista de n£meros y calcular la moda, la mediana y la media de dichos n£meros. Un ejemplo de su uso es el siguiente:

En la documentaci¢n oficial se puede encontrar m s informaci¢n sobre este paquete: https://docs.python.org/es/3.8/library/statistics.html.
La moda (mode), la mediana (median) y la media (mean) son par metros estad¡sticos que se pueden utilizar para predecir la forma de una distribuci¢n normal a partir del siguiente criterio:
? Sesgo positivo o a la derecha: cuando la media es mayor que la mediana y, a su vez, la mediana es mayor que la moda.
? Sesgo negativo o a la izquierda: cuando la media es menor que la mediana y, a su vez, la mediana es menor que la moda.
? Sin sesgo: cuando la media, la mediana y la moda son iguales.
Teniendo en cuenta lo antes mencionado, escribir un programa que tome la lista numeros_aleatorios, calcule su moda, su mediana y su media y las compare para determinar si hay sesgo positivo, negativo o no hay sesgo. Imprimir el resultado por pantalla.
Definir la lista numeros_aleatorios de la siguiente forma:
Nota: el bloque de c¢digo anterior crea una lista con 50 n£meros entre 1 y 100 elegidos de forma aleatoria.
''')
from statistics import mode
from statistics import median
from statistics import mean
import random
numeros_aleatorios = [random.randint(1, 100) for i in range(50)]
print(numeros_aleatorios)

print("la moda es ", mode(numeros_aleatorios))
print("la mediana es ", median(numeros_aleatorios))
print("la media es ", mean(numeros_aleatorios))
if mean(numeros_aleatorios)>median(numeros_aleatorios) and median(numeros_aleatorios)>mode(numeros_aleatorios):
    print("Sesgo positivo o a la derecha: La media es mayor que la mediana y, a su vez, la mediana es mayor que la moda.")

elif mean(numeros_aleatorios)>median(numeros_aleatorios)<median(numeros_aleatorios) and median(numeros_aleatorios)<mode(numeros_aleatorios):
    print("? Sesgo negativo o a la izquierda: cuando la media es menor que la mediana y, a su vez, la mediana es menor que la moda.")

elif mean(numeros_aleatorios)==median(numeros_aleatorios) and median(numeros_aleatorios)==mode(numeros_aleatorios):
    print("? Sin sesgo: cuando la media, la mediana y la moda son iguales.")

input('''
7) Escribir un programa que solicite una frase o palabra al usuario. Si el string ingresado termina con vocal, a¤adir un signo de exclamaci¢n al final e imprimir el string resultante por pantalla; en caso contrario, dejar el string tal cual lo ingres¢ el usuario e imprimirlo por pantalla.
''')
cadena = input("ingrese una frase o palabra: ")
print(cadena, "!") if cadena[-1::] == "a" or cadena[-1::] == "e" or cadena[-1::] == "i" or cadena[-1::] == "o" or cadena[-1::] == "u" else print(cadena)

input('''
8) Escribir un programa que solicite al usuario que ingrese su nombre y el n£mero 1, 2 o 3 dependiendo de la opci¢n que desee:
1. Si quiere su nombre en may£sculas. Por ejemplo: PEDRO.
2. Si quiere su nombre en min£sculas. Por ejemplo: pedro.
3. Si quiere su nombre con la primera letra may£scula. Por ejemplo: Pedro.
El programa debe transformar el nombre ingresado de acuerdo a la opci¢n seleccionada por el usuario e imprimir el resultado por pantalla. Nota: investigue uso de las funciones upper(), lower() y title() de Python para convertir entre may£sculas y min£sculas.
''')
nombre = input("por favor, ingrese nombre: ")

print("""
1. Si quiere su nombre en may£sculas.
2. Si quiere su nombre en min£sculas.
3. Si quiere su nombre con la primera letra may£scula..
""")

opcion = int(input("por favor, ingrese opcion: "))
if opcion == 1:
    print(cadena.upper())

elif opcion == 2:
    print(cadena.lower())

elif opcion == 3:
    print(cadena.title())
else:
    print("opcion incorrecta")

input('''
9) Escribir un programa que pida al usuario la magnitud de un terremoto, clasifique la magnitud en una de las siguientes categor¡as seg£n la escala de Richter e imprima el resultado por pantalla:
? Menor que 3: "Muy leve" (imperceptible).
? Mayor o igual que 3 y menor que 4: "Leve" (ligeramente perceptible).
? Mayor o igual que 4	y menor que 5: "Moderado" (sentido por personas, pero generalmente no causa da¤os).
? Mayor o igual que 5 y menor que 6: "Fuerte" (puede causar da¤os en estructuras d‚biles).
? Mayor o igual que 6 y menor que 7: "Muy Fuerte" (puede causar da¤os significativos).
? Mayor o igual que 7: "Extremo" (puede causar graves da¤os a gran escala).
''')
magitud = int(input("ingrese la magnitud del terremoto: "))

if magitud < 3:
    print("? Menor que 3: Muy leve (imperceptible).")

elif magitud >= 3 and magitud <4:
    print("? Mayor o igual que 3 y menor que 4: 'Leve' (ligeramente perceptible).")

elif magitud >= 4 and magitud <5:
    print("? Mayor o igual que 4	y menor que 5: 'Moderado' (sentido por personas, pero generalmente no causa da¤os).")

elif magitud >= 5 and magitud <6:
    print("? Mayor o igual que 5 y menor que 6: 'Fuerte' (puede causar da¤os en estructuras d‚biles).")

elif magitud >= 6 and magitud <7:
    print("? Mayor o igual que 6 y menor que 7: 'Muy Fuerte' (puede causar da¤os significativos).")

elif magitud >= 7:
    print("? Mayor o igual que 7: 'Extremo' (puede causar graves da¤os a gran escala).")


input('''
10) Utilizando la informaci¢n aportada en la siguiente tabla sobre las estaciones del a¤o

Periodo del a¤o
 Estaci¢n en el hemisferio norte
Estaci¢n en el hemisferio sur
Desde el 21 de diciembre hasta el 20 de marzo (incluidos)
Invierno
Verano
Desde el 21 de marzo hasta el 20 de junio (incluidos)
Primavera
Oto¤o
Desde el 21 de junio hasta el 20 de septiembre (incluidos)
Verano
Invierno
Desde el 21 de septiembre hasta el 20 de diciembre (incluidos)
Oto¤o
Primavera
Escribir un programa que pregunte al usuario en cu l hemisferio
se encuentra (N/S), qu‚ mes del a¤o es y qu‚ d¡a es.
El programa deber  utilizar esa informaci¢n para imprimir por pantalla si
el usuario se encuentra en oto¤o, invierno, primavera o verano.
''')




