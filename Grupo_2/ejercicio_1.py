#Calcular el área de una caja de forma rectangular, para lo cual
#debe solicitar la base y la altura (las cuales son en centímetros)
#y retornar el área

# Solicitar al usuario que ingrese la base de la caja en centímetros
# Usamos input() para pedir datos al usuario y convertimos la entrada a un número flotante (float)
base = float(input("Ingrese la base de la caja en centímetros: "))

# Solicitar al usuario que ingrese la altura de la caja en centímetros
# También convertimos la entrada a un número flotante (float)
altura = float(input("Ingrese la altura de la caja en centímetros: "))

# Calcular el área de la caja
# El área de un rectángulo se calcula con la fórmula: área = base * altura
area = base * altura

# Mostrar el resultado del cálculo
# Usamos print() para mostrar el área en centímetros cuadrados (cm²)
print(f"El área de la caja es: {area} cm².")

