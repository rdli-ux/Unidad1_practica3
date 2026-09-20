'''
Ricardo Daniel Lazo Ibarra
GTIR246
Este es un programa de inventario de mercancía para una tienda de abarrotes. Permite agregar, eliminar, actualizar y buscar productos, 
así como mostrar el inventario completo y generar un reporte de productos agotados.
'''



import time
from operaciones import (
    mostrar_inventario, 
    agregar_producto, 
    buscar_producto,
    editar_producto,
    eliminar_producto
)
from datos import cargar_datos, guardar_datos

def menu():
    print("\n-------------------------------------------")
    print("INVENTARIO DE MERCANCÍA - ABARROTES")
    print("-------------------------------------------")
    print(" 1. Agregar producto")
    print(" 2. Eliminar producto")
    print(" 3. Actualizar cantidad de producto")
    print(" 4. Mostrar inventario completo")
    print(" 5. Buscar producto")
    print(" 6. Reporte de mercancía agotada")
    print(" 7. Guardar inventario y Salir")
    print(" 8. Salir sin guardar")
    print("-------------------------------------------")

def main():
    inventario = cargar_datos()

    while True:
        time.sleep(1)
        menu()
        opcion = input("Seleccione una opción (1-8): ").strip()
        
        match opcion:
            case "1":
                agregar_producto(inventario)
            case "2":
                eliminar_producto(inventario)
            case "3":
                editar_producto(inventario)
            case "4":
                mostrar_inventario(inventario)
            case "5":
                buscar_producto(inventario)
            case "6":
                print("\n--- Productos Agotados (Cantidad = 0) ---")
                agotados = [p for p in inventario if p["cantidad"] == 0]
                mostrar_inventario(agotados)
            case "7":
                guardar_datos(inventario)
                print("Inventario guardado. ¡Hasta luego!")
                break
            case "8":
                print("Saliendo sin guardar. ¡Hasta luego!")
                break
            case _:
                print("Opción inválida. Seleccione un número del 1 al 8.")

if __name__ == "__main__":
    main()
    