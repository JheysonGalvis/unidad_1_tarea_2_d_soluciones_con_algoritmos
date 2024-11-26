#La empresa Netflix desea saber cuántas horas promedio usted
#mira sus series y películas los días: viernes, sábado y Domingo.
#Para esto, usted debe construir un algoritmo que solicite la
#cantidad de horas del viernes, del sábado y del domingo y
#muestre el promedio de horas.

# Paso 1: Pedir al usuario las horas que ve Netflix en los días viernes, sábado y domingo.
# Usamos la función input() para pedir estos datos, y convertimos la entrada a un número flotante (float), 
# ya que las horas pueden ser números con decimales.

horas_viernes = float(input("¿Cuántas horas ves Netflix el viernes? "))
horas_sabado = float(input("¿Cuántas horas ves Netflix el sábado? "))
horas_domingo = float(input("¿Cuántas horas ves Netflix el domingo? "))

# Paso 2: Calcular el promedio de horas. 
# Para esto, sumamos las horas de los tres días y luego dividimos entre 3 (porque son 3 días).

promedio_horas = (horas_viernes + horas_sabado + horas_domingo) / 3

# Paso 3: Mostrar el resultado del promedio en la pantalla.
# Usamos la función print() para mostrar el resultado al usuario. Mostramos el promedio con 2 decimales.

print(f"El promedio de horas que ves Netflix durante el fin de semana es: {promedio_horas:.2f} horas.")
