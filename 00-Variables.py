# 1. Definición: Una variable es un nombre que apunta a un valor.
# Imagina que la variable es una etiqueta pegada a una caja.

nombre_jugador = "Alex"      # Guardamos un 'string' (texto)
puntos = 100                 # Guardamos un 'integer' (número entero)
dinero = 10.56               # Guardamos un 'float' (número flotante/decimal)
esta_activo = True           # Guardamos un 'booleano' (lógico)

# 2. Uso: Ahora podemos usar la etiqueta para recuperar el valor.
print(f"El jugador {nombre_jugador} tiene {puntos} puntos.")

# 3. Mutabilidad: Las variables pueden cambiar su contenido.
puntos = puntos + 50
print(f"Ahora {nombre_jugador} tiene {puntos} puntos.")
