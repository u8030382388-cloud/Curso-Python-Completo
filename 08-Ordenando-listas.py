numeros = [8, 2, 9, 1, 5, 6]

# ? Ordenar la lista de números
numeros.sort()

# * Otra forma de ordenar la lista pero al reves es usando sort con el argumento reverse=True
# ! numeros.sort(reverse=True)

# * También se puede usar la función sorted() que devuelve una nueva lista ordenada sin modificar la original
# ! numeros2 = sorted(numeros)

# ? Otra forma de ordenar la lista pero al reves es usando sorted con el argumento reverse=True
numeros2 = sorted(numeros, reverse=True)

print("Lista ordenada:", numeros2)
print("Lista original ordenada:", numeros)
    