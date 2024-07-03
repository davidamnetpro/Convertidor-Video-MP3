from pytube import YouTube
from pydub import AudioSegment
import os

def download_youtube_audio(url, output_path):
    # Descargar el video de YouTube
    yt = YouTube(url)
    video = yt.streams.filter(only_audio=True).first()
    out_file = video.download(output_path=output_path)
    
    # Convertir el archivo descargado a mp3
    base, ext = os.path.splitext(out_file)
    new_file = base + '.mp3'
    audio = AudioSegment.from_file(out_file)
    audio.export(new_file, format='mp3')
    
    # Eliminar el archivo original
    os.remove(out_file)
    
    print(f"Descarga completa: {new_file}")
    return new_file

# Ejemplo de uso
link = input("Introduce el enlace de YouTube: ")
output_path = "./"  # Puedes cambiar la ruta de salida
download_youtube_audio(link, output_path)
