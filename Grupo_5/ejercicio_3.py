#Construir un algoritmo que permita calcular el área de una
#piscina de forma circular, solicitando el valor del radio y
#mostrando el área

# Importamos la biblioteca math para usar el valor de pi.
import math

# Mostramos un mensaje inicial para que el usuario sepa qué hace el programa.
print("Este programa calcula el área de una piscina circular.")

# Solicitamos al usuario que ingrese el radio de la piscina.
# Usamos float para permitir números con decimales.
radio = float(input("Por favor, ingrese el radio de la piscina (en metros): "))

# Calculamos el área de la piscina usando la fórmula del área de un círculo: A = π * r^2
# Usamos math.pi para obtener un valor preciso de π.
area = math.pi * (radio ** 2)

# Mostramos el área calculada, redondeada a 2 decimales para mayor claridad.
print(f"El área de la piscina es: {area:.2f} metros cuadrados.")
