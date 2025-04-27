# -*- coding: utf-8 -*-

"""
manfredi-tp05.py



tecnicatura universitaria en programacion
#TECNICATURA UNIVERSITARIA
#EN PROGRAMACIÓN
#Materia: Programacion 1
#Práctico 5: Listas
#Alumno Manfredi Aldo Dario
"""

"""
################################################################################
Actividades
1) Crear una lista con los números del 1 al 100 que sean múltiplos de 4. Utilizar la función
range.
################################################################################
"""
print([i for i in range(100) if i % 4 == 0])

'''################################################################################
2) Crear una lista con cinco elementos (colocar los elementos que más te gusten) y mostrar el
penúltimo. ¡Puedes hacerlo como se muestra en los videos o bien investigar cómo funciona el
indexing con números negativos!
################################################################################'''
colores = ["rojo", "azul", "blanco", "negro", "gris"]
print(colores[-2])

'''################################################################################
3) Crear una lista vacía, agregar tres palabras con append e imprimir la lista resultante por
pantalla. Pista: para crear una lista vacía debes colocar los corchetes sin nada en su interior. Por
ejemplo:
lista_vacia = []
################################################################################'''
lista_vacia = []
lista_vacia.append("palabra1")
lista_vacia.append("palabra2")
lista_vacia.append("palabra3")
print(lista_vacia)

'''################################################################################
4) Reemplazar el segundo y último valor de la lista “animales” con las palabras “loro” y “oso”,
respectivamente. Imprimir la lista resultante por pantalla. ¡Puedes hacerlo como se muestra
en los videos o bien investigar cómo funciona el indexing con números negativos!
animales = ["perro", "gato", "conejo", "pez"]
################################################################################'''
animales = ["flamenco", "puma", "tero", "liebre", "zorrino"]
animales[0] = "loro"
animales[-1] = "oso"
print(animales)

'''################################################################################
5) Analizar el siguiente programa y explicar con tus palabras qué es lo que realiza.
numeros = [8, 15, 3, 22, 7]
numeros.remove(max(numeros))
print(numeros)
################################################################################'''
numeros = [8, 15, 3, 22, 7] # crea una lista de ocho numeros

numeros.remove(max(numeros)) # elimina(remove) el numero maximo(nax) de la lista(numeros)
print(numeros) # imprime en pantalla la nueva lista de numeros

'''################################################################################
6) Crear una lista con números del 10 al 30 (incluído), haciendo saltos de 5 en 5 y mostrar por
pantalla los dos primeros.
################################################################################'''
num = [i for i in range(10, 31) if i % 5 == 0]
print(num[:2])

'''################################################################################
7) Reemplazar los dos valores centrales (índices 1 y 2) de la lista “autos” por dos nuevos valores
cualesquiera.
autos = ["sedan", "polo", "suran", "gol"]
################################################################################'''
autos = ["sedan", "polo", "suran", "gol"]
autos[1], autos[2] = "fiat", "pick up"
print(autos)

'''################################################################################
8) Crear una lista vacía llamada "dobles" y agregar el doble de 5, 10 y 15 usando append
directamente. Imprimir la lista resultante por pantalla.
################################################################################'''
dobles = []
dobles.append(5*2)
dobles.append(10*2)
dobles.append(15*2)
print(dobles)


'''################################################################################
9) Dada la lista “compras”, cuyos elementos representan los productos comprados por
diferentes clientes:
compras = [["pan", "leche"], ["arroz", "fideos", "salsa"],["agua"]]
a) Agregar "jugo" a la lista del tercer cliente usando append.
b) Reemplazar "fideos" por "tallarines" en la lista del segundo cliente.
c) Eliminar "pan" de la lista del primer cliente.
d) Imprimir la lista resultante por pantalla

################################################################################'''

compras = [["pan", "leche"], ["arroz", "fideos", "salsa"],["agua"]]
# a) Agregar "jugo" a la lista del tercer cliente usando append.
#print(compras)
compras[2].append("jugo")
#print(compras)
compras[1][1] = ("tallarines")
#print(compras)
compras[0].remove("pan")
print(compras)

'''################################################################################
10) Elaborar una lista anidada llamada “lista_anidada” que contenga los siguientes elementos:
● Posición lista_anidada[0]: 15
● Posición lista_anidada[1]: True
● Posición lista_anidada[2][0]: 25.5
● Posición lista_anidada[2][1]: 57.9
● Posición lista_anidada[2][2]: 30.6
● Posición lista_anidada[3]: False
Imprimir la lista resultante por pantalla.
'''
lista_anidada = []
lista_anidada.append(15)
lista_anidada.append(True)
lista_anidada.append([25.5, 57.9, 30.6])
lista_anidada.append(False)
print(lista_anidada)
