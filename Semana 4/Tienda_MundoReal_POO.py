# tienda_verduras.py

class Verdura:
    """VENTAS DE VERDURAS FRESCAS EN LA TIENDA DE ALEX."""

    def __init__(self, nombre, precio, stock=100):
        """Verduras con nombre, precio y cantidad en stock (por defecto 100)."""
        self.nombre = nombre
        self.precio = precio
        self.stock = stock

    def vender(self, cantidad):
        """Vende una cantidad de la verdura, actualizando el stock."""
        if cantidad <= self.stock:
            self.stock -= cantidad
            return self.precio * cantidad
        else:
            print(f"No hay suficiente stock de {self.nombre}.")
            return 0

    def __str__(self):
        """Devuelve una representación en cadena de la verdura."""
        return f"{self.nombre} - Precio: ${self.precio}, Stock: {self.stock}"


class TiendaVerduras:
    """Clase que representa una tienda de verduras."""

    def __init__(self, nombre):
        """Inicializa la tienda con un nombre y una lista de verduras."""
        self.nombre = nombre
        self.verduras = []

    def agregar_verdura(self, verdura):
        """Agrega una verdura a la tienda."""
        self.verduras.append(verdura)

    def mostrar_verduras(self):
        """Muestra todas las verduras disponibles en la tienda."""
        print(f"Verduras disponibles en {self.nombre}:")
        for verdura in self.verduras:
            print(verdura)

    def vender_verdura(self, nombre_verdura, cantidad):
        """Vende una verdura específica de la tienda."""
        for verdura in self.verduras:
            if verdura.nombre == nombre_verdura:
                print(f"\nIntentando vender {cantidad} de {nombre_verdura}.")
                print(f"Stock antes de la venta: {verdura.stock} unidades.")
                total_venta = verdura.vender(cantidad)
                if total_venta > 0:
                    print(f"Venta realizada: {cantidad} de {nombre_verdura} por ${total_venta}.")
                    print(f"Stock después de la venta: {verdura.stock} unidades.")
                return
        print(f"Verdura {nombre_verdura} no encontrada en la tienda.")


# Se ejecuta el programa
if __name__ == "__main__":
    # Se crea una tienda de verduras
    tienda = TiendaVerduras("Tienda de Verduras Frescas")

    # Se establece algunas verduras con stock inicial de 100
    lechuga = Verdura("Lechuga", 1.5)
    tomate = Verdura("Tomate", 2.0)
    zanahoria = Verdura("Zanahoria", 1.0)
    col = Verdura("Col", 1.2)
    brócoli = Verdura("Brócoli", 3.1)
    coliflor = Verdura("Coliflor", 4.0)
    apio = Verdura("Apio", 1.6)
    pepinos = Verdura("Pepino", 2.2)


    # Se agrega verduras a la tienda
    tienda.agregar_verdura(lechuga)
    tienda.agregar_verdura(tomate)
    tienda.agregar_verdura(zanahoria)
    tienda.agregar_verdura(col)
    tienda.agregar_verdura(brócoli)
    tienda.agregar_verdura(coliflor)
    tienda.agregar_verdura(apio)
    tienda.agregar_verdura(pepinos)


    # Mostrar verduras disponibles
    tienda.mostrar_verduras()

    # Vender algunas verduras
    tienda.vender_verdura("Lechuga", 3)
    tienda.vender_verdura("Tomate", 5)
    tienda.vender_verdura("Zanahoria", 3)
    tienda.vender_verdura("Col", 9)
    tienda.vender_verdura("Brócoli", 7)
    tienda.vender_verdura("Coliflor", 10)
    tienda.vender_verdura("Apio", 2)


    # Mostrar verduras después de la venta
    tienda.mostrar_verduras()