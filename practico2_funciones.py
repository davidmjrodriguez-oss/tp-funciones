# Punto 1

def imprimir_hola_mundo():
    print("Hola Mundo!")

# Punto 2

def saludar_usuario(nombre):
    return f"Hola {nombre}!"

nombre_usuario = input("Ingrese su nombre: ")
saludo = saludar_usuario(nombre_usuario)
print(saludo)

# Punto 3
def informacion_personal(nombre, apellido, edad, residencia):
    print(f"Soy {nombre} {apellido}, tengo {edad} años y vivo en {residencia}.")

nombre = input("Ingrese su nombre: ")
apellido = input("Ingrese su apellido: ")
edad = input("Ingrese su edad: ")
residencia = input("Ingrese su lugar de residencia: ")

informacion_personal(nombre, apellido, edad, residencia)

# Punto 4
import math  # Importamos la librería math para usar el valor de pi

def calcular_area_circulo(radio):
    return math.pi * (radio ** 2)

def calcular_perimetro_circulo(radio):
    return 2 * math.pi * radio

radio = float(input("Ingrese el radio del círculo: "))

area = calcular_area_circulo(radio)
perimetro = calcular_perimetro_circulo(radio)

print(f"El área del círculo es: {area:.2f}")
print(f"El perímetro del círculo es: {perimetro:.2f}")

# Punto 5
def segundos_a_horas(segundos):
    horas = segundos / 3600
    return horas

segundos = float(input("Ingrese la cantidad de segundos: "))
resultado = segundos_a_horas(segundos)
print(f"{segundos} segundos equivalen a {resultado:.2f} horas.")

# Punto 6
def tabla_multiplicar(numero):
    print(f"\nTabla de multiplicar del {numero}:")
    for i in range(1, 11):
        print(f"{numero} x {i} = {numero * i}")

numero = int(input("Ingrese un número para ver su tabla de multiplicar: "))
tabla_multiplicar(numero)

# Punto 7
def operaciones_basicas(a, b):
    suma = a + b
    resta = a - b
    multiplicacion = a * b
    division = a / b if b != 0 else "No se puede dividir por cero"
    return (suma, resta, multiplicacion, division)

a = float(input("Ingrese el primer número: "))
b = float(input("Ingrese el segundo número: "))

resultados = operaciones_basicas(a, b)

print(f"Suma: {resultados[0]}")
print(f"Resta: {resultados[1]}")
print(f"Multiplicación: {resultados[2]}")
print(f"División: {resultados[3]}")

# Punto 8
def calcular_imc(peso, altura):
    imc = peso / (altura ** 2)
    return imc

peso = float(input("Ingrese su peso en kilogramos: "))
altura = float(input("Ingrese su altura en metros: "))

imc = calcular_imc(peso, altura)
print(f"Su índice de masa corporal (IMC) es: {imc:.2f}")

# Punto 9
def celsius_a_fahrenheit(celsius):
    fahrenheit = (celsius * 9/5) + 32
    return fahrenheit

celsius = float(input("Ingrese la temperatura en grados Celsius: "))
resultado = celsius_a_fahrenheit(celsius)
print(f"{celsius}°C equivalen a {resultado:.2f}°F")

# Punto 10
def calcular_promedio(a, b, c):
    promedio = (a + b + c) / 3
    return promedio

a = float(input("Ingrese el primer número: "))
b = float(input("Ingrese el segundo número: "))
c = float(input("Ingrese el tercer número: "))

resultado = calcular_promedio(a, b, c)
print(f"El promedio de los tres números es: {resultado:.2f}")
