# La función lambda sirve para:

# ? Devolver texto:
saludar = lambda nombre: f"Hola {nombre}"

print(saludar("Gabriel"))

# ? Comprobar condiciones:
es_par = lambda x: x % 2 == 0

print(es_par(4))

# ? Sacar información de una tupla:
persona = ("Gabriel", 12)

obtener_nombre = lambda x: x[0]

print(obtener_nombre(persona))

# Elementos que trabajan de mejor manera con lambda:

# ! map():
# ! Transforma cada elemento
numeros = [1, 2, 3]

resultado = list(map(lambda x: x * 2, numeros))

print(resultado)

# ! filter():
# ! Filtra elementos
numeros = [1, 2, 3, 4, 5, 6]

pares = list(filter(lambda x: x % 2 == 0, numeros))

print(pares)

# ! sorted():
# ! Ordena según una regla que indiques
nombres = ["Gabriel", "Ana", "Juan"]

ordenados = sorted(nombres, key=len)# * --> Está representando lo mismo que el lambda

print(ordenados)
    