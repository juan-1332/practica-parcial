# main.py
from sucursales import (
    crear_sucursal,
    listar_sucursales,
    actualizar_sucursal,
    eliminar_sucursal,
)
from persistencia import cargar_datos, guardar_datos

def mostrar_menu():
    print("\n=================================")
    print("  GESTIÓN DE SUCURSALES (CRUD)   ")
    print("=================================")
    print("1. Registrar nueva sucursal")
    print("2. Consultar / Filtrar sucursales")
    print("3. Editar sucursal existente")
    print("4. Eliminar sucursal")
    print("0. Salir")
    print("=================================")

def main():
    # Carga inicial desde JSON
    sucursales = cargar_datos()

    while True:
        mostrar_menu()
        opcion = input("Seleccione una opción: ").strip()

        if opcion == "1":
            crear_sucursal(sucursales)
            guardar_datos(sucursales)
        elif opcion == "2":
            listar_sucursales(sucursales)
        elif opcion == "3":
            actualizar_sucursal(sucursales)
            guardar_datos(sucursales)
        elif opcion == "4":
            eliminar_sucursal(sucursales)
            guardar_datos(sucursales)
        elif opcion == "0":
            guardar_datos(sucursales)
            print("Saliendo del programa...")
            break
        else:
            print(" Opción no válida. Intente de nuevo.")

if __name__ == "__main__":
    main()