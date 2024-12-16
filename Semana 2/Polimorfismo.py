# Clase base
class Shape:
    def area(self):
        """Método que debe ser implementado por las subclases."""
        raise NotImplementedError("Subclase debe implementar este método.")

# Clase derivada que representa un cuadrado
class Square(Shape):
    def __init__(self, side):
        self.side = side

    def area(self):
        """Calcula el área del cuadrado."""
        return self.side ** 2

# Clase derivada que representa un triángulo
class Triangle(Shape):
    def __init__(self, base, height):
        self.base = base
        self.height = height

    def area(self):
        """Calcula el área del triángulo."""
        return (self.base * self.height) / 2

# Función que recibe una lista de formas y calcula sus áreas
def print_areas(shapes):
    for shape in shapes:
        print(f"Área: {shape.area()}")

# Uso de las clases Square y Triangle
shapes = [Square(4), Triangle(3, 6)]
print_areas(shapes)