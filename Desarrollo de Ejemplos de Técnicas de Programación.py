class Animal:

    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad
        self.salud = 100

    def mostrar_informacion(self):
        print(self.nombre, ":", sep="")
        print("·Edad:", self.edad)
        print("·Salud:", self.salud)

    def envejecer(self):
        self.edad += 1
        print(self.nombre, "ha envejecido un año. Nueva edad:", self.edad)

    def esta_saludable(self):
        return self.salud > 0

    def enfermar(self):
        self.salud -= 20
        if not self.esta_saludable():
            print(self.nombre, "está enfermo. Salud:", self.salud)


class Perro(Animal):

    def __init__(self, nombre, edad, raza):
        super().__init__(nombre, edad)
        self.raza = raza
        self.huesos_enterrados = 0

    def enterrar_hueso(self):
        self.huesos_enterrados += 1
        print(self.nombre, "ha enterrado un hueso. Total de huesos enterrados:", self.huesos_enterrados)

    def mostrar_informacion(self):
        super().mostrar_informacion()
        print("·Raza:", self.raza)
        print("·Huesos Enterrados:", self.huesos_enterrados)

    def ladrar(self):
        print(self.nombre, "está ladrando: ¡Guau, guau!")


class Gato(Animal):

    def __init__(self, nombre, edad, color_pelo):
        super().__init__(nombre, edad)
        self.color_pelo = color_pelo
        self.ratones_cazados = 0

    def cazar_ratones(self):
        self.ratones_cazados += 1
        print(self.nombre, "ha cazado un ratón. Total de ratones cazados:", self.ratones_cazados)

    def mostrar_informacion(self):
        super().mostrar_informacion()
        print("·Color de Pelo:", self.color_pelo)
        print("·Ratones Cazados:", self.ratones_cazados)

    def maullar(self):
        print(self.nombre, "está maullando: ¡Miau, miau!")


def competencia_animal(animal_1, animal_2):
    turno = 0
    while animal_1.esta_saludable() and animal_2.esta_saludable():
        print("\nTurno", turno)
        print(">>> Acción de ", animal_1.nombre, ":", sep="")
        animal_1.enfermar()
        if isinstance(animal_1, Perro):
            animal_1.enterrar_hueso()
            animal_1.ladrar()
        elif isinstance(animal_1, Gato):
            animal_1.cazar_ratones()
            animal_1.maullar()

        print(">>> Acción de ", animal_2.nombre, ":", sep="")
        animal_2.enfermar()
        if isinstance(animal_2, Perro):
            animal_2.enterrar_hueso()
            animal_2.ladrar()
        elif isinstance(animal_2, Gato):
            animal_2.cazar_ratones()
            animal_2.maullar()

        turno += 1

    if animal_1.esta_saludable():
        print("\nHa ganado", animal_1.nombre)
    elif animal_2.esta_saludable():
        print("\nHa ganado", animal_2.nombre)
    else:
        print("\nEmpate")


perro = Perro("Max", 3, "Labrador")
gato = Gato("Whiskers", 2, "Blanco y negro")

perro.mostrar_informacion()
gato.mostrar_informacion()

competencia_animal(perro, gato)