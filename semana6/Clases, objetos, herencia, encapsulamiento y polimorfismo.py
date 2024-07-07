# Clase base que representa un Animal
class Animal:
    def __init__(self, nombre, edad):
        self.__nombre = nombre  # Encapsulación del nombre
        self.__edad = edad  # Encapsulación de la edad

    def hacer_sonido(self):
        pass  # Método base para hacer sonido

    def obtener_informacion(self):
        return f"Nombre: {self.__nombre}, Edad: {self.__edad}"


# Clase derivada que representa un Perro
class Perro(Animal):
    def __init__(self, nombre, edad, raza):
        super().__init__(nombre, edad)  # Llamada al constructor de la clase base
        self.__raza = raza  # Encapsulación de la raza

    def hacer_sonido(self):
        return "¡Guau!"  # Polimorfismo: Método sobrescrito para un perro

    def obtener_informacion(self):
        # Polimorfismo: Utilizando el método de la clase base y añadiendo información específica
        return f"{super().obtener_informacion()}, Raza: {self.__raza}"


# Crear instancias de las clases
animal_generico = Animal("Animalito", 3)
perro1 = Perro("Fido", 2, "Labrador")

# Demostrar funcionalidad
print("Información del Animal Genérico:")
print(animal_generico.obtener_informacion())
print("\nInformación del Perro:")
print(perro1.obtener_informacion())
print(f"Sonido del Perro: {perro1.hacer_sonido()}")