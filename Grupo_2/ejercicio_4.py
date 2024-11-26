#Construir un algoritmo que permita calcular las cesantías de un
#empleado. Para esto, usted debe solicitar la cantidad de días
#laborados y el valor del salario y calcular las cesantías con esta
#fórmula:
#Cesantías= (días laborados * salario)/360

# Solicitar al usuario la cantidad de días laborados por el empleado
dias_laborados = int(input("Ingrese la cantidad de días laborados por el empleado: "))

# Solicitar al usuario el valor del salario mensual del empleado
salario = float(input("Ingrese el valor del salario mensual del empleado (en pesos): "))

# Calcular las cesantías usando la fórmula
# Cesantías = (días laborados * salario) / 360
cesantias = (dias_laborados * salario) / 360

# Mostrar el resultado: el valor de las cesantías
print(f"El valor de las cesantías es: {cesantias:.2f} pesos")
