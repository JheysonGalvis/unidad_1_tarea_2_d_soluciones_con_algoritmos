#Diseñe un algoritmo que calcule el área de un terreno de forma
#cuadrada. Para esto, usted debe solicitar la medida del lado del
#terreno (el cual será en metros) y el algoritmo debe calcular el
#área del terreno"""


# Solicitar la medida del lado del terreno al usuario
# Usamos la función input() para recibir datos del usuario.
# Convertimos el valor ingresado a un número decimal (float) porque el usuario puede ingresar medidas con decimales.
lado = float(input("Por favor, ingrese la medida del lado del terreno en metros: "))

# Calcular el área del terreno
# Fórmula del área de un cuadrado: lado * lado
area = lado * lado

# Mostrar el resultado al usuario
# Usamos print() para mostrar el área calculada, con un mensaje claro.
print(f"El área del terreno cuadrado es: {area} metros cuadrados.")
