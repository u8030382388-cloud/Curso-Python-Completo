Gasolina = input("¿Tienes gasolina? (si/no): ")
Dinero = int(input("El relleno del tanque de combustible cuesta 50 dólares, introduce el dinero disponible: "))

if Gasolina == "no" and Dinero >= 50:
    print("Perfecto, combustible al máximo")

elif Gasolina == "no" and Dinero < 50:
    print("Lo siento, no puedes llenar el tanque, dinero insuficiente")

elif Gasolina == "si":
    print("Lo siento, no puedes llenar el tanque, el tanque ya tiene gasolina")
