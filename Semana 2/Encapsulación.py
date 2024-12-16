class Usuario:
    def __init__(self, nombre, edad):
        self.__nombre = nombre  # Atributo privado
        self.__edad = edad      # Atributo privado

    # Método para obtener el nombre
    def obtener_nombre(self):
        return self.__nombre

    # Método para establecer el nombre
    def establecer_nombre(self, nuevo_nombre):
        self.__nombre = nuevo_nombre

    # Método para obtener la edad
    def obtener_edad(self):
        return self.__edad

    # Método para establecer la edad
    def establecer_edad(self, nueva_edad):
        if nueva_edad >= 0:  # Validación simple
            self.__edad = nueva_edad
        else:
            print("La edad no puede ser negativa.")

# Uso de la clase Usuario
usuario = Usuario("Juan", 30)

# Accediendo a los atributos a través de métodos
print("Nombre:", usuario.obtener_nombre())
print("Edad:", usuario.obtener_edad())

# Modificando los atributos a través de métodos
usuario.establecer_nombre("Pedro")
usuario.establecer_edad(35)

print("Nombre actualizado:", usuario.obtener_nombre())
print("Edad actualizada:", usuario.obtener_edad())

# Intentando establecer una edad negativa
usuario.establecer_edad(-5)  # Esto mostrará un mensaje de error