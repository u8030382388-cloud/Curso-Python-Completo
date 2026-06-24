import random

eleccion = input("Elige un camino sabiamente: Izquierda o Derecha: ")
print("Has elegido el camino de la " + eleccion)

if eleccion == "Izquierda":

    eleccion = input("Te puedes encontrar con un monstruo o con un tesoro, ¿Te arriesgas? (Si/No):")

    if eleccion == "Si":
        accion = random.choice(["monstruo", "Tesoro"])
        if accion == "monstruo":
            print("¡Oh no! Te has encontrado con un monstruo. ¡Has perdido!")
        else:
            print("¡Felicidades! Has encontrado un tesoro. ¡Has ganado!")

    elif eleccion == "No":
        print("Has decidido no arriesgarte. ¡Has salido de la cueva!")

elif eleccion == "Derecha":

    eleccion = input("Te puedes encontrar con una trampa o con la salida, ¿Te arriesgas? (Si/No):")
    if eleccion == "Si":
        accion = random.choice(["trampa", "salida"])
        if accion == "trampa":
            print("¡Oh no! Has caído en una trampa. ¡Has perdido!")
        else:
            print("¡Felicidades! Has encontrado la salida. ¡Has ganado!")
            
    elif eleccion == "No":
        print("Has decidido no arriesgarte. ¡Has salido de la cueva!")
