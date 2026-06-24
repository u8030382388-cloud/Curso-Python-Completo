def crear_perfil(nombre, **kwargs):
    # kwargs se convierte en un diccionario con las "etiquetas=valor"
    perfil = {"nombre": nombre}
    perfil.update(kwargs)
    return perfil

# Aquí pasas el nombre y las etiquetas que quieras
usuario1 = crear_perfil("Gabriel", edad=12, hobby="Programar")
usuario2 = crear_perfil("Mouredev", lenguaje="Python", puesto="CEO")

print(usuario1)
# Resultado: {'nombre': 'Gabriel', 'edad': 12, 'hobby': 'Programar'}
print(usuario2)
# Resultado: {'nombre': 'Mouredev', 'lenguaje': 'Python', 'puesto': 'CEO'}

# ? kwargs te permite recibir información etiquetada (clave-valor).
# ? Es súper flexible porque cada llamada a la función puede tener características distintas.
