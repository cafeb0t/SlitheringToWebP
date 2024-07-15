# SlitheringToWebP V1.0.0

"""Librerías necesarias para trabajar con imágenes"""
# Para manejar rutas
from pathlib import Path
# Para procesar imágenes
from PIL import Image
# Para interactuar con el sistema operativo
import os

# Obtener la ruta del directorio del script
directorio_script = os.path.dirname(os.path.abspath(__file__))

# Directorio de imágenes sin procesar
imagenes_sin_procesar = directorio_script

# Carpeta donde se va a guardar el resultado de la conversión de imágenes
nombre_carpeta = "webp"

# Ruta de la carpeta 'webp'
ruta_carpeta = os.path.join(directorio_script, nombre_carpeta)

contm_global = 0

# Función para verificar y crear la carpeta 'webp'
def verificar_y_crear_carpeta_webp():
    global contm_global
    if not os.path.exists(ruta_carpeta):
        os.makedirs(ruta_carpeta)
        print(f"Carpeta '{nombre_carpeta}' creada en {directorio_script}.")
       
        if contm_global == 0:
            print("""
Bienvenido a SlitheringToWebP
=============================

Un pequeño software para convertir imágenes a formato WebP en lotes.

Por favor, recuerde tener instalado:
- Pillow 10.4.0
- Pathlib 1.0.1

Puede encontrarlos en https://pypi.org o instalarlos con los siguientes comandos PIP:

    pip install pathlib
    pip install pillow

Coloque este script en la carpeta donde tiene las imágenes para comenzar el proceso. Las imágenes convertidas se guardarán en la carpeta 'webp' dentro del directorio de este script. Puede elegir entre convertir imágenes JPEG, JPG o GIF.

Presione Enter para continuar...
""")
            contm_global =+ 1
            print(contm_global)
            input()  # Espera a que el usuario presione Enter
            
    else:
        print(f"La carpeta '{nombre_carpeta}' ya existe en {directorio_script}.")
        if contm_global == 0:
            print("""
Bienvenido a SlitheringToWebP
=============================

Un pequeño software para convertir imágenes a formato WebP en lotes.

Por favor, recuerde tener instalado:
- Pillow 10.4.0
- Pathlib 1.0.1

Puede encontrarlos en https://pypi.org o instalarlos con los siguientes comandos PIP:

    pip install pathlib
    pip install pillow

Coloque este script en la carpeta donde tiene las imágenes para comenzar el proceso. Las imágenes convertidas se guardarán en la carpeta 'webp' dentro del directorio de este script. Puede elegir entre convertir imágenes JPEG, JPG o GIF.

Presione Enter para continuar...
""")  
            contm_global =+ 1
            print(contm_global)
            input()  # Espera a que el usuario presione Enter


# Función para convertir a webp
def convert_to_webp(source):
    destination = os.path.join(ruta_carpeta, source.stem + ".webp")
    image = Image.open(source)
    image.save(destination, format="webp")
    return destination


def main(tipo_imagen):
    # Verificar y crear la carpeta 'webp' si no existe
    verificar_y_crear_carpeta_webp()
    
    # Obtener todas las imágenes del tipo seleccionado
    paths = Path(imagenes_sin_procesar).glob(f"**/*.{tipo_imagen}")
    
    numero_ima = 0  # Variable para contar las imágenes convertidas
    
    for path in paths:
        webp_path = convert_to_webp(path)
        numero_ima += 1  # Incrementar el contador de imágenes convertidas
        print(f"Convertido {path} a {webp_path}")
    
    print(f"Proceso Terminado. Se han convertido {numero_ima} imágenes {tipo_imagen.upper()}.")

verificar_y_crear_carpeta_webp()
# Preguntar al usuario qué tipo de imágenes desea convertir
while True:
    tipo_imagen = input("Ingrese el tipo de imagen que desea convertir (jpeg, jpg o gif): ").lower()
    if tipo_imagen in ['jpeg', 'jpg', 'gif']:
        main(tipo_imagen)
        break
    else:
        print("Tipo de imagen no válido. Por favor, ingrese 'jpeg', 'jpg' o 'gif'.")
        break
