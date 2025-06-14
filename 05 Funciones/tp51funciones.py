# -*- coding: utf-8 -*-
#tp51funciones.py

"""
####################################################################
####################################################################
1. Crear una función llamada imprimir_hola_mundo que imprima por
pantalla el mensaje: “Hola Mundo!”. Llamar a esta función desde el
programa principal
####################################################################
####################################################################
"""
def imprimir_hola_mundo():
    print("Hola Mundo!")

imprimir_hola_mundo()

"""
####################################################################
####################################################################
2. Crear una función llamada saludar_usuario(nombre) que reciba
como parámetro un nombre y devuelva un saludo personalizado.
Por ejemplo, si se llama con saludar_usuario("Marcos"), deberá devolver:
“Hola Marcos!”. Llamar a esta función desde el programa principal solicitando
el nombre al usuario.
####################################################################
####################################################################
"""
def saludar_usuario(nombre):
    return f"Hola {nombre}!"

nombre = input("Ingrese su nombre: ")
print(saludar_usuario(nombre))

"""
####################################################################
####################################################################
3. Crear una función llamada informacion_personal(nombre, apellido,
edad, residencia) que reciba cuatro parámetros e imprima: “Soy
[nombre] [apellido], tengo [edad] años y vivo en [residencia]”. Pedir los
datos al usuario y llamar a esta función con los valores ingresados.
####################################################################
####################################################################
"""
def informacion_personal(nombre, apellido, edad, residencia):
    return f"Soy {nombre} {apellido}, tengo {edad} años y vivo en {residencia}"

nombre, apellido = input("Ingrese su nombre y apellido: ").split()
edad = int(input("Ingrese su edad: "))
residencia = input("Ingrese su residencia: ")
print(informacion_personal(nombre, apellido, edad, residencia))

"""
####################################################################
####################################################################
4. Crear dos funciones: calcular_area_circulo(radio) que reciba el radio como
parámetro y devuelva el área del círculo. calcular_perimetro_circulo(radio) que
reciba el radio como parámetro y devuelva el perímetro del círculo. Solicitar
el radio al usuario y llamar ambas funciones para mostrar los resultados.
####################################################################
####################################################################
"""
def calcular_area_circulo(radio):
    return 3.14*(radio**2)

def calcular_perimetro_circulo(radio):
    return 2*3.14*radio

radio = float(input("Ingrese el radio del circulo: "))
print(radio)

"""
####################################################################
####################################################################
5. Crear una función llamada segundos_a_horas(segundos) que reciba
una cantidad de segundos como parámetro y devuelva la cantidad
de horas correspondientes. Solicitar al usuario los segundos y mostrar
el resultado usando esta función.
####################################################################
####################################################################
"""
def segundos_a_horas(segundos):
    return segundos/3600

seg_in = int(input("ingrese segundos para convertir a hs: "))
print(f"{seg_in} segundos son {segundos_a_horas(seg_in)} horas")

"""
####################################################################
####################################################################
6. Crear una función llamada tabla_multiplicar(numero) que reciba un
número como parámetro y imprima la tabla de multiplicar de ese
número del 1 al 10. Pedir al usuario el número y llamar a la función
####################################################################
####################################################################
"""
def tabla_multiplicar(numero):
    for i in range(10):
        print(f"\t{i}\tx\t{numero}\t=\t{(i)*numero}\n")


tabla_multiplicar(int(input("ingrese nro a multiplicar: ")))

"""
####################################################################
####################################################################
7. Crear una función llamada operaciones_basicas(a, b) que reciba
dos números como parámetros y devuelva una tupla con el resultado de sumarlos,
restarlos, multiplicarlos y dividirlos. Mostrar los resultados de forma clara.
####################################################################
####################################################################
"""
def operaciones_basicas(a, b):
    return (a+b, a-b, a*b, a/b if b != 0 else "no se puede dividir por 0")

num1 = int(input("ingrese primer numero de la operacion: "))
num2 = int(input("ingrese segundo numero de la operacion: "))
resultados = operaciones_basicas(num1, num2)

print(f"La suma entre {num1} y {num2} es {resultados[0]}")
print(f"La resta de {num1} y {num2} es {resultados[1]}")
print(f"La multiplicacion entre {num1} y {num2} es {resultados[2]}")
print(f"La division entre {num1} y {num2} es {resultados[3]}")

"""
####################################################################
####################################################################
8. Crear una función llamada calcular_imc(peso, altura) que reciba el
peso en kilogramos y la altura en metros, y devuelva el índice de
masa corporal (IMC). Solicitar al usuario los datos y llamar a la función para
mostrar el resultado con dos decimales.
####################################################################
####################################################################
"""
def calcular_imc(peso, altura):
    imc = peso/(altura**2)
    return imc

pe, al = float(input("ingreso peso: ")), float(input("ingresa altura: "))
print(f"Su IMC es: {calcular_imc(pe, al):.2f}")

"""
####################################################################
####################################################################
9. Crear una función llamada celsius_a_fahrenheit(celsius) que reciba
una temperatura en grados Celsius y devuelva su equivalente en
Fahrenheit. Pedir al usuario la temperatura en Celsius y mostrar el
resultado usando la función.
####################################################################
####################################################################
"""
def celsius_a_fahrenheit(celsius):
    return (celsius*9/5)+32

f = float(input("ingrese celsius (para convertir a farenheit): "))
print(f"{f} grados celsius equivale a {celsius_a_fahrenheit(f):.2f} farenheit")

"""
####################################################################
####################################################################
10.Crear una función llamada calcular_promedio(a, b, c) que reciba
tres números como parámetros y devuelva el promedio de ellos.
Solicitar los números al usuario y mostrar el resultado usando esta
función.
####################################################################
####################################################################
"""
def calcular_promedio(a, b, c):
    return (a+b+c)/3

notaa = float(input("ingrese primer nota: "))
notab = float(input("ingrese segunda nota: "))
notac = float(input("ingrese tercer nota: "))

print(f"el promedio entre {notaa}, {notab}, y {notac} es {calcular_promedio(notaa,notab,notac):.2f}")

