# Programación Orientada a Objetos (POO)

class ClimaDiario:
    def __init__(self):
        self.temperaturas = []
# El usuario ingresa el valor de la temperatura de cada dia
    def ingresar_temperaturas_diarias(self):
        for i in range(7):
            temp = float(input(f"Ingrese la temperatura para el día {i + 1}: "))
            self.temperaturas.append(temp)
# Calcula el promedio de la temperatura semanal
    def calcular_promedio_semanal(self):
        promedio = sum(self.temperaturas) / len(self.temperaturas)
        return promedio
# Imprime el valor de la tempertura semanal
def main():
    clima = ClimaDiario()
    clima.ingresar_temperaturas_diarias()
    promedio_semanal = clima.calcular_promedio_semanal()
    print(f"El promedio semanal de temperaturas es: {promedio_semanal:.2f}")

if __name__ == "__main__":
    main()