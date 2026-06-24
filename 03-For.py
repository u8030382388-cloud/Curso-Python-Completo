vocales = "aeiouAEIOU"
frase = input("Introduce una frase: ")
contador = 0
for vocal in frase:
    if vocal in vocales:
        contador += 1
print("El número de vocales es: ", contador)

# ? También puede servir para recorrer cada elmento de algo y mostrarlo

