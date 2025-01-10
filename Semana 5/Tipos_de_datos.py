# Programa para calcular el área de un círculo y convertir metros a kilómetros.
# En este elemento se utilizara diferentes tipos de datos y se establece las convenciones de nomenclatura.

import math #Empesamos con un import math para esta clase

def calcular_area_circulo(radio: float) -> float:
    """
    Calcular el área de un círculo dado su radio.

    :param radio: El radio del círculo.
    :return: El área del círculo.
    """
    area = math.pi * (radio ** 2)
    return area


def convertir_metros_a_kilometros(metros: float) -> float:
    """
    Convierte una distancia de metros a kilómetros.

    :param metros: La distancia en metros.
    :return: La distancia en kilómetros.
    """
    kilometros = metros / 1000
    return kilometros


def main():
    # En este apartado se muestra el nombre del usuario
    nombre = "USUARIO"  #Se le da una bienvenida al usuario antes de realizar cualquier calculo
    print(f"Bienvenido/a, {nombre}!")
    while True:
        # Solicitar al usuario el radio del círculo
        radio_str = input("Ingrese el radio del círculo en metros: ")
        radio = float(radio_str)  # Convertir la entrada a float

        # Calcular el área del círculo
        area = calcular_area_circulo(radio)
        print(f"El área del círculo con radio {radio} metros es: {area:.2f} metros cuadrados.")

        # Solicitar al usuario una distancia en metros
        metros_str = input("Ingrese una distancia en metros para convertir a kilómetros: ")
        metros = float(metros_str)  # Convertir la entrada a float

        # Convertir metros a kilómetros
        kilometros = convertir_metros_a_kilometros(metros)
        print(f"{metros} metros son {kilometros:.2f} kilómetros.")

        # Preguntar al usuario si desea realizar otro cálculo
        continuar = input("¿Desea realizar otro cálculo? (s/n): ").strip().lower()
        if continuar != 's':
            print("Gracias por acudir a nosotros. ¡Hasta luego!")
            break


#Se Ejecutara el programa
if __name__ == "__main__":
    main()