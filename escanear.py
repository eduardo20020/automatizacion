import os

def search_files(directorio):
  
    for item in os.listdir(directorio):
      
      ruta_completa = os.path.join(directorio, item)
      

      if os.path.isdir(ruta_completa):
          
        if not os.listdir(ruta_completa):
            print(f"\n\t\tCARPETA VACIA: {item}\n")
        else:
            search_files(ruta_completa)

      else:
        size_gb = os.stat(ruta_completa).st_size / 1_073_741_824  # Convertir a GB
        print(ruta_completa, "-----", round(size_gb, 2), "GB")

search_files(r"/root/cattana/ENTRETENIMIENTO/POST ENTRETENIMIENTO/To_GALILEO")

