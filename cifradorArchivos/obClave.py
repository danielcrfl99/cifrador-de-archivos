import os
import io
from google.cloud import speech
import voz_cif as voz
from obArchivos import resource_Path
import os

def obtenerKey(intento):
    print("Obteniendo clave de voz...\nEspera un momento por favor...\n")
    global aux
    aux = ""
    path = resource_Path("key.json")
    #Se autentica el usuario
    client = speech.SpeechClient.from_service_account_file(path)
    #Se determina el archivo con el que se va a trabajar
    if(intento == 1):
        filename = "grabacion1.wav"
    elif(intento == 4):
        filename = "validacion1.wav"
    else:
        filename = "grabacion4.wav"
    #Se lee la información del archivo de audio
    with io.open(filename, 'rb') as f:
        content = f.read()
    #Se codifica el audio para ser compatible con la API
    audio = speech.RecognitionAudio(content=content)
    #Se configura el audio con base en las características del audio
    config = speech.RecognitionConfig(
        sample_rate_hertz = 44100,
        enable_automatic_punctuation = False,
        language_code = 'es-MX',
        audio_channel_count = 1
        )
    #Se pasa la configuración y el audio para tener el contenido
    response = client.recognize(
        config = config,
        audio = audio
        )
    #Se separa toda la respuesta y se queda únicamente con el mensaje
    for resultado in response.results:
        aux = resultado.alternatives[0].transcript.lower().replace(" ", "")

    acentos = {'á': 'a', 'é': 'e', 'í': 'i', 'ó': 'o', 'ú': 'u', 'ü': 'u'}
    for acen in acentos:
    	if acen in aux:
    		aux = aux.replace(acen, acentos[acen]) #Eliminación de acentos y dieresis
    print("\n\nProceso finalizado\n")
    return aux




    #print(aux_2.replace(" ", ""))
    #return aux_2.replace(" ","")


#clave = obtenerKey(4)
#print(clave)