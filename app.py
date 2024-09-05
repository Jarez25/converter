import os
from PIL import Image
from tkinter import Tk, filedialog

# Función para seleccionar una carpeta
def seleccionar_carpeta():
    root = Tk()
    root.withdraw()  # Oculta la ventana principal de tkinter
    carpeta = filedialog.askdirectory()  # Abre el cuadro de diálogo para seleccionar la carpeta
    return carpeta

# Función para convertir imágenes a formato WebP y guardarlas en una subcarpeta
def convertir_a_webp(carpeta):
    formatos_permitidos = ['.jpg', '.jpeg', '.png', '.bmp', '.tiff']  # Formatos de imagen soportados
    calidad = 85  # Calidad de la imagen en el formato WebP
    carpeta_destino = os.path.join(carpeta, 'imgconvertida')  # Carpeta donde se guardarán las imágenes convertidas

    # Crea la carpeta de destino si no existe
    if not os.path.exists(carpeta_destino):
        os.makedirs(carpeta_destino)

    for archivo in os.listdir(carpeta):
        archivo_ruta = os.path.join(carpeta, archivo)
        nombre, extension = os.path.splitext(archivo)

        if extension.lower() in formatos_permitidos:  # Verifica si el archivo es una imagen
            try:
                imagen = Image.open(archivo_ruta)
                webp_ruta = os.path.join(carpeta_destino, f"{nombre}.webp")
                imagen.save(webp_ruta, 'webp', quality=calidad)  # Guarda la imagen en formato WebP en la nueva carpeta
                print(f"Convertido: {archivo} a {nombre}.webp")
            except Exception as e:
                print(f"Error al convertir {archivo}: {e}")

if __name__ == "__main__":
    carpeta_seleccionada = seleccionar_carpeta()
    if carpeta_seleccionada:
        convertir_a_webp(carpeta_seleccionada)
    else:
        print("No se seleccionó ninguna carpeta.")
