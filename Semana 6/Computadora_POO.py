# Clase base
print("......................Bienvenidos......................")
class Computadora:
    def __init__(self, marca, modelo, ram):
        self.__marca = marca  # Atributo privado
        self.__modelo = modelo  # Atributo privado
        self.__ram = ram  # Atributo privado

    # Se usa este metodo para obtener la marca de la computadora
    def get_marca(self):
        return self.__marca

    # Se usa este metodo para obtener el modelo de la computadora
    def get_modelo(self):
        return self.__modelo

    # Se usa este metodo para obtener la RAM de la computadora
    def get_ram(self):
        return self.__ram

    # Realice este metodo que será sobrescrito en la clase derivada
    def tipo_computadora(self):
        raise NotImplementedError("Este método debe ser sobrescrito en la clase derivada")

# Clase derivada
class Laptop(Computadora):
    def __init__(self, marca, modelo, ram, peso):
        super().__init__(marca, modelo, ram)  # Llamada al constructor de la clase base
        self.__peso = peso  # Atributo privado

    # Sobrescribiendo el método tipo_computadora
    def tipo_computadora(self):
        return "Laptop"

    # Método para obtener el peso de la laptop
    def get_peso(self):
        return self.__peso

# Clase derivada
class Desktop(Computadora):
    def __init__(self, marca, modelo, ram, torre):
        super().__init__(marca, modelo, ram)  # Llamada al constructor de la clase base
        self.__torre = torre  # Atributo privado

    # Sobrescribiendo el método tipo_computadora
    def tipo_computadora(self):
        return "Desktop"

    # Método para obtener el tipo de torre
    def get_torre(self):
        return self.__torre

# Estas son las funciones para mostrar información de la computadora
def mostrar_info(computadora):
    print(f"Marca: {computadora.get_marca()}")
    print(f"Modelo: {computadora.get_modelo()}")
    print(f"RAM: {computadora.get_ram()} GB")
    print(f"Tipo: {computadora.tipo_computadora()}")

# Se realiza la creación de instancias
laptop1 = Laptop("Dell", "XPS 13", 16, "1.2 kg")
desktop1 = Desktop("HP", "Pavilion", 32, "Torre Media")

# Se culmina con la demostración de la funcionalidad
print("Información de la Laptop:")
mostrar_info(laptop1)
print(f"Peso: {laptop1.get_peso()}")

print("\nInformación de la Desktop:")
mostrar_info(desktop1)
print(f"Torre: {desktop1.get_torre()}")
