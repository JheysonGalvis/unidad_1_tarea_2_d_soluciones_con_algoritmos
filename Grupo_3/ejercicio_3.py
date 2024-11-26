#El restaurante “doña Pancha” desea construir un algoritmo para
#calcular el valor de la propina sugerida. Para esto, usted debe
#solicitar el valor de la cuenta, calcular el 15% de ese valor y
#mostrar así el valor de la propina sugerida.

# Solicitar al usuario el valor de la cuenta en el restaurante
valor_cuenta = float(input("Ingrese el valor de la cuenta (en pesos): "))

# Calcular el 15% de la cuenta para obtener la propina sugerida
propina = valor_cuenta * 0.15

# Mostrar el valor de la propina sugerida
print(f"La propina sugerida es: {propina:.2f} pesos")
