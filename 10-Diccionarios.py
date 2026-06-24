# Así se crea un diccionario: usando llaves {} y parejas clave:valor
jugador = {
    "nombre": "Gabriel",
    "nivel": 10,
    "tiene_espada": True,
    "puntos_vida": 100
}

# 1. ¿Cómo leo un valor? (Usando su clave entre corchetes)
print(f"El jugador se llama {jugador['nombre']}")
print(f"Su nivel es {jugador['nivel']}")

# 2. ¿Cómo cambio un valor? (Es tan fácil como asignar una variable)
jugador["nivel"] = 11  # ¡Subimos de nivel!

# 3. ¿Cómo añado algo nuevo? (Si la clave no existe, la crea)
jugador["puntuacion"] = 500

# 4. ¿Cómo borro algo? (Usando del)
del jugador["tiene_espada"]

# Así queda el diccionario al final
print(jugador)
    