#Construir un algoritmo que permita calcular la edad de una
#persona, para lo cual se requiere solicitar el año de nacimiento
#de la persona, calcular la edad y mostrarla.

# Importamos la biblioteca `datetime` para obtener el año actual automáticamente
import datetime

# Obtenemos el año actual utilizando la función `datetime.datetime.now()`
# Esto nos permite calcular la edad sin necesidad de que el usuario ingrese el año actual
año_actual = datetime.datetime.now().year

# Pedimos al usuario que ingrese su año de nacimiento
# Convertimos el dato ingresado a un número entero (int), porque los años son números enteros
año_nacimiento = int(input("Ingrese su año de nacimiento (por ejemplo, 1990): "))

# Calculamos la edad restando el año de nacimiento del año actual
edad = año_actual - año_nacimiento

# Mostramos el resultado al usuario
# Usamos una f-string para integrar la edad directamente en el mensaje
print(f"Tienes {edad} años.")