#Martha desea calcular el total y el promedio de gastos de los
#últimos 5 meses, para lo cual ha solicitado su ayuda en la
#construcción de un algoritmo que solicite el valor de los
#gastos de cada mes, sume el valor de esos gastos, calcule el
#promedio y muestre estos resultados.

# Inicializamos una variable para almacenar la suma de los gastos
total_gastos = 0

# Solicitamos los gastos de los 5 meses y los vamos sumando uno por uno
for mes in range(1, 6):  # Usamos un bucle que se repetirá 5 veces, de mes 1 a mes 5
    # Pedimos al usuario el gasto de ese mes y lo convertimos en un número decimal (float)
    gasto = float(input(f"Ingrese el gasto del mes {mes}: "))
    
    # Sumamos el gasto del mes al total de los gastos
    total_gastos += gasto

# Calculamos el promedio de los gastos
promedio_gastos = total_gastos / 5  # Dividimos el total de gastos entre 5 meses

# Mostramos el total de los gastos y el promedio
print(f"El total de los gastos es: {total_gastos:.2f} unidades monetarias")
print(f"El promedio de los gastos es: {promedio_gastos:.2f} unidades monetarias")
