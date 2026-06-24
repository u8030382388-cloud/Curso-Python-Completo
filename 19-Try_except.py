
# ? Usamos try y except para manejar errores en nuestro código.
# ? Esto nos permite intentar ejecutar un bloque de código y, si ocurre un error, podemos manejarlo de manera controlada sin que el programa se detenga abruptamente.

try: # ! Empieza la ejecución del bloque de código
    edad = int(input("Ingresa tu edad: "))
    print(f"Tienes {edad} años.")

except ValueError: # ! Si no llega a poner un número como se le indica y da error, entra except en la ejecución
    print("Ocurrió un error al ingresar la edad. Asegúrate de ingresar un número válido.")
