#Fernando desea calcular el consumo de combustible por
#kilómetro realizado en su motocicleta mediante un algoritmo,
#para lo cual se debe pedir la cantidad de kilómetros recorridos
#y la cantidad de litros de combustible que consumió y calcular
#el consumo por kilómetro. Ejemplo
#Kilómetros=300,
#litros consumidos=12
#consumo por kilómetro=25

# Mostramos un mensaje inicial que explica lo que hace el programa.
print("Este programa calcula el consumo de combustible por kilómetro de tu motocicleta.")

# Pedimos al usuario que ingrese la cantidad de kilómetros recorridos.
# Convertimos el valor ingresado a tipo float para permitir decimales.
kilometros = float(input("Ingresa la cantidad de kilómetros recorridos: "))

# Pedimos al usuario que ingrese la cantidad de litros de combustible consumidos.
# También lo convertimos a float para permitir números decimales.
litros = float(input("Ingresa la cantidad de litros de combustible consumidos: "))

# Calculamos el consumo por kilómetro dividiendo los kilómetros recorridos entre los litros consumidos.
consumo_por_km = kilometros / litros

# Mostramos el resultado del consumo por kilómetro, redondeado a 2 decimales para mayor claridad.
print(f"El consumo de combustible por kilómetro es: {consumo_por_km:.2f} kilómetros por litro.")
