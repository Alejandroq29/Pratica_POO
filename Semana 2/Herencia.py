# Clase base
class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        """Método que debe ser implementado por las subclases."""
        raise NotImplementedError("Subclase debe implementar este método.")

# Clase derivada que hereda de Animal
class Dog(Animal):
    def speak(self):
        """Implementación del método speak para perros."""
        return f"{self.name} dice: ¡Guau!"

# Clase derivada que hereda de Animal
class Cat(Animal):
    def speak(self):
        """Implementación del método speak para gatos."""
        return f"{self.name} dice: ¡Miau!"

# Uso de las clases Dog y Cat
dog = Dog("Rex")
cat = Cat("Miau")

print(dog.speak())
print(cat.speak())