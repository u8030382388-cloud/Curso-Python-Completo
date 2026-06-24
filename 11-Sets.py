# Un set es una colección de elementos únicos (sin duplicados)
# y no mantiene un orden fijo.

primer = {1, 2, 3, 4}

# Convertimos una lista en set (se eliminan duplicados automáticamente)
segundo = [1, 4, 4, 5]
segundo = set(segundo)

# =========================
# ! OPERACIONES CON SETS
# =========================

# ? Unión (|):
# * Une todos los elementos de ambos sets sin repetir ninguno
print(primer | segundo)

# ? Intersección (&):
# * Muestra solo los elementos que están en los dos sets
print(primer & segundo)

# ? Diferencia (-):
# * Muestra los elementos que están en "primer" pero NO en "segundo"
print(primer - segundo)

# ? Diferencia simétrica (^):
# * Muestra los elementos que están en uno u otro set, pero no en ambos
print(primer ^ segundo)
    