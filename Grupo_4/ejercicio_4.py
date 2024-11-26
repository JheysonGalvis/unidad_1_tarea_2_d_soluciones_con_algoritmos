#Construir un algoritmo que permita calcular el promedio de
#horas de desplazamiento de un trabajador de su casa al trabajo
#durante 6 días laborales. Para esto, usted debe solicitar el
#tiempo invertido en cada día de desplazamiento (en minutos) y
#mostrar el promedio en horas.

# Inicializamos una variable para guardar la suma total de los minutos
total_minutos = 0

# Usamos un bucle para solicitar el tiempo de desplazamiento para cada uno de los 6 días
for i in range(1, 7):  # El rango de 1 a 7 nos dará 6 iteraciones (de 1 a 6)
    # Solicitamos el tiempo de desplazamiento en minutos para el día actual
    tiempo = float(input(f"Ingrese el tiempo de desplazamiento para el día {i} (en minutos): "))
    # Sumamos el tiempo de cada día al total
    total_minutos += tiempo

# Calculamos el promedio de los minutos
promedio_minutos = total_minutos / 6

# Convertimos el promedio de minutos a horas dividiendo entre 60
promedio_horas = promedio_minutos / 60

# Mostramos el resultado en horas con 2 decimales
print(f"El promedio de horas de desplazamiento durante los 6 días laborales es: {promedio_horas:.2f} horas.")
