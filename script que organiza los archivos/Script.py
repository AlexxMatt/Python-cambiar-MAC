import os
import shutil

# Define el directorio a organizar
directory = "ruta/del/directorio/a/organizar"

# Define los directorios donde se moverán los archivos
image_dir = "ruta/del/directorio/imagenes"
doc_dir = "ruta/del/directorio/documentos"
video_dir = "ruta/del/directorio/videos"
audio_dir = "ruta/del/directorio/audio"
other_dir = "ruta/del/directorio/otros"

# Recorre los archivos en el directorio
for filename in os.listdir(directory):
    # Obtiene la extensión del archivo
    extension = os.path.splitext(filename)[1][1:].lower()

    # Organiza los archivos según su extensión
    if extension in ["jpg", "jpeg", "png", "gif"]:
        shutil.move(os.path.join(directory, filename), os.path.join(image_dir, filename))
    elif extension in ["doc", "docx", "pdf", "txt"]:
        shutil.move(os.path.join(directory, filename), os.path.join(doc_dir, filename))
    elif extension in ["mp4", "avi", "mkv", "mov"]:
        shutil.move(os.path.join(directory, filename), os.path.join(video_dir, filename))
    elif extension in ["mp3", "wav", "aac", "flac"]:
        shutil.move(os.path.join(directory, filename), os.path.join(audio_dir, filename))
    else:
        shutil.move(os.path.join(directory, filename), os.path.join(other_dir, filename))
