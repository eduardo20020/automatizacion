import os

def search_files(directorio):
  
    for item in os.listdir(directorio):
      
      ruta_completa = os.path.join(directorio, item)
      

      if os.path.isdir(ruta_completa):
        search_files(ruta_completa)
        print(f"\n\t\tCARPETA VACIA: {item}\n")
      else:
        print(f"\t\t\t\tCARPETA: {item}")
        size_gb = os.stat(ruta_completa).st_size / 1_073_741_824  # Convertir a GB
        print(ruta_completa, "-----", round(size_gb, 2), "GB")

search_files(r"/root/cattana/ENTRETENIMIENTO/POST ENTRETENIMIENTO/To_GALILEO")

