mascotas = ("Pelusa", "Michi", "Gato", "Peluche", "Gato", "Gato", "Peluche")
print(mascotas.count("Gato"))  # Devuelve el número de veces que aparece el elemento
print(mascotas.count("Peluche"))
if "Gato" in mascotas:
    print(mascotas.index("Gato"))  # Devuelve el índice del elemento encontrado
if "Pelusa" in mascotas:
    print(mascotas.index("Pelusa"))
 