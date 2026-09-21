# sucursales.py

def crear_sucursal(lista_sucursales):
    """
    Pide los datos de la sucursal al usuario y la agrega a la lista.
    """
    print("\n--- REGISTRAR NUEVA SUCURSAL ---")
    
    nombre = input("Nombre de la sucursal: ").strip()
    direccion = input("Dirección completa: ").strip()
    telefono = input("Teléfono de contacto: ").strip()
    id_gerente = input("ID del gerente/responsable: ").strip()

    # Validar que los campos no queden vacíos
    if not nombre or not direccion or not telefono or not id_gerente:
        print(" Error: Todos los campos son obligatorios. Registro cancelado.")
        return

    # Estructura de la sucursal como diccionario
    nueva_sucursal = {
        "id": len(lista_sucursales) + 1,  # ID autoincrementable para identificar la sucursal
        "nombre": nombre,
        "direccion": direccion,
        "telefono": telefono,
        "id_gerente": id_gerente,
        "estado": "Activo"  # Estado por defecto para los futuros filtros
    }

    lista_sucursales.append(nueva_sucursal)
    print(f" Sucursal '{nombre}' registrada con éxito (ID: {nueva_sucursal['id']}).")