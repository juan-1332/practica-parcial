# main.py
from sucursales import crear_sucursal, listar_sucursales, actualizar_sucursal

def mostrar_menu():
    print("\n=================================")
    print("  GESTIÓN DE SUCURSALES (CRUD)   ")
    print("=================================")
    print("1. Registrar nueva sucursal")
    print("2. Consultar / Filtrar sucursales")
    print("3. Editar sucursal existente")
    print("0. Salir")
    print("=================================")

def main():
    sucursales = []

    while True:
        mostrar_menu()
        opcion = input("Seleccione una opción: ").strip()

        if opcion == "1":
            crear_sucursal(sucursales)
        elif opcion == "2":
            listar_sucursales(sucursales)
        elif opcion == "3":
            actualizar_sucursal(sucursales)
        elif opcion == "0":
            print("Saliendo del programa...")
            break
        else:
            print(" Opción no válida. Intente de nuevo.")

if __name__ == "__main__":
    main()