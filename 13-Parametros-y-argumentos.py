"""Ejemplo de función de saludo con valores por defecto."""

# ! Parámetros
# es una variable que recibe la función al ser definida

def saludo(nombre: str = "Hola", apellido: str = "Mundo") -> str:
    """Devuelve un saludo usando nombre y apellido."""
    return f"Hola {nombre} {apellido}"

# ? Argumentos
# es el valor que se le pasa a la función al ser llamada
print(saludo("Gabriel", "Moya"))
print(saludo("Gabriel"))
print(saludo())
    