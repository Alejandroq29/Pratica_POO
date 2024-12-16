class ClimaDiario:
    def __init__(self):
        self.__temperaturas = []  # Atributo privado para almacenar temperaturas

    # Método para ingresar la temperatura de un día
    def ingresar_temperatura(self, temperatura):
        self.__temperaturas.append(temperatura)

    # Método para calcular el promedio de temperaturas
    def calcular_promedio(self):
        if len(self.__temperaturas) == 0:
            return 0  # Evitar división por cero
        return sum(self.__temperaturas) / len(self.__temperaturas)

# Clase para manejar el clima semanal
class ClimaSemanal:
    def __init__(self):
        self.clima_diario = ClimaDiario()  # Composición: ClimaSemanal tiene un ClimaDiario

    # Método para ingresar temperaturas de la semana
    def ingresar_temperaturas_semanales(self):
        for i in range(7):  # Para una semana
            temp = float(input(f"Ingrese la temperatura del día {i + 1}: "))
            self.clima_diario.ingresar_temperatura(temp)

    # Método para mostrar el promedio semanal
    def mostrar_promedio_semanal(self):
        promedio = self.clima_diario.calcular_promedio()
        print(f"El promedio semanal de temperaturas es: {promedio:.2f}°C")

# Función principal
def main():
    print("Promedio Semanal del Clima")
    clima_semanal = ClimaSemanal()  # Crear instancia de ClimaSemanal
    clima_semanal.ingresar_temperaturas_semanales()  # Ingresar temperaturas
    clima_semanal.mostrar_promedio_semanal()  # Mostrar promedio

# Ejecutar el programa
if __name__ == "__main__":
    main()