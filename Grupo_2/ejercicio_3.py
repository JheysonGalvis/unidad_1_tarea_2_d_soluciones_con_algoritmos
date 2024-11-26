#El profesor Juan desea saber el porcentaje de estudiantes que
#han aprobado un curso. Para esto, usted debe solicitar la
#cantidad total de estudiantes del curso y la cantidad de estudiantes
#que aprobaron el curso y mostrar el porcentaje de aprobación del
#curso.

# Solicitar al usuario la cantidad total de estudiantes del curso
total_estudiantes = int(input("Ingrese la cantidad total de estudiantes del curso: "))

# Solicitar al usuario la cantidad de estudiantes que aprobaron el curso
estudiantes_aprobados = int(input("Ingrese la cantidad de estudiantes que aprobaron el curso: "))

# Calcular el porcentaje de estudiantes que aprobaron
# El porcentaje se calcula como (estudiantes_aprobados / total_estudiantes) * 100
porcentaje_aprobados = (estudiantes_aprobados / total_estudiantes) * 100

# Mostrar el resultado: el porcentaje de aprobación
print(f"El porcentaje de estudiantes que aprobaron el curso es: {porcentaje_aprobados:.2f}%")

