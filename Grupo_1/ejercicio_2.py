#El profesor Juan ha solicitado su ayuda para calcular el promedio
#de notas de 6 estudiantes. Usted debe construir un algoritmo
#que solicite las 6 notas, las sume y muestre el promedio de los
#estudiantes."""

# Inicializamos una variable para almacenar la suma de las notas
suma_notas = 0

# Usamos un bucle para pedir las 6 notas, una por una
for i in range(1, 7):  # El rango va de 1 a 6 (incluyendo ambos extremos)
    # Solicitamos al usuario que ingrese cada nota
    # Convertimos el valor ingresado a un número decimal (float) porque las notas pueden incluir decimales
    nota = float(input(f"Ingrese la nota del estudiante {i}: "))
    
    # Sumamos la nota ingresada a la variable 'suma_notas'
    suma_notas += nota

# Calculamos el promedio dividiendo la suma de las notas entre 6 (el total de estudiantes)
promedio = suma_notas / 6

# Mostramos el promedio al usuario con un mensaje claro
print(f"El promedio de las notas de los estudiantes es: {promedio:.2f}")
