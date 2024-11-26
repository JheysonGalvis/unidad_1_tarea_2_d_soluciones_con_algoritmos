#La escuela ECAPMA de la UNAD está desarrollando un estudio
#para verificar el cambio climático en su ciudad. Para esto, le ha
#pedido su ayuda en la construcción de un algoritmo que solicite
#las temperaturas de los últimos 4 días y muestre el promedio de temperaturas

# Inicializamos una variable para almacenar la suma de las temperaturas
suma_temperaturas = 0

# Pedimos la temperatura del primer día y sumamos a la variable
# input() solicita un dato al usuario, y usamos float() para asegurarnos de que la entrada sea un número decimal
temperatura_dia1 = float(input("Ingrese la temperatura del primer día: "))
suma_temperaturas += temperatura_dia1  # Sumar la temperatura del primer día a la suma total

# Pedimos la temperatura del segundo día y sumamos a la variable
temperatura_dia2 = float(input("Ingrese la temperatura del segundo día: "))
suma_temperaturas += temperatura_dia2  # Sumar la temperatura del segundo día

# Pedimos la temperatura del tercer día y sumamos a la variable
temperatura_dia3 = float(input("Ingrese la temperatura del tercer día: "))
suma_temperaturas += temperatura_dia3  # Sumar la temperatura del tercer día

# Pedimos la temperatura del cuarto día y sumamos a la variable
temperatura_dia4 = float(input("Ingrese la temperatura del cuarto día: "))
suma_temperaturas += temperatura_dia4  # Sumar la temperatura del cuarto día

# Ahora calculamos el promedio de las temperaturas
# El promedio se calcula sumando todas las temperaturas y dividiendo entre 4 (ya que son 4 días)
promedio_temperaturas = suma_temperaturas / 4

# Mostramos el resultado: el promedio de las temperaturas
print(f"El promedio de las temperaturas de los últimos 4 días es: {promedio_temperaturas:.2f} grados.")
