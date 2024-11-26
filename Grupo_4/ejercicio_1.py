#Construir un algoritmo que permita calcular el área de un
#triángulo, para lo cual debe solicitar la medida de la base y de la
#altura y mostrar el área calculada.

# Solicitar al usuario la medida de la base del triángulo
base = float(input("Ingrese la medida de la base del triángulo (en metros): "))

# Solicitar al usuario la medida de la altura del triángulo
altura = float(input("Ingrese la medida de la altura del triángulo (en metros): "))

# Calcular el área usando la fórmula del área de un triángulo: (base * altura) / 2
area = (base * altura) / 2

# Mostrar el resultado del cálculo del área
print(f"El área del triángulo es: {area:.2f} metros cuadrados")
