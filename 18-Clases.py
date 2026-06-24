import random

class Personaje:
    def __init__(self, nombre, vida, nivel):
        self.nombre = nombre
        self.vida = vida
        self.nivel = nivel

    def __str__(self):
        return f"Nombre: {self.nombre}\nVida: {self.vida}\nNivel: {self.nivel}"

    def recibir_daño(self):
        daño = random.randint(1, 50)
        self.vida -= daño
        if self.vida < 0:
            self.vida = 0
        print(f"{self.nombre} ha recibido {daño} puntos de daño y tiene {self.vida} puntos de vida restante")

    def curarse(self):
        curación = random.randint(1, 20)
        self.vida += curación
        if self.vida > 100:
            self.vida = 100
        print(f"{self.nombre} se ha curado {curación} puntos de salud y tiene {self.vida} puntos de vida")

    def subir_nivel(self):
        self.nivel += 1
        print(f"{self.nombre} ha subido al nivel {self.nivel}")

    def esta_vivo(self):
        if self.vida <= 0:
            print(f"{self.nombre} ha muerto")
        else:
            print(f"{self.nombre} está vivo con {self.vida} puntos de vida restante")


P1 = Personaje("Link", 100, 1)

print(P1)
P1.recibir_daño()
P1.curarse()
P1.subir_nivel()
print(P1)
P1.esta_vivo()


# ? __init__ se ejecuta cuando creas/defines un objeto de la clase.

# * class Perro:
# *    def __init__(self, nombre):
# *        self.nombre = nombre

# * p = Perro("Toby")
# ! Luego habrá que definir funciones.

# ? __str__ se ejecuta cuando imprimes un objeto de la clase.

# * class Personaje:
# *    def __init__(self, nombre, vida):
# *        self.nombre = nombre
# *        self.vida = vida

# *    def estado(self):
# *        print(f"{self.nombre} tiene {self.vida} de vida")

# *    def __str__(self):
# *        return f"{self.nombre} | Vida: {self.vida}"


# * p = Personaje("Link", 80)

# MÉTODO NORMAL
# * p.estado()

# __str__ (automático con print)
# * print(p)

# ? __repr__ se ejecuta cuando imprimes un objeto de la clase en la consola con información técnica del código,
# ? pero a diferencia de __str__, __repr__ devuelve una representación más detallada del objeto,
# ? que puede ser útil para depuración.

# ? __eq__ se ejecuta cuando comparas dos objetos de la clase para determinar si son iguales o no.
# * class Personaje:
# *    def __init__(self, nombre, vida):
# *        self.nombre = nombre
# *        self.vida = vida

# *    def __eq__(self, otro):
# *        return self.vida == otro.vida --->self.vida = p1 y otro.vida = p2
# !                                         |---> Ej: Devuelve True si las vidas son iguales, False si no lo son.
# * p1 = Personaje("Link", 100)
# * p2 = Personaje("Zelda", 100)

# * print(p1 == p2)

# ! __ eq__ es una función de comparación de objetos

# ! self es para indicar los objetos de la clase, es decir, para referirse a los atributos y métodos de la clase.

