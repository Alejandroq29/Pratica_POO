class Producto:
    def __init__(self, nombre, precio, cantidad):
        # Inicializa un objeto Producto con nombre, precio y cantidad disponible
        self.nombre = nombre
        self.precio = precio
        self.cantidad = cantidad

    def __del__(self):
        # Destructor que se llama cuando un objeto Producto es destruido
        print(f"Producto destruido: {self.nombre}")

class Tienda:
    def __init__(self, nombre):
        # Inicializa un objeto Tienda con un nombre y una lista vacía de inventario
        self.nombre = nombre
        self.inventario = []

    def agregar_producto(self, producto):
        # Agrega un objeto Producto a la lista de inventario de la tienda
        self.inventario.append(producto)

    def mostrar_inventario(self):
        # Muestra todos los productos disponibles en el inventario
        print(f"\nInventario de la tienda '{self.nombre}':")
        for index, p in enumerate(self.inventario):
            # Enumera los productos y muestra su nombre, precio y cantidad
            print(f"{index + 1}. {p.nombre}: ${p.precio} (Cantidad: {p.cantidad})")

    def mostrar_producto(self, index):
        # Muestra los detalles de un producto específico dado su índice
        if 0 <= index < len(self.inventario):
            p = self.inventario[index]
            # Muestra el nombre, precio y cantidad del producto seleccionado
            print(f"\nProducto seleccionado: {p.nombre} - Precio: ${p.precio} - Cantidad: {p.cantidad}")
        else:
            # Mensaje de error si el índice es inválido
            print("Índice no válido.")

    def __del__(self):
        # Destructor que se llama cuando un objeto Tienda es destruido
        print(f"Tienda destruida: {self.nombre}")
        # Limpia el inventario al eliminar la tienda
        self.inventario.clear()

# Indicamos name para mostrar lo que se va a realizar 
if __name__ == "__main__":
    # Crear una instancia de la clase Tienda
    tienda = Tienda("Alejandro")

    # Agregar productos de refresco a la tienda
    tienda.agregar_producto(Producto("Coca-Cola", 1.50, 20))
    tienda.agregar_producto(Producto("Pepsi", 1.40, 15))
    tienda.agregar_producto(Producto("Sprite", 1.20, 25))
    tienda.agregar_producto(Producto("Fanta", 1.30, 18))

    # Mostrar inventario de la tienda
    tienda.mostrar_inventario()

    # Permitir que el usuario seleccione un producto por su número en el inventario
    indice_producto = int(input("Selecciona el número del producto para ver detalles: ")) - 1
    # Mostrar los detalles del producto elegido
    tienda.mostrar_producto(indice_producto)