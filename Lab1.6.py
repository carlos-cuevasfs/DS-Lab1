class Producto:
    def __init__(self, nombre, precio, cantidad):
        """Inicializa un producto con nombre, precio y cantidad en stock."""
        self.nombre = nombre  # Nombre del producto
        self.precio = precio  # Precio del producto
        self.cantidad = cantidad  # Cantidad disponible en el inventario

    def vender(self, cantidad_vendida):
        """Reduce el stock si hay suficiente cantidad disponible."""
        if cantidad_vendida <= self.cantidad:
            self.cantidad -= cantidad_vendida  # Se resta la cantidad vendida del stock
            print(f"\n Se vendieron {cantidad_vendida} unidades de {self.nombre}.")
        else:
            print(f"\n Stock insuficiente. Solo hay {self.cantidad} unidades de {self.nombre} disponibles.")

    def mostrar_info(self):
        """Muestra la información del producto."""
        print(f"{self.nombre} - Cantidad: {self.cantidad} - Precio: ${self.precio:.2f}")


class Tienda:
    def __init__(self):
        """Inicializa una tienda con un inventario vacío."""
        self.inventario = []  # Lista vacía donde se almacenarán los productos

    def agregar_producto(self):
        """Solicita datos al usuario para agregar un nuevo producto."""
        nombre = input("\nIngrese el nombre del producto: ").strip().capitalize()
        precio = float(input("Ingrese el precio del producto: "))  # Se convierte el precio a float
        cantidad = int(input("Ingrese la cantidad disponible: "))  # Se convierte la cantidad a entero

        # Se crea una nueva instancia de Producto y se agrega a la lista de inventario
        self.inventario.append(Producto(nombre, precio, cantidad))
        print(f"\n Producto '{nombre}' agregado al inventario.")

    def vender_producto(self):
        """Permite vender un producto reduciendo su stock."""
        nombre = input("\nIngrese el nombre del producto a vender: ").strip().capitalize()
        cantidad = int(input("Ingrese la cantidad a vender: "))

        # Se busca el producto en el inventario
        for producto in self.inventario:
            if producto.nombre == nombre:
                producto.vender(cantidad)  # Se llama al método vender del objeto Producto
                return
        
        print(f"\n Producto '{nombre}' no encontrado en el inventario.")

    def verificar_disponibilidad(self):
        """Verifica la cantidad de un producto en inventario."""
        nombre = input("\nIngrese el nombre del producto a consultar: ").strip().capitalize()

        # Se busca el producto en el inventario
        for producto in self.inventario:
            if producto.nombre == nombre:
                print(f"\n Hay {producto.cantidad} unidades de '{nombre}' disponibles.")
                return
        
        print(f"\n No hay existencias de '{nombre}'.")

    def mostrar_inventario(self):
        """Muestra todos los productos en la tienda."""
        print("\n Inventario de la tienda:")
        
        if not self.inventario:  # Verifica si el inventario está vacío
            print(" El inventario está vacío.")
        else:
            for producto in self.inventario:
                producto.mostrar_info()  # Muestra la información de cada producto

    def ejecutar(self):
        """Ejecuta el menú interactivo de la tienda."""
        while True:
            print("\n MENÚ DE GESTIÓN DE INVENTARIO \n Seleccione el número de la opción a usar:")
            print("1️ Agregar producto")
            print("2️ Vender producto")
            print("3️ Verificar disponibilidad")
            print("4️ Mostrar inventario")
            print("5️ Salir")
            
            opcion = input("\nSeleccione una opción: ")

            if opcion == "1":
                self.agregar_producto()
            elif opcion == "2":
                self.vender_producto()
            elif opcion == "3":
                self.verificar_disponibilidad()
            elif opcion == "4":
                self.mostrar_inventario()
            elif opcion == "5":
                print("\n Saliendo del programa...")
                break  # Termina el bucle y finaliza el programa
            else:
                print("\n Opción no válida, intente nuevamente.")


# Inicializar y ejecutar la tienda
tienda = Tienda()
tienda.ejecutar()
