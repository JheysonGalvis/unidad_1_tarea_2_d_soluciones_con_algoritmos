#Las tiendas “descuéntalo” le han solicitado su ayuda para crear
#un algoritmo que permita calcular el IVA (19%) de un
#producto. Para esto, usted debe solicitar la cantidad del
#producto, el valor del producto y mostrar el valor a pagar
#incluyendo el IVA

# Solicitamos al usuario que ingrese la cantidad de productos que desea comprar
# Convertimos el valor ingresado a un número entero (int) porque la cantidad siempre es un número entero
cantidad = int(input("Ingrese la cantidad del producto: "))

# Solicitamos al usuario que ingrese el valor unitario del producto
# Convertimos el valor ingresado a un número decimal (float) porque puede incluir centavos
valor_unitario = float(input("Ingrese el valor del producto (por unidad): "))

# Calculamos el valor total sin incluir el IVA
valor_total_sin_iva = cantidad * valor_unitario

# Calculamos el IVA (19% del valor total sin IVA)
iva = valor_total_sin_iva * 0.19

# Calculamos el valor total a pagar, sumando el IVA al valor total sin IVA
valor_total_con_iva = valor_total_sin_iva + iva

# Mostramos los resultados al usuario con mensajes claros
print(f"El valor total sin IVA es: ${valor_total_sin_iva:.2f}")
print(f"El IVA (19%) es: ${iva:.2f}")
print(f"El valor total a pagar con IVA incluido es: ${valor_total_con_iva:.2f}")
