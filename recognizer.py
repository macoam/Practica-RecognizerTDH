import speech_recognition as sr

#Definir el reconocedor

r = sr.Recognizer()

#Definimos archivos de audio

audio_file = sr.AudioFile('goodmorning.wav')

#Speech recognition

with audio_file as source:
    r.adjust_for_ambient_noise(source)
    audio = r.record(source)
    result = r.recognize_google(audio)
    

#Exportar resultados

with open('result.txt', mode='w') as file:
    file.write("Texto destacado:")
    file.write("\n")
    file.write(result)
    print("¡Listo!")