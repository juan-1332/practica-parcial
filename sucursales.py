# sucursales.py

def crear_sucursal(lista_sucursales):
    """Pide los datos de la sucursal al usuario y la agrega a la lista."""
    print("\n--- REGISTRAR NUEVA SUCURSAL ---")
    
    nombre = input("Nombre de la sucursal: ").strip()
    direccion = input("Dirección completa: ").strip()
    telefono = input("Teléfono de contacto: ").strip()
    id_gerente = input("ID del gerente/responsable: ").strip()

    if not nombre or not direccion or not telefono or not id_gerente:
        print(" Error: Todos los campos son obligatorios. Registro cancelado.")
        return

    nueva_sucursal = {
        "id": len(lista_sucursales) + 1,
        "nombre": nombre,
        "direccion": direccion,
        "telefono": telefono,
        "id_gerente": id_gerente,
        "estado": "Activo"
    }

    lista_sucursales.append(nueva_sucursal)
    print(f" Sucursal '{nombre}' registrada con éxito (ID: {nueva_sucursal['id']}).")


def listar_sucursales(lista_sucursales):
    """Visualiza todas las sucursales con opción a filtrar por nombre o estado."""
    if not lista_sucursales:
        print("\n No hay sucursales registradas.")
        return

    print("\n--- CONSULTA DE SUCURSALES ---")
    print("1. Ver todas las sucursales")
    print("2. Filtrar por nombre")
    print("3. Filtrar por estado (Activo/Inactivo)")
    
    opcion_filtro = input("Seleccione una opción de filtrado: ").strip()
    resultados = []

    if opcion_filtro == "1":
        resultados = lista_sucursales
    elif opcion_filtro == "2":
        criterio = input("Ingrese el nombre a buscar (o parte de él): ").strip().lower()
        resultados = [s for s in lista_sucursales if criterio in s["nombre"].lower()]
    elif opcion_filtro == "3":
        estado_criterio = input("Ingrese el estado a filtrar (Activo/Inactivo): ").strip().capitalize()
        resultados = [s for s in lista_sucursales if s["estado"] == estado_criterio]
    else:
        print(" Opción de filtro no válida.")
        return

    if not resultados:
        print("\n No se encontraron sucursales con el criterio ingresado.")
        return

    # Mostrar lista formateada
    print("\n" + "=" * 80)
    print(f"{'ID':<5} | {'Nombre':<20} | {'Dirección':<20} | {'Teléfono':<12} | {'ID Gerente':<10} | {'Estado':<8}")
    print("=" * 80)
    for s in resultados:
        print(f"{s['id']:<5} | {s['nombre']:<20} | {s['direccion']:<20} | {s['telefono']:<12} | {s['id_gerente']:<10} | {s['estado']:<8}")
    print("=" * 80)


def actualizar_sucursal(lista_sucursales):
    """Permite editar los datos de una sucursal existente seleccionada por ID."""
    if not lista_sucursales:
        print("\n No hay sucursales registradas para editar.")
        return

    try:
        id_buscar = int(input("\nIngrese el ID de la sucursal que desea editar: ").strip())
    except ValueError:
        print(" Error: El ID debe ser un número entero.")
        return

    # Buscar la sucursal por ID
    sucursal = next((s for s in lista_sucursales if s["id"] == id_buscar), None)

    if not sucursal:
        print(f" No se encontró ninguna sucursal con el ID {id_buscar}.")
        return

    print(f"\n--- EDITANDO SUCURSAL: {sucursal['nombre']} (ID: {sucursal['id']}) ---")
    print("(Presione 'Enter' sin escribir nada si desea mantener el valor actual)")

    nuevo_nombre = input(f"Nombre [{sucursal['nombre']}]: ").strip()
    nueva_direccion = input(f"Dirección [{sucursal['direccion']}]: ").strip()
    nuevo_telefono = input(f"Teléfono [{sucursal['telefono']}]: ").strip()
    nuevo_gerente = input(f"ID Gerente [{sucursal['id_gerente']}]: ").strip()
    nuevo_estado = input(f"Estado [{sucursal['estado']}] (Activo/Inactivo): ").strip().capitalize()

    # Si el usuario ingresó algo, se actualiza; si no, mantiene el valor previo
    if nuevo_nombre:
        sucursal["nombre"] = nuevo_nombre
    if nueva_direccion:
        sucursal["direccion"] = nueva_direccion
    if nuevo_telefono:
        sucursal["telefono"] = nuevo_telefono
    if nuevo_gerente:
        sucursal["id_gerente"] = nuevo_gerente
    if nuevo_estado in ["Activo", "Inactivo"]:
        sucursal["estado"] = nuevo_estado

    print(f" Sucursal ID {id_buscar} actualizada correctamente.")