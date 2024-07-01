# Programa para calcular el área de un rectángulo

# Función para calcular el área del rectángulo
def calcular_area_rectangulo(base, altura):
    """
    Esta función toma la base y la altura de un rectángulo y devuelve el área.

    Parámetros:
    - base (float): La longitud de la base del rectángulo.
    - altura (float): La altura del rectángulo.

    Retorna:
    float: El área del rectángulo.
    """
    area = base * altura
    return area


# Entrada de datos desde el usuario
base_rectangulo = float(input("Ingrese la longitud de la base del rectángulo: "))
altura_rectangulo = float(input("Ingrese la altura del rectángulo: "))

# Llamada a la función para calcular el área
area_resultante = calcular_area_rectangulo(base_rectangulo, altura_rectangulo)

# Mostrar el resultado
print(f"El área del rectángulo con base {base_rectangulo} y altura {altura_rectangulo} es: {area_resultante}")
