# persistencia.py
import json
import os

NOMBRE_ARCHIVO = "sucursales.json"

def cargar_datos():
    """
    Carga la lista de sucursales desde el archivo JSON.
    Si el archivo no existe, retorna una lista vacía.
    """
    if not os.path.exists(NOMBRE_ARCHIVO):
        return []

    try:
        with open(NOMBRE_ARCHIVO, "r", encoding="utf-8") as archivo:
            return json.load(archivo)
    except (json.JSONDecodeError, OSError) as e:
        print(f" Error al leer {NOMBRE_ARCHIVO}: {e}. Se iniciará con lista vacía.")
        return []


def guardar_datos(lista_sucursales):
    """
    Guarda la lista de sucursales en el archivo JSON con formato legible.
    """
    try:
        with open(NOMBRE_ARCHIVO, "w", encoding="utf-8") as archivo:
            json.dump(lista_sucursales, archivo, indent=4, ensure_ascii=False)
        print(" Datos guardados correctamente en 'sucursales.json'.")
    except OSError as e:
        print(f" Error al guardar los datos: {e}")