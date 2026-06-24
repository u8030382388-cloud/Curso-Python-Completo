Calculadora = input("Elige sumar, multiplicar, restar o dividir: ")

if Calculadora == "sumar":
    S1 = float(input("Introduce el primer número que quieres sumar: "))
    S2 = float(input("Introduce el segundo número que quieres sumar: "))
    print(S1 + S2)

elif Calculadora == "restar":
    R1 = float(input("Introduce el primer número que quieres restar: "))
    R2 = float(input("Introduce el segundo número que quieres restar: "))
    print(R1 - R2)

elif Calculadora == "multiplicar":
    M1 = float(input("Introduce el primer número que quieres multiplicar: "))
    M2 = float(input("Introduce el segundo número que quieres multiplicar: "))
    print(M1 * M2)

elif Calculadora == "dividir":
    D1 = float(input("Introduce el primer número que quieres dividir: "))
    D2 = float(input("Introduce el segundo número que quieres dividir: "))
    if D2 == 0:
        calc = ValueError("Error: no se puede dividir por 0")
        print(calc)
    else:
        print(D1 / D2)
      