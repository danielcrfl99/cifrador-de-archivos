import sounddevice as sd
import soundfile as sf
from scipy.io.wavfile import write
import os
import sys

import numpy as np
from tkinter import Label, Button, Tk, messagebox
from PIL import Image, ImageTk
import descifrar_archivo
import obClave
from obClave import *
from obArchivos import resource_Path
import noisereduce as nr
import librosa
import politicaUso


color_ventana=("blue")
color_etiqueta = ("black")
fuente = "Century Gothic"

fm = 44100
d = 5

class grab_voz():
    def __init__(self, usuario, ruta, bandera, con_rgb, con_voz):
    #def __init__(self):
        ventana = Tk()
        self.ventana = ventana
        self.ventana.title("Detección de voz para descifrar")
        self.ventana.resizable(0,0)
        self.ventana.geometry("650x360")
        self.ventana.configure(background=color_ventana)
        
        global user
        global route
        global flag
        global passrgb
        global passvoz
        user = usuario
        route = ruta
        flag = bandera
        passrgb = con_rgb
        passvoz = con_voz
        
        #img = PhotoImage(file = "fondo.png")
        #labelfondo = Label(self.wind, image = img)
        #labelfondo.place(x=0, y=0)
        path = resource_Path("fondo.png")
        image = Image.open(path)
        resize_image = image.resize((650, 360))
        img = ImageTk.PhotoImage(resize_image)
        labelfondo = Label(self.ventana, image = img)
        labelfondo.place(x=-2, y=0)
        
        lblTitulo = Label(self.ventana,text="Ingresar clave de voz para descifrar",bg=color_ventana)
        lblTitulo.place(x=75,y=8)
        lblTitulo.config(fg="white", bg=color_ventana,font=(fuente,20, "bold"),height=1)

        lblTam = Label(self.ventana,text="Nota: Recuerda que la grabación dura 5 segundos.",bg=color_ventana)
        lblTam.place(x=40,y=80)
        lblTam.config(fg="white", bg=color_ventana,font=(fuente,14, "bold"),height=1)
        
        lblGrab1 = Label(self.ventana,text="Grabación 1",bg=color_ventana)
        lblGrab1.place(x=240,y=130)
        lblGrab1.config(fg="white", bg=color_ventana,font=(fuente,12, "bold"),height=1)
        
        global btnGrabar1
        btnGrabar1 = Button(self.ventana,text="Grabar",bg="red",fg=color_etiqueta,width=6,height=1,command=lambda: self.grabar(1),cursor="hand2",font=(fuente,12,"bold"))
        btnGrabar1.place(x=180,y=170)
        #btnDetener = Button(self.ventana,text="Detener",fg=color_etiqueta,width=8,height=1,command=self.detener,font=(fuente,17,"bold")).place(x=240,y=170)
        global btnReprod1
        btnReprod1 = Button(self.ventana,text="Reproducir Grabación",fg=color_etiqueta,width=20,height=1,command=lambda: self.reproducir(1),cursor="hand2",font=(fuente,12,"bold"))
        btnReprod1.place(x=280,y=170)
        btnReprod1.config(state = 'disabled')
        
        global btnValidar
        btnValidar = Button(self.ventana,activebackground= "gray",text="Finalizar",fg=color_etiqueta,width=20,height=1,command=self.finalizar,cursor="hand2",font=(fuente,12,"bold"))
        btnValidar.place(x=130,y=280)
        btnValidar.config(state = 'disabled')
        
        global btnCancelar
        btnCancelar = Button(self.ventana,activebackground= "gray",text="Cancelar",fg=color_etiqueta,width=14,height=1,command=self.cancelar,cursor="hand2",font=(fuente,12,"bold"))
        btnCancelar.place(x=340,y=280)
        
        lblPolUso = Label(self.ventana, text="Políticas de uso", bg = "blue", font=('Helveticabold', 9), fg="white", cursor="hand2")
        lblPolUso.place(x=45, y=320)
        lblPolUso.bind("<Button-1>", lambda e: self.funPolUso())
        
        ventana.mainloop()
        
    def grabar(self, btna):
        global rec1
        global bn1
        global btnReprod1
        global btnValidar
        global passvoz
        global passrgb
        #print(passvoz)
        #print(passrgb)
        if(btna == 1):
            rec1 = sd.rec(int(d*fm),fm, 1)
            sd.wait()
            btnReprod1.config(state = 'normal')
            btnValidar.config(state = 'normal')

    def reproducir(self, rep):
        global rec1
        if(rep == 1):
            sd.wait()
            sd.play(rec1)
            sd.wait()

    def finalizar(self):
        global rec1, user, route, flag, passrgb, passvoz
        sf.write("validacion1.wav", rec1, fm)
        sd.wait()
        print("Grabacion validacion hecha")
        passvoz = obClave.obtenerKey(4)
        print("Clave de voz detectada: "+passvoz)
        if(len(passvoz) < 6):
            passvoz = ""
            self.borrarGrab()
            messagebox.showerror(message="Ha ocurrido un error al intentar generar la clave, por favor vuelve a realizar las grabaciones.", title="Error")
        else:
            #self.elimRuido()
            #print("Grabacion sin ruido hecha")
            self.ventana.destroy()
            descifrar_archivo.descifrar_archivo(user, route, flag, passrgb, passvoz)
        
    def cancelar(self):
        global user, route, flag, passrgb, passvoz
        passvoz = ""
        self.ventana.destroy()
        descifrar_archivo.descifrar_archivo(user, route, flag, passrgb, passvoz)
        
    def borrarGrab(self):
        os.remove('validacion1.wav')
        
    def elimRuido(self):
        y1, sr1 = librosa.load('validacion1.wav')
        reduce_noise = nr.reduce_noise(y = y1, sr = sr1)
        sf.write("validacion1.wav", reduce_noise, sr1)

    def funPolUso(self):
        politicaUso.nuevo() 

#if __name__ == '__main__':
   #ventana = Tk()
#   grab_voz()
   #ventana.mainloop()'''