#Construir un algoritmo que permita calcular el área de un
#balón de basquetbol, para lo cual usted debe solicitar el valor
#del radio y mostrar el área del balón.

# Importamos la biblioteca 'math' para usar constantes y funciones matemáticas.
import math

# Mostramos un mensaje para que el usuario sepa qué hará el programa.
print("Este programa calcula el área de un balón de baloncesto.")

# Pedimos al usuario que ingrese el valor del radio del balón en centímetros.
# Usamos float para aceptar números con decimales.
radio = float(input("Por favor, ingrese el radio del balón en centímetros: "))

# Calculamos el área del balón.
# La fórmula para el área de una esfera es: 4 * π * radio^2
# Usamos math.pi para obtener el valor de π (pi).
area = 4 * math.pi * (radio ** 2)

# Mostramos el resultado al usuario, redondeado a 2 decimales para mayor claridad.
print(f"El área del balón de baloncesto es: {area:.2f} centímetros cuadrados.")
