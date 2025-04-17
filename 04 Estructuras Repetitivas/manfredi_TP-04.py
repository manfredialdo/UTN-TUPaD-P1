# TECNICATURA UNIVERSITARIA #EN PROGRAMACIÓN
# UTN
# Práctico 4: Estructuras condicionales
# Manfredi Aldo Dario


input('''1) Crea un programa que imprima en pantalla todos los números enteros desde 0 hasta 100
(incluyendo ambos extremos), en orden creciente, mostrando un número por línea.''')
for i in range(101):
    print(i)

input('''2) Desarrolla un programa que solicite al usuario un número entero y determine la cantidad de
dígitos que contiene.''')
a, b = "el numero ingresado contiene", "numeros"
print(a, len(str(int(input("ingrese numero: ")))), b)

input('''3) Escribe un programa que sume todos los números enteros comprendidos entre dos valores
dados por el usuario, excluyendo esos dos valores.''')
valor1, valor2 = int(input("Ingrese el primer valor: ")), int(input("Ingrese el segundo valor: "))
total = 0

inicio = valor1 + 1 if valor1 < valor2 else valor2 + 1
fin = valor2 if valor1 < valor2 else valor1

for i in range(inicio, fin):
    total += i

print(f"La suma de los números enteros entre {min(valor1, valor2)} y {max(valor1, valor2)} es: {total}")

input('''4) Elabora un programa que permita al usuario ingresar números enteros y los sume en
secuencia. El programa debe detenerse y mostrar el total acumulado cuando el usuario ingrese un 0.''')
total, num = 0, int(input("Ingrese un entero (0 para finalizar): "))
while num != 0:
    total += num
    num = int(input("Ingrese otro entero (0 para finalizar): "))
print(f"Total acumulado: {total}")

input('''5) Crea un juego en el que el usuario deba adivinar un número aleatorio entre 0 y 9. Al final, el
programa debe mostrar cuántos intentos fueron necesarios para acertar el número.''')
from random import randint
alea, ingresado, intentos = randint(0, 9), -1, 0

print("ingrese un número entre 0 y 9.")
while ingresado != alea:
    ingresado = int(input("Ingresa tu número: "))
    intentos += 1
print(f"Bien.. es el número ({alea}) y fue resuelto en {intentos} intentos.")

input('''6) Desarrolla un programa que imprima en pantalla todos los números pares comprendidos
entre 0 y 100, en orden decreciente.''')
for num in range(100, -1, -2):
    print(num)

input('''7) Crea un programa que calcule la suma de todos los números comprendidos entre 0 y un
número entero positivo indicado por el usuario.''')
total = 0
for num in range(int(input("ingrese un numero positivo: "))+1):
    total += num
print(f"el total es {total}")

input('''8) Escribe un programa que permita al usuario ingresar 100 números enteros. Luego, el
programa debe indicar cuántos de estos números son pares, cuántos son impares, cuántos son
negativos y cuántos son positivos. (Nota: para probar el programa puedes usar una cantidad
menor, pero debe estar preparado para procesar 100 números con un solo cambio).''')
par, impar, positivo, negativo = 0, 0, 0, 0
for i in range(100):
    num = int(input("por favor ingrese numero entero: "))
    par += 1 if num % 2 == 0 else 0
    impar += 1 if num % 2 != 0 else 0
    negativo += 1 if num < 0 else 0
    positivo += 1 if num >= 0 else 0

print(f"usted ha ingresado {par} numeros pares, {impar} numeros impares, {positivo} numeros positivos, {negativo} numeros negativos, ")

input('''9) Elabora un programa que permita al usuario ingresar 100 números enteros y luego calcule la
media de esos valores. (Nota: puedes probar el programa con una cantidad menor, pero debe
poder procesar 100 números cambiando solo un valor).''')
cantidad_num = 100  # valor modificable
suma = 0

for i in range(cantidad_num):
    num = int(input(f"Ingrese el número {i + 1}: "))
    suma += num

print(f"\nLa media de los {cantidad_num} números ingresados es: {suma / cantidad_num}") if cantidad_num > 0 else print("No se ingresaron números para calcular la media.")

input('''10) Escribe un programa que invierta el orden de los dígitos de un número ingresado por el
usuario. Ejemplo: si el usuario ingresa 547, el programa debe mostrar 745.''')
num = int(str(int(input("ingrese un numero: ")))[::-1])
print(f"el orden invertido del numero ingresado es {num}")