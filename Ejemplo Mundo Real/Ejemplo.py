class Usuario:
    def __init__(self, nombre, correo):
        self.nombre = nombre
        self.correo = correo
        self.reservas = []

    def hacer_reserva(self, evento, cantidad_personas):
        if evento.quedan_asientos(cantidad_personas):
            reserva = Reserva(self, evento, cantidad_personas)
            self.reservas.append(reserva)
            evento.actualizar_asientos(cantidad_personas)
            print(f"{self.nombre} ha hecho una reserva para {cantidad_personas} personas en el evento {evento.nombre}.")
        else:
            print(f"No hay suficientes asientos disponibles para {cantidad_personas} personas en el evento {evento.nombre}.")

    def ver_reservas(self):
        print(f"Reservas de {self.nombre}:")
        for reserva in self.reservas:
            print(f" - Evento: {reserva.evento.nombre}, Personas: {reserva.cantidad_personas}")

class Reserva:
    def __init__(self, usuario, evento, cantidad_personas):
        self.usuario = usuario
        self.evento = evento
        self.cantidad_personas = cantidad_personas

class Evento:
    def __init__(self, nombre, fecha, capacidad_maxima):
        self.nombre = nombre
        self.fecha = fecha
        self.capacidad_maxima = capacidad_maxima
        self.asientos_disponibles = capacidad_maxima

    def quedan_asientos(self, cantidad_personas):
        return self.asientos_disponibles >= cantidad_personas

    def actualizar_asientos(self, cantidad_personas):
        self.asientos_disponibles -= cantidad_personas

# Creación de instancias y demostración de interacción
evento1 = Evento("Concierto", "01/01/2023", 100)
usuario1 = Usuario("Juan", "juan@gmail.com")

usuario1.hacer_reserva(evento1, 3)
usuario1.ver_reservas()