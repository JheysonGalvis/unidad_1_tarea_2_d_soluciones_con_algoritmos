#En el Black Friday, una tienda de artículos deportivos va a
#realizar un descuento del 15% en toda su línea de productos y
#le han solicitado a usted que construya un algoritmo que
#solicite el valor del producto a comprar, muestre el valor del
#descuento y el valor final a pagar.

# Solicitar al usuario el valor del producto a comprar
valor_producto = float(input("Ingrese el valor del producto a comprar (en pesos): "))

# Calcular el descuento del 15% en el producto
descuento = valor_producto * 0.15

# Calcular el valor final a pagar después del descuento
valor_final = valor_producto - descuento

# Mostrar el valor del descuento y el valor final a pagar
print(f"El valor del descuento es: {descuento:.2f} pesos")
print(f"El valor final a pagar es: {valor_final:.2f} pesos")
