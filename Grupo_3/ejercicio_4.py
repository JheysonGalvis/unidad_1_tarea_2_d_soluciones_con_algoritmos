#Construir un algoritmo que permita calcular la velocidad a la cual
#se desplaza un vehículo, para lo cual se debe solicitar el valor
#de la distancia y el valor del tiempo.

# Solicitar al usuario el valor de la distancia recorrida
distancia = float(input("Ingrese la distancia recorrida (en metros): "))

# Solicitar al usuario el valor del tiempo que tardó en recorrer esa distancia
tiempo = float(input("Ingrese el tiempo transcurrido (en segundos): "))

# Calcular la velocidad usando la fórmula: velocidad = distancia / tiempo
velocidad = distancia / tiempo

# Mostrar el resultado de la velocidad
print(f"La velocidad del vehículo es: {velocidad:.2f} metros por segundo")
