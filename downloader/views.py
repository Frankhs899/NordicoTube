from django.shortcuts import render
from django.views import View
from django.http import JsonResponse
import os
import re
from pytube import YouTube
import moviepy.editor as mp


class HomeView(View):
    template_name = 'downloder/pages/home.html'

    def get(self, request):
        return render(request, self.template_name)
    
####################DESCARGA DE ARCHIVOS#####################################################################

def limpiar_nombre_archivo(nombre_original):
    # Eliminar caracteres especiales utilizando una expresión regular
    nombre_limpio = re.sub(r'[^\w\s.-]', '', nombre_original)
    return nombre_limpio

def video(request):
    if request.method == 'POST' and request.headers.get('X-Requested-With') == 'XMLHttpRequest':
        url = request.POST.get('url')
        try:
            yt = YouTube(url)
            video_stream = yt.streams.get_highest_resolution()
            video_stream.download(output_path='media/video/')
            file_name = video_stream.default_filename

            # Obtener el título del video y el autor
            titulo = f'{yt.title}-{yt.author}'

            # Limpiar el nombre del archivo
            nuevo_nombre = limpiar_nombre_archivo(titulo)

            # Obtener la extensión del archivo
            _, file_extension = os.path.splitext(file_name)

            # Nuevo nombre del archivo con el título y la extensión
            nuevo_nombre_con_extension = nuevo_nombre + file_extension

            # Ruta original del archivo
            file_path_original = os.path.join('media/video/', file_name)

            # Ruta nueva del archivo
            file_path_nuevo = os.path.join('media/video/', nuevo_nombre_con_extension)

            # Renombrar el archivo
            os.rename(file_path_original, file_path_nuevo)

            # Devolver la ruta del archivo para su posterior descarga
            return JsonResponse({'file_path': file_path_nuevo}) 
        except Exception as e:
            error_message = f'Ha ocurrido un error: {str(e)}'
            return JsonResponse({'error': error_message})

    return JsonResponse({'error': 'Método no permitido'}, status=400)

def convert(ruta, name):
    #Cargamos el fichero .mp4
    clip = mp.VideoFileClip(ruta)
    print('clip obtenido')

    # Ruta completa para guardar el archivo convertido a MP3 en la carpeta 'media/'
    file_path_mp3 = os.path.join('media/audio/convert/', f'{name}.mp3')
    print(f'filepa es {file_path_mp3}')

     #Lo escribimos como audio y `.mp3`
    clip.audio.write_audiofile(file_path_mp3)
    print('Archivo convertido')

    # Cerrar el clip para liberar los recursos
    clip.close()
    print('clip cerrado')

    return file_path_mp3

def delete_convert(ruta):
    try:
        os.remove(ruta)
        print(f"Archivo {ruta} eliminado con éxito.")
    except OSError as e:
        print(f"Error al eliminar el archivo {ruta}: {e}")

#Funcion para descargar audio
def audio(request):
    if request.method == 'POST' and request.headers.get('X-Requested-With') == 'XMLHttpRequest':
        url = request.POST.get('url')
        try:
            yt = YouTube(url)
            video_stream = yt.streams.get_highest_resolution()
            video_stream.download(output_path='media/audio/')
            file_name = video_stream.default_filename
            #titulos        
            titulo = f'{yt.title}-{yt.author}'# Obtener el título del video y el autor
            nuevo_nombre = limpiar_nombre_archivo(titulo)# Limpiar el nombre del archivo            
            _, file_extension = os.path.splitext(file_name)# Obtener la extensión del archivo           
            nuevo_nombre_con_extension = nuevo_nombre + file_extension # Nuevo nombre del archivo con el título y la extensión           
            file_path_original = os.path.join('media/audio/', file_name)# Ruta original del archivo            
            file_path_nuevo = os.path.join('media/audio/', nuevo_nombre_con_extension)# Ruta nueva del archivo            
            os.rename(file_path_original, file_path_nuevo)# Renombrar el archivo
            ruta = file_path_nuevo#Hace referencia a el archivo a convertir y eliminar

            file_path_mp3 = convert(file_path_nuevo, nuevo_nombre)#Convertir archivo a mp3
            delete_convert(ruta)#Eliminar archivo una vez convertido        

            # Devolver la ruta del archivo para su posterior descarga
            return JsonResponse({'file_path': file_path_mp3})  

        except Exception as e:
            error_message = f'Ha ocurrido un error: {str(e)}'
            return JsonResponse({'error': error_message})

    return JsonResponse({'error': 'Método no permitido'}, status=400)

#Funcion obtener info de el video
def obtener_informacion(request):
    if request.method == 'POST' and request.headers.get('X-Requested-With') == 'XMLHttpRequest':
        url = request.POST.get('url')
        if url:
                try:
                    yt = YouTube(url)
                    video_info = {
                        'url':url,
                        'title':yt.title,
                        'autor':yt.author,
                        'duration':yt.length
                    }
                    print(video_info)
                    return JsonResponse({'video_info':video_info})
                except Exception as e:
                    error_message = f'Error: {str(e)}'
                    return JsonResponse({'error': error_message})
    return JsonResponse({'error': 'Método no permitido'}, status=400)
    
class MusicView(View):
    template_name = 'downloder/pages/music.html'

    def get(self, request):
        return render(request, self.template_name)