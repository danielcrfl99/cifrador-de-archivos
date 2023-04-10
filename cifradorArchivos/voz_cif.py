import sounddevice as sd
import soundfile as sf
import os
import sys
import numpy as np
from tkinter import Label, Button, messagebox, Tk
from google.cloud import speech
from PIL import Image, ImageTk
import cifrar_archivo
import obClave
from obClave import *
import descifrar_archivo
from os import remove
from obArchivos import resource_Path
import matplotlib.pyplot as plt
import noisereduce as nr
import librosa
import politicaUso


color_ventana=("blue")
color_etiqueta = ("black")
fuente = "Century Gothic"

fm = 44100
d = 5

class voz:
    #def __init__(self):
    def __init__(self, usuario, ruta, bandera, con_rgb, con_voz):
        self.ventana = Tk()
        self.ventana.title("Detección de voz para cifrar")
        self.ventana.resizable(0,0)
        self.ventana.geometry("820x560")
        self.ventana.configure(background=color_ventana)
        
        #img = PhotoImage(file = "fondo.png")
        #labelfondo = Label(self.ventana, image = img)
        #labelfondo.place(x=0, y=0)
        path = resource_Path("fondo.png")
        image = Image.open(path)
        resize_image = image.resize((820, 560))
        img = ImageTk.PhotoImage(resize_image)
        labelfondo = Label(self.ventana, image = img)
        labelfondo.place(x=-2, y=0)
        
        lblTitulo=Label(self.ventana,text="Ingresar clave de voz para cifrar",bg=color_ventana)
        lblTitulo.place(x=180,y=8)
        lblTitulo.config(fg="white", bg=color_ventana,font=(fuente,20, "bold"),height=1)

        lblTam=Label(self.ventana,text="La longitud de la clave de voz debe ser mínimo de 6 letras y el orden en que se diga la clave debe ser\nel mismo en todas las grabaciones.",bg=color_ventana)
        lblTam.place(x=40,y=60)
        lblTam.config(fg="white", bg=color_ventana,font=(fuente,11, "bold"),height=2)        

        lblTam=Label(self.ventana,text="Nota: Recuerda que la grabación dura 5 segundos.",bg=color_ventana)
        lblTam.place(x=40,y=100)
        lblTam.config(fg="white", bg=color_ventana,font=(fuente,11, "bold"),height=1)

        global cont
        global bn1
        global bn2
        global bn3
        global bn4
        global bn5
        global user
        global route
        global flag
        global passrgb
        global passvoz
        global flaggen
        user = usuario
        route = ruta
        flag = bandera
        passrgb = con_rgb
        passvoz = con_voz
        cont = 0
        bn1 = 0
        bn2 = 0
        bn3 = 0
        bn4 = 0
        bn5 = 0
        flaggen = 0
        #####################Botón 1####################################
        
        lblGrab1=Label(self.ventana,text="Grabación 1",bg=color_ventana)
        lblGrab1.place(x=160,y=140)
        lblGrab1.config(fg="white", bg=color_ventana,font=(fuente,12, "bold"),height=1)
        
        global btnGrabar1
        btnGrabar1 = Button(self.ventana,text="Grabar",bg="red",fg=color_etiqueta,width=6,height=1,command=lambda: self.grabar(1),cursor="hand2",font=(fuente,12,"bold"))
        btnGrabar1.place(x=90,y=180)
        #btnDetener = Button(self.ventana,text="Detener",fg=color_etiqueta,width=8,height=1,command=self.detener,font=(fuente,17,"bold")).place(x=240,y=170)
        global btnReprod1
        btnReprod1 = Button(self.ventana,activebackground= "gray",text="Reproducir Grabación",fg=color_etiqueta,width=20,height=1,cursor="hand2",command=lambda: self.reproducir(1),font=(fuente,12,"bold"))
        btnReprod1.place(x=190,y=180)
        btnReprod1.config(state = 'disabled')

        ################Grabación 2###########################
        
        lblGrab2=Label(self.ventana,text="Grabación 2",bg=color_ventana)
        lblGrab2.place(x=510,y=140)
        lblGrab2.config(fg="white", bg=color_ventana,font=(fuente,12, "bold"),height=1)
        
        global btnGrabar2
        btnGrabar2 = Button(self.ventana,text="Grabar",bg="red",fg=color_etiqueta,width=6,height=1,command=lambda: self.grabar(2),cursor="hand2",font=(fuente,12,"bold"))
        btnGrabar2.place(x=440,y=180)
        #btnDetener = Button(self.ventana,text="Detener",fg=color_etiqueta,width=8,height=1,command=self.detener,font=(fuente,17,"bold")).place(x=240,y=170)
        global btnReprod2
        btnReprod2 = Button(self.ventana,activebackground= "gray",text="Reproducir Grabación",fg=color_etiqueta,width=20,height=1,command=lambda: self.reproducir(2),cursor="hand2",font=(fuente,12,"bold"))
        btnReprod2.place(x=540,y=180)
        btnReprod2.config(state = 'disabled')
        
        
        #################Grabación 3########################
        
        lblGrab3=Label(self.ventana,text="Grabación 3",bg=color_ventana)
        lblGrab3.place(x=160,y=230)
        lblGrab3.config(fg="white", bg=color_ventana,font=(fuente,12, "bold"),height=1)
        
        global btnGrabar3
        btnGrabar3 = Button(self.ventana,text="Grabar",bg="red",fg=color_etiqueta,width=6,height=1,command=lambda: self.grabar(3),cursor="hand2",font=(fuente,12,"bold"))
        btnGrabar3.place(x=90,y=270)
        #btnDetener = Button(self.ventana,text="Detener",fg=color_etiqueta,width=8,height=1,command=self.detener,font=(fuente,17,"bold")).place(x=240,y=170)
        global btnReprod3
        btnReprod3 = Button(self.ventana,activebackground= "gray",text="Reproducir Grabación",fg=color_etiqueta,width=20,height=1,command=lambda: self.reproducir(3),cursor="hand2",font=(fuente,12,"bold"))
        btnReprod3.place(x=190,y=270)
        btnReprod3.config(state = 'disabled')
        
        ################Grabación 4################################
        
        lblGrab4=Label(self.ventana,text="Grabación 4",bg=color_ventana)
        lblGrab4.place(x=510,y=230)
        lblGrab4.config(fg="white", bg=color_ventana,font=(fuente,12, "bold"),height=1)
        
        global btnGrabar4
        btnGrabar4 = Button(self.ventana,text="Grabar",bg="red",fg=color_etiqueta,width=6,height=1,command=lambda: self.grabar(4),cursor="hand2",font=(fuente,12,"bold"))
        btnGrabar4.place(x=440,y=270)
        #btnDetener = Button(self.ventana,text="Detener",fg=color_etiqueta,width=8,height=1,command=self.detener,font=(fuente,17,"bold")).place(x=240,y=170)
        global btnReprod4
        btnReprod4 = Button(self.ventana,activebackground= "gray",text="Reproducir Grabación",fg=color_etiqueta,width=20,height=1,command=lambda: self.reproducir(4),cursor="hand2",font=(fuente,12,"bold"))
        btnReprod4.place(x=540,y=270)
        btnReprod4.config(state = 'disabled')
        
        #################Grabación 5#################################
        
        lblGrab5=Label(self.ventana,text="Grabación 5",bg=color_ventana)
        lblGrab5.place(x=350,y=320)
        lblGrab5.config(fg="white", bg=color_ventana,font=(fuente,12, "bold"),height=1)
        
        global btnGrabar5
        btnGrabar5 = Button(self.ventana,text="Grabar",bg="red",fg=color_etiqueta,width=6,height=1,command=lambda: self.grabar(5),cursor="hand2",font=(fuente,12,"bold"))
        btnGrabar5.place(x=280,y=360)
        #btnDetener = Button(self.ventana,text="Detener",fg=color_etiqueta,width=8,height=1,command=self.detener,font=(fuente,17,"bold")).place(x=240,y=170)
        global btnReprod5
        btnReprod5 = Button(self.ventana,activebackground= "gray",text="Reproducir Grabación",fg=color_etiqueta,width=20,height=1,cursor="hand2",command=lambda: self.reproducir(5),font=(fuente,12,"bold"))
        btnReprod5.place(x=380,y=360)
        btnReprod5.config(state = 'disabled')
        
        ################Botones extra###############################
        
        global btnGenClave
        btnGenClave = Button(self.ventana,activebackground= "gray",text="Generar Clave",fg=color_etiqueta,width=20,height=1,command=self.genClave,cursor="hand2",font=(fuente,12,"bold"))
        btnGenClave.place(x=300,y=420)
        btnGenClave.config(state = 'disabled')

        global btnFinalizar
        btnFinalizar = Button(self.ventana,activebackground= "gray",text="Finalizar Proceso",fg=color_etiqueta,width=20,height=1,command=self.finalizar,cursor="hand2",font=(fuente,12,"bold"))
        btnFinalizar.place(x=220,y=480)
        btnFinalizar.config(state = 'disabled')
        
        btnCancelar = Button(self.ventana,activebackground= "gray",text="Cancelar",fg=color_etiqueta,width=10,height=1,command=self.cancelar,cursor="hand2",font=(fuente,12,"bold"))
        btnCancelar.place(x=440,y=480)

        lblPolUso = Label(self.ventana, text="Políticas de uso", bg = "blue", font=('Helveticabold', 9), fg="white", cursor="hand2")
        lblPolUso.place(x=45, y=500)
        lblPolUso.bind("<Button-1>", lambda e: self.funPolUso())

        self.ventana.mainloop()
        

    def grabar(self, btna):
        global rec1, rec2, rec3, rec4, rec5, bn1, bn2, bn3, bn4, bn5
        global btnReprod1, btnReprod2, btnReprod3, btnReprod4, btnReprod5, btnGenClave, cont
        #fm (frecuencia de muestreo) = 44100 y d (duracion) = 5 segundos
        if(btna == 1):
            rec1 = sd.rec(int(d*fm),fm, 1) #Almacenamiento de la grabación 1 
            sd.wait()
            btnReprod1.config(state = 'normal')
            if bn1 == 0:
                bn1 = 1;
                
        elif(btna == 2):
            rec2 = sd.rec(int(d*fm),fm, 1) #Almacenamiento de la grabación 2 
            sd.wait()
            btnReprod2.config(state = 'normal')
            if bn2 == 0:
                bn2 = 1;
        elif(btna == 3):
            rec3 = sd.rec(int(d*fm),fm, 1) #Almacenamiento de la grabación 3 
            sd.wait()
            btnReprod3.config(state = 'normal')
            if bn3 == 0:
                bn3 = 1;
        elif(btna == 4):
            rec4 = sd.rec(int(d*fm),fm, 1) #Almacenamiento de la grabación 4 
            sd.wait()
            btnReprod4.config(state = 'normal')
            if bn4 == 0:
                bn4 = 1;
        elif(btna == 5):
            rec5 = sd.rec(int(d*fm),fm, 1) #Almacenamiento de la grabación 5 
            sd.wait()
            btnReprod5.config(state = 'normal') 
            if bn5 == 0:
                bn5 = 1;
        print("Grabación hecha")
        if(bn1 == 1 and bn2 == 1 and bn3 == 1 and bn4 == 1 and bn5 == 1):
            btnGenClave.config(state = 'normal')
            
    def reproducir(self, rep):
        global rec1, rec2, rec3, rec4, rec5
        if(rep == 1):
            sd.wait()
            sd.play(rec1) #Play para reproducción de audio
            sd.wait()
        elif(rep == 2):
            sd.wait()
            sd.play(rec2) #Play para reproducción de audio
            sd.wait()
        elif(rep == 3):
            sd.wait()
            sd.play(rec3) #Play para reproducción de audio
            sd.wait()
        elif(rep == 4):
            sd.wait()
            sd.play(rec4) #Play para reproducción de audio
            sd.wait()
        elif(rep == 5):
            sd.wait()
            sd.play(rec5) #Play para reproducción de audio
            sd.wait()
        print("reproduccion hecha")
        
    def genClave(self):
        global rec1, rec2, rec3, rec4, rec5, passvoz, flaggen
        #Frecuencia de muestreo 44100
        sf.write("grabacion1.wav", rec1, fm) #Guardar archivo número 1
        sd.wait()
        sf.write("grabacion2.wav", rec2, fm) #Guardar archivo número 2
        sd.wait()
        sf.write("grabacion3.wav", rec3, fm) #Guardar archivo número 3
        sd.wait()
        sf.write("grabacion4.wav", rec4, fm) #Guardar archivo número 4
        sd.wait()
        sf.write("grabacion5.wav", rec5, fm) #Guardar archivo número 5
        sd.wait()
        #print("Grabación hecha")
        flaggen = 1
        passvoz = obClave.obtenerKey(1)
        print("Clave de voz detectada: "+passvoz)
        if(len(passvoz) < 6):
            passvoz = obClave.obtenerKey(2)
            print("Clave de voz detectada: "+passvoz)
            if(len(passvoz) < 6):
                self.borrarGrab()
                messagebox.showerror(message="Ha ocurrido un error al intentar generar la clave, por favor vuelve a realizar las grabaciones.", title="Error")
            else:
                #self.elimRuido()
                btnFinalizar.config(state = 'normal')
        else:
            #self.elimRuido()
            btnFinalizar.config(state = 'normal')
        
    def finalizar(self):
        global user, route, flag, passrgb, passvoz
        self.ventana.destroy()
        cifrar_archivo.cifrar_archivo(user, route, flag, passrgb, passvoz)
    
    def cancelar(self):
        global user, route, flag, passrgb, passvoz, flaggen
        passvoz = ""
        if(flaggen == 1):
            self.borrarGrab()
        os.system('cls')
        self.ventana.destroy()
        cifrar_archivo.cifrar_archivo(user, route, flag, passrgb, passvoz)

    def borrarGrab(self):
        os.remove('grabacion1.wav')
        os.remove('grabacion2.wav')
        os.remove('grabacion3.wav')
        os.remove('grabacion4.wav')
        os.remove('grabacion5.wav')
    
    def elimRuido(self):
        y1, sr1 = librosa.load('grabacion1.wav')
        y2, sr2 = librosa.load('grabacion2.wav')
        y3, sr3 = librosa.load('grabacion3.wav')
        y4, sr4 = librosa.load('grabacion4.wav')
        y5, sr5 = librosa.load('grabacion5.wav')
        reduce_noise = nr.reduce_noise(y = y1, sr = sr1)
        reduce_noise2 = nr.reduce_noise(y = y2, sr = sr2)
        reduce_noise3 = nr.reduce_noise(y = y3, sr = sr3)
        reduce_noise4 = nr.reduce_noise(y = y4, sr = sr4)
        reduce_noise5 = nr.reduce_noise(y = y5, sr = sr5)
        sf.write("grabacion1.wav", reduce_noise, sr1)
        sf.write("grabacion2.wav", reduce_noise2, sr2)
        sf.write("grabacion3.wav", reduce_noise3, sr3)
        sf.write("grabacion4.wav", reduce_noise4, sr4)
        sf.write("grabacion5.wav", reduce_noise5, sr5)
    
    def funPolUso(self):
        politicaUso.nuevo() 
    
#if __name__ == '__main__':
   #ventana = Tk()
#   voz()
   #ventana.mainloop()'''