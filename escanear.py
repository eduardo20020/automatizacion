import os

def search_files(directorio: str, indent: int = 0) -> None:
    """
    Recorre recursivamente 'directorio' y muestra:
      - Encabezado con el nombre de la carpeta si contiene archivos.
      - Cada archivo con su tamaño en GB.
      - Si una subcarpeta está vacía, lo indica.
    
    El parámetro 'indent' permite formatear la salida para visualizar la jerarquía.
    """
    try:
        items = os.listdir(directorio)
    except (PermissionError, FileNotFoundError) as error:
        print(" " * indent + f"Error al acceder a '{directorio}': {error}")
        return

    # Se separan los archivos y las carpetas
    archivos = [item for item in items if os.path.isfile(os.path.join(directorio, item))]
    subcarpetas = [item for item in items if os.path.isdir(os.path.join(directorio, item))]

    # Si hay archivos, se imprime el encabezado con el nombre de la carpeta
    if archivos:
        print(" " * indent + f"Carpeta: {directorio}")

    # Se listan los archivos con su tamaño
    for archivo in archivos:
        ruta_archivo = os.path.join(directorio, archivo)
        try:
            size_bytes = os.stat(ruta_archivo).st_size
            size_gb = size_bytes / 1_073_741_824  # Convertir a GB
        except Exception as e:
            print(" " * (indent + 2) + f"Error al obtener tamaño de '{archivo}': {e}")
            continue
        print(" " * (indent + 2) + f"{archivo} ----- {round(size_gb, 2)} GB")

    # Se recorren las subcarpetas
    for subdir in subcarpetas:
        ruta_subdir = os.path.join(directorio, subdir)
        try:
            contenido = os.listdir(ruta_subdir)
        except Exception as e:
            print(" " * (indent + 2) + f"Error al acceder a '{ruta_subdir}': {e}")
            continue

        # Si la subcarpeta está vacía, se indica
        if not contenido:
            print(" " * (indent + 2) + f"CARPETA VACÍA: {subdir}")
        else:
            # Llamada recursiva aumentando la indentación para visualizar la jerarquía
            search_files(ruta_subdir, indent + 2)


if __name__ == "__main__":
    ruta_inicial = r"/root/cattana/ENTRETENIMIENTO/POST ENTRETENIMIENTO/To_GALILEO"
    search_files(ruta_inicial)
