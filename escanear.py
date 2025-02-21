import os

def search_files(directorio: str) -> None:
    """
    Busca recursivamente archivos y carpetas en el directorio especificado.
    
    - Imprime la ruta y el tamaño (en GB) de cada archivo.
    - Indica cuando se encuentra una carpeta vacía.
    """
    try:
        items = os.listdir(directorio)
    except (PermissionError, FileNotFoundError) as error:
        print(f"No se pudo acceder a '{directorio}': {error}")
        return

    for item in items:
        ruta_completa = os.path.join(directorio, item)
        
        if os.path.isdir(ruta_completa):
            # Si la carpeta está vacía, se muestra el mensaje
            if not os.listdir(ruta_completa):
                print(f"\n\tCARPETA VACÍA: {ruta_completa}\n")
            else:
                search_files(ruta_completa)
        else:
            try:
                size_bytes = os.stat(ruta_completa).st_size
            except Exception as e:
                print(f"Error al obtener el tamaño de '{ruta_completa}': {e}")
                continue
            
            size_gb = size_bytes / 1_073_741_824  # Convertir bytes a GB
            print(f"{ruta_completa} ----- {round(size_gb, 2)} GB")


if __name__ == "__main__":
    ruta_inicial = r"/root/cattana/ENTRETENIMIENTO/POST ENTRETENIMIENTO/To_GALILEO"
    search_files(ruta_inicial)
