import time

def mostrar_inventario(inventario):
    if not inventario:
        print("El inventario está vacío.")
        return
    
    # Formato de tabla sencillo con Python puro
    print(f"{'Nombre':<15} | {'Cantidad':<10} | {'Precio':<10}")
    print("-" * 40)
    for p in inventario:
        print(f"{p['nombre']:<15} | {p['cantidad']:<10} | ${p['precio']:<10}")

def agregar_producto(inventario):
    try:
        nombre = input("Ingrese el nombre del producto: ").strip()
        if nombre == "":
            print("Error: El nombre no puede estar vacío.")
            return
            
        cantidad = int(input("Ingrese la cantidad: "))
        precio = float(input("Ingrese el precio: "))
        
        producto = {
            "nombre": nombre,
            "cantidad": cantidad,
            "precio": precio
        }
        inventario.append(producto)
        print("Producto agregado correctamente.")
        
    except ValueError:
        print("Error: La cantidad y el precio deben ser números. Intente de nuevo.")

def buscar_producto(inventario):
    dato = input("Ingrese el nombre a buscar: ").strip().lower()
    encontrado = False
    
    for p in inventario:
        if dato in p["nombre"].lower():
            print(f"-> {p['nombre']} | Cantidad: {p['cantidad']} | Precio: ${p['precio']}")
            encontrado = True
            
    if not encontrado:
        print("Producto no encontrado.")

def editar_producto(inventario):
    nombre = input("Ingrese el nombre exacto del producto a actualizar: ").strip().lower()
    for p in inventario:
        if p["nombre"].lower() == nombre:
            try:
                p["cantidad"] = int(input("Nueva cantidad: "))
                time.sleep(1)
                print("Cantidad actualizada.")
            except ValueError:
                print("Error: La cantidad debe ser un número entero.")
            return
    print("No se encontró el producto.")

def eliminar_producto(inventario):
    nombre = input("Ingrese el nombre exacto del producto a eliminar: ").strip().lower()
    for p in inventario:
        if p["nombre"].lower() == nombre:
            inventario.remove(p)
            time.sleep(1)
            print("Producto eliminado.")
            return
    print("No se encontró el producto.")