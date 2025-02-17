class Producto:
    def __init__(self, id, nombre, cantidad, precio):
        """Constructor de la clase Producto."""
        self.id = id
        self.nombre = nombre
        self.cantidad = cantidad
        self.precio = precio

# Métodos getter y setter para cada atributo del producto
def get_id(self):
    """Retorna el ID del producto."""
    return self.id

def get_nombre(self):
    """Retorna el nombre del producto."""
    return self.nombre

def get_cantidad(self):
    """Retorna la cantidad del producto."""
    return self.cantidad

def set_cantidad(self, cantidad):
    """Actualiza la cantidad del producto."""
    self.cantidad = cantidad

def set_precio(self, precio):
    """Actualiza el precio del producto."""
    self.precio = precio

def __str__(self):
    """Retorna una representación en cadena del producto."""
    return f"ID: {self.id}, Nombre: {self.nombre}, Cantidad: {self.cantidad}, Precio: {self.precio:.2f}"

class Inventario:
    def __init__(self):
        """Constructor de la clase Inventario."""
        self.productos = []

def añadir_producto(self, producto):
    """Añade un nuevo producto al inventario si el ID es único."""
    for prod in self.productos:
        if prod.get_id() == producto.get_id():
            print("Error: El ID del producto ya existe.")
        return
    self.productos.append(producto)
    print("Producto añadido exitosamente.")

def eliminar_producto(self, id):
    """Elimina un producto del inventario por ID."""
    for i, prod in enumerate(self.productos):
        if prod.get_id() == id:
            del self.productos[i]
            print("Producto eliminado exitosamente.")
            return
        print("Error: Producto no encontrado.")

def actualizar_producto(self, id, cantidad=None, precio=None):
    """Actualiza la cantidad o precio de un producto por ID."""
    for prod in self.productos:
        if prod.get_id() == id:
            if cantidad is not None:
                prod.set_cantidad(cantidad)
                if precio is not None:
                    prod.set_precio(precio)
                    print("Producto actualizado exitosamente.")
                    return
print("Error: Producto no encontrado.")

def buscar_producto(self, nombre):
    """Busca productos por nombre."""
    encontrados = [prod for prod in self.productos if nombre.lower() in prod.get_nombre().lower()]
    if encontrados:
        print("Productos encontrados:")
    for prod in encontrados:
        print(prod)
    else:
        print("No se encontraron productos con ese nombre.")

def mostrar_productos(self):
    """Muestra todos los productos en el inventario."""
    if not self.productos:
        print("El inventario está vacío.")
        return
    print("Productos en el inventario:")
    for prod in self.productos:
        print(prod)

def main():
    inventario = Inventario()

    while True:
        print("\nMenu:")
        print("1. Añadir Producto")
        print("2. Eliminar Producto")
        print("3. Actualizar Producto")
        print("4. Buscar Producto")
        print("5. Mostrar Productos")
        print("6. Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == '1':
            id = input("ID del producto: ")
            nombre = input("Nombre del producto: ")
            cantidad = int(input("Cantidad del producto: "))
            precio = float(input("Precio del producto: "))
            nuevo_producto = Producto(id, nombre, cantidad, precio)
            inventario.añadir_producto(nuevo_producto)

        elif opcion == '2':
            id = input("ID del producto a eliminar: ")
            inventario.eliminar_producto(id)

        elif opcion == '3':
            id = input("ID del producto a actualizar: ")
            cantidad = input("Nueva cantidad (deje en blanco para no cambiar): ")
            precio = input("Nuevo precio (deje en blanco para no cambiar): ")
            cantidad = int(cantidad) if cantidad else None
            precio = float(precio) if precio else None
            inventario.actualizar_producto(id, cantidad, precio)

        elif opcion == '4':
            nombre = input("Nombre del producto a buscar: ")
            inventario.buscar_producto(nombre)

        elif opcion == '5':
            inventario.mostrar_productos()

        elif opcion == '6':
            print("Saliendo del sistema...")
            break

        else:
            print("Opción no válida, intente nuevamente.")

if __name__ == "__main__":
    main()
