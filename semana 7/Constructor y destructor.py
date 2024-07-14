class Empleado:
    def __init__(self, nombre, salario):
        # Constructor (__init__)
        self.nombre = nombre
        self.salario = salario
        print(f"Se ha creado un empleado: {self.nombre}")

    def realizar_trabajo(self):
        # Método de ejemplo
        print(f"{self.nombre} está realizando su trabajo")

    def __del__(self):
        # Destructor (__del__)
        print(f"Se está eliminando al empleado: {self.nombre}")
        # Aquí podrías agregar acciones de limpieza o liberación de recursos si es necesario

class Departamento:
    def __init__(self, nombre):
        # Constructor (__init__)
        self.nombre = nombre
        self.empleados = []
        print(f"Se ha creado un departamento: {self.nombre}")

    def contratar_empleado(self, nombre, salario):
        # Método para contratar un nuevo empleado
        nuevo_empleado = Empleado(nombre, salario)
        self.empleados.append(nuevo_empleado)
        print(f"{nombre} ha sido contratado en el departamento {self.nombre}")

    def __del__(self):
        # Destructor (__del__)
        print(f"Se está eliminando el departamento: {self.nombre}")

# Crear instancias de las clases
departamento_ti = Departamento("TI")
departamento_ventas = Departamento("Ventas")

# Contratar empleados
departamento_ti.contratar_empleado("Mery Jean", 1000)
departamento_ventas.contratar_empleado("Jimbo", 1200)

# Realizar trabajo
departamento_ti.empleados[0].realizar_trabajo()

# Al finalizar el programa, los destructores se llamarán automáticamente al eliminar las instancias.
# No es necesario llamar a __del__ manualmente.

# Salida esperada:
# Se ha creado un departamento: TI
# Se ha creado un departamento: Ventas
# Se ha creado un empleado: Ana
# Ana ha sido contratado en el departamento TI
# Se ha creado un empleado: Juan
# Juan ha sido contratado en el departamento Ventas
# Ana está realizando su trabajo
# Se está eliminando al empleado: Ana
# Se está eliminando el departamento: TI
# Se está eliminando al empleado: Juan
# Se está eliminando el departamento: Ventas