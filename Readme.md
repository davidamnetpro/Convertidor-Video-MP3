Instalación de librerías

pip install pytube pydub

Además, necesitas instalar ffmpeg en tu sistema. En Windows, puedes seguir las instrucciones: https://ffmpeg.org/download.html

Este programa realiza las siguientes tareas:

1. Usa pytube para descargar el video de YouTube.
2. Filtra las transmisiones de video para obtener solo el audio.
3. Descarga el archivo de audio.
4. Usa pydub para convertir el archivo de audio a formato MP3.
5. Elimina el archivo de audio original descargado.
6. Devuelve y muestra la ruta del archivo MP3 resultante.