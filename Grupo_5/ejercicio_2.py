#Para incentivar las compras, la cadena de almacenes “el
#triunfo” está otorgando un 30% de descuento en todos sus
#productos. Usted debe construir un algoritmo que permita
#calcular este descuento, solicitando al usuario el valor del
#artículo, calculando el descuento y mostrando el valor a
#pagar.

# Mostramos un mensaje para que el usuario sepa qué hará el programa.
print("Bienvenido a la cadena de almacenes 'El Triunfo'.")
print("Este programa calculará el 30% de descuento en el precio de un artículo.")

# Solicitamos al usuario que ingrese el precio del artículo.
# Usamos float para aceptar precios con decimales.
precio = float(input("Por favor, ingrese el precio del artículo: "))

# Calculamos el descuento aplicando el 30% al precio ingresado.
# La fórmula es: descuento = precio * 0.30
descuento = precio * 0.30

# Calculamos el valor final a pagar restando el descuento del precio original.
# La fórmula es: valor_final = precio - descuento
valor_final = precio - descuento

# Mostramos el resultado al usuario:
# - El descuento aplicado.
# - El precio final después del descuento.
print(f"El descuento aplicado es: ${descuento:.2f}")
print(f"El valor final a pagar por el artículo es: ${valor_final:.2f}")
