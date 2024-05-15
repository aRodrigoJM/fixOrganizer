import os
import re

def renombrar_archivos_serie(directorio_principal):
    # Patrón de expresión regular para encontrar temporada y episodio
    patron = re.compile(r'\bCap\.(\d{3})\b', re.IGNORECASE)

    # Iterar sobre cada carpeta, subcarpeta y archivo en el directorio
    for raiz, _, archivos in os.walk(directorio_principal, topdown=False):
        for archivo in archivos:
            match = patron.search(archivo)
            if match:
                # Extraer el número de temporada y episodio del nombre del archivo
                num = match.group(1)
                temporada = num[0]
                episodio = num[1:]

                # Crear un nuevo nombre en el formato correcto de Plex
                nombre_serie = archivo.split(' - ')[0]  # Asumiendo que el nombre de la serie está antes del guión
                nuevo_nombre = f"{nombre_serie} - s{temporada}e{episodio}.mp4"  # Asumiendo que el archivo es siempre .mp4

                # Ruta completa del nuevo archivo
                nuevo_archivo_ruta = os.path.join(directorio_principal, nuevo_nombre)

                # Ruta completa del archivo actual
                archivo_actual_ruta = os.path.join(raiz, archivo)

                # Renombrar y mover el archivo
                os.rename(archivo_actual_ruta, nuevo_archivo_ruta)
                print(f"Renombrado y movido '{archivo_actual_ruta}' a '{nuevo_archivo_ruta}'")

def obtener_subcarpetas(directorio):
    subcarpetas = []
    # Listar todos los elementos en el directorio dado
    for item in os.listdir(directorio):
        # Construir la ruta completa del elemento
        ruta_completa = os.path.join(directorio, item)
        # Verificar si el elemento es una carpeta
        if os.path.isdir(ruta_completa):
            subcarpetas.append(ruta_completa)
    return subcarpetas

# Usar la función
directorio_principal = "/media/VARIOS"
subcarpetas = obtener_subcarpetas(directorio_principal)

# Ahora puedes recorrer la lista de subcarpetas para realizar operaciones adicionales
for subcarpeta in subcarpetas:
    # directorio_principal = "/media/VARIOS/theLastOfUs" # Ruta a la carpeta principal
    renombrar_archivos_serie(subcarpeta)
    # print(f'{subcarpeta}')
