print ("******Bienvenidos******")
# Función para ingresar las temperaturas diarias
def ingresar_temperaturas():
    temperaturas = []
    for i in range(7):  # Para una semana
        temp = float(input(f"Ingrese la temperatura del día {i + 1}: "))
        temperaturas.append(temp)
    return temperaturas

# Función para calcular el promedio de las temperaturas
def calcular_promedio(temperaturas):
    return sum(temperaturas) / len(temperaturas)

# Función principal
def main():
    print("Promedio Semanal del Clima")
    temperaturas = ingresar_temperaturas()  # Ingresar temperaturas
    promedio = calcular_promedio(temperaturas)  # Calcular promedio
    print(f"El promedio semanal de temperaturas es: {promedio:.2f}°C")

# Ejecutar el programa
if __name__ == "__main__":
    main()