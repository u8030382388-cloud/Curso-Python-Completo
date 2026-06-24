# importamos diferentes módulos en Python con "import" y "from ... import ..."
import math  # Importar módulo math para funciones matemáticas
import datetime  # Importar módulo datetime para fechas y horas
import random  # Importar módulo random para generar valores aleatorios
from random import randint  # Importar randint para números enteros aleatorios
from math import sqrt  # Importar sqrt para calcular la raíz cuadrada


def main():
    print("math.pi:", math.pi)
    print("sqrt(16):", sqrt(16))
    print("datetime:", datetime.datetime.now())
    print("random.random():", random.random())
    print("randint(1, 10):", randint(1, 10))


if __name__ == "__main__":
    main()
