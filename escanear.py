import os, time

def escanear_carpeta():
    direccion_galileo = r"/root/cattana/ENTRETENIMIENTO/POST ENTRETENIMIENTO/To_GALILEO"
    for archivo in os.listdir(direccion_galileo):

        full_path = os.path.join(direccion_galileo, archivo)
        

        if os.path.isdir(full_path):
            escanear_carpeta(full_path)
        else:
            size_gb = os.stat(full_path).st_size / 1_073_741_824  # Convertir a GB
            print(full_path, "\t\t||\t", round(size_gb, 2), "GB")

escanear_carpeta() 
    