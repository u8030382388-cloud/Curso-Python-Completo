
# * Las tuplas son inmutables, lo que significa que no se pueden modificar después de su creación.
# * Puedes concatenar tuplas para crear una nueva.
# * Las tuplas se representan con paréntesis () y los elementos se separan por comas.
numeros = (1, 2, 3) + (4, 5)
print(numeros)

# ? Como convertir una lista a una tupla
lista = [1, 2, 3]
tupla = tuple(lista)
print(tupla)

# ? Las tuplas pueden contener elementos de diferentes tipos de datos.
mixta = (1, "hola", 3.14, True)
print(mixta)

# ? También puedes hacer el efecto contrario, convertir una tupla a una lista.
tupla = (1, 2, 3)
lista = list(tupla)
print(lista)

# ? Puedes extraer una porción de una tupla usando slicing.
menosNumeros = numeros[:2]
print(menosNumeros)
    