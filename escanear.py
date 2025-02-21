import os

def search_files(directory):
  
    for file in os.listdir(directory):
      
      full_path = os.path.join(directory, file)
      

      if os.path.isdir(full_path):
        search_files(full_path)
      else:
        size_gb = os.stat(full_path).st_size / 1_073_741_824  # Convertir a GB
        print(full_path, "\t\t||\t", round(size_gb, 2), "GB")

search_files(r"/root/cattana/ENTRETENIMIENTO/POST ENTRETENIMIENTO/To_GALILEO")

