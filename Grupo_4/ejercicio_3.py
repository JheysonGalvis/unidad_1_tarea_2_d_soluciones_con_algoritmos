#Construir un algoritmo que permita calcular el pago de un
#trabajador semanalmente, para lo cual usted debe solicitar la
#cantidad de horas trabajadas a la semana y el valor de la hora y
#mostrar el valor del pago.

# Solicitar la cantidad de horas trabajadas en la semana
horas_trabajadas = float(input("Ingrese la cantidad de horas trabajadas en la semana: "))

# Solicitar el valor de la hora de trabajo
valor_hora = float(input("Ingrese el valor de la hora de trabajo: "))

# Calcular el pago total multiplicando las horas trabajadas por el valor de la hora
pago_total = horas_trabajadas * valor_hora

# Mostrar el pago total
print(f"El pago total por {horas_trabajadas} horas trabajadas es: {pago_total:.2f} unidades monetarias")
