def sumar_todos(*args):
    # args se convierte en una tupla, una lista de los valores que le pasaste
    total = sum(args)
    return total

# Puedes pasarle los números que quieras
print(sumar_todos(10, 20, 30))      # Resultado: 60
print(sumar_todos(5, 5, 5, 5, 5))   # Resultado: 25

# ? *args te permite recibir una cantidad indefinida de valores sin tener que definirlos uno a uno en la función.
    