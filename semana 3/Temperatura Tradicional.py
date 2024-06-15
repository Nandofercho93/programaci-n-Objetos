# Programación Tradicional
# El usuario ingresa el valor de la temperatura de cada dia
def ingresar_temperaturas_diarias():
    temperaturas = []
    for i in range(7):
        temp = float(input(f"Ingrese la temperatura para el día {i + 1}: "))
        temperaturas.append(temp)
    return temperaturas
# Calcula el promedio de la temperatura semanal
def calcular_promedio_semanal(temperaturas):
    promedio = sum(temperaturas) / len(temperaturas)
    return promedio
# Imprime el valor de la tempertura semanal
def main():
    temperaturas_diarias = ingresar_temperaturas_diarias()
    promedio_semanal = calcular_promedio_semanal(temperaturas_diarias)
    print(f"El promedio semanal de temperaturas es: {promedio_semanal:.2f}")

if __name__ == "__main__":
    main()