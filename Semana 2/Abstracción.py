from abc import ABC, abstractmethod

# Clase abstracta que define un contrato para los vehículos
class Vehicle(ABC):
    @abstractmethod
    def start_engine(self):
        """Método abstracto para iniciar el motor del vehículo."""
        pass

    @abstractmethod
    def stop_engine(self):
        """Método abstracto para detener el motor del vehículo."""
        pass

    @abstractmethod
    def drive(self):
        """Método abstracto para conducir el vehículo."""
        pass

# Clase concreta que representa un coche
class Car(Vehicle):
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model
        self.engine_running = False

    def start_engine(self):
        """Inicia el motor del coche."""
        self.engine_running = True
        print(f"El motor del coche {self.brand} {self.model} está encendido.")

    def stop_engine(self):
        """Detiene el motor del coche."""
        self.engine_running = False
        print(f"El motor del coche {self.brand} {self.model} está apagado.")

    def drive(self):
        """Conduce el coche si el motor está encendido."""
        if self.engine_running:
            print(f"Conduciendo el coche {self.brand} {self.model}.")
        else:
            print(f"No se puede conducir el coche {self.brand} {self.model} porque el motor está apagado.")

# Clase concreta que representa una motocicleta
class Motorcycle(Vehicle):
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model
        self.engine_running = False

    def start_engine(self):
        """Inicia el motor de la motocicleta."""
        self.engine_running = True
        print(f"El motor de la motocicleta {self.brand} {self.model} está encendido.")

    def stop_engine(self):
        """Detiene el motor de la motocicleta."""
        self.engine_running = False
        print(f"El motor de la motocicleta {self.brand} {self.model} está apagado.")

    def drive(self):
        """Conduce la motocicleta si el motor está encendido."""
        if self.engine_running:
            print(f"Conduciendo la motocicleta {self.brand} {self.model}.")
        else:
            print(f"No se puede conducir la motocicleta {self.brand} {self.model} porque el motor está apagado.")

# Uso de las clases Car y Motorcycle
car = Car("Toyota", "Corolla")
motorcycle = Motorcycle("Yamaha", "MT-07")

# Interacción con el coche
car.start_engine()
car.drive()
car.stop_engine()

# Interacción con la motocicleta
motorcycle.start_engine()
motorcycle.drive()
motorcycle.stop_engine()