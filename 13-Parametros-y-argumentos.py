"""Ejemplo de función de saludo con valores por defecto."""

# ! Parámetros
def saludo(nombre: str = "Hola", apellido: str = "Mundo") -> str:
    """Devuelve un saludo usando nombre y apellido."""
    return f"Hola {nombre} {apellido}"

# ? Argumentos
print(saludo("Gabriel", "Moya"))
print(saludo("Gabriel"))
print(saludo())
    