from tkinter import ttk
from tkinter import Label, Button, Tk, messagebox
from PIL import Image, ImageTk
import rgb
import voz_des
import menu
import pymysql
import os
import io
import sys
import ejecCifDec
from ejecCifDec import descifrar, descifrar_grab

from dtw import dtw, accelerated_dtw
import numpy as np
import librosa
from numpy.linalg import norm
import librosa.display
import scipy
import scipy.io.wavfile
from argon2 import PasswordHasher
from obArchivos import resource_Path
import politicaUso

fuente = "Century Gothic"

class descifrar_archivo:
    def __init__(self, usuario, ruta, bandera, con_rgb, con_voz):
    #def __init__(self, usuario, ruta):
        window = Tk()
        self.wind = window
        self.wind.title("Descifrar Archivo")
        self.wind.resizable(0,0)
        self.wind.geometry("620x350")
        self.wind.configure(background="blue")
        
        global host, userbd, passbd, nombd, portbd
        host = "brfvvzvjp0x6ye5yzxsa-mysql.services.clever-cloud.com"
        nombd = "brfvvzvjp0x6ye5yzxsa"
        userbd = "u2w8flswhjfoqbf0"
        passbd = "RuhbO7yQ9p7H3AzZ2Eud"
        portbd = 21401
        
        global user, route, flag, rgbpass, voz
        user = usuario
        route = ruta
        flag = bandera
        rgbpass = con_rgb
        voz = con_voz
        
        #img = PhotoImage(file = "fondo.png")
        #labelfondo = Label(self.wind, image = img)
        #labelfondo.place(x=0, y=0)
        path = resource_Path("fondo.png")
        image = Image.open(path)
        resize_image = image.resize((620, 350))
        img = ImageTk.PhotoImage(resize_image)
        labelfondo = Label(self.wind, image = img)
        labelfondo.place(x=-2, y=0)
        
        
        lblTitulo=Label(self.wind,text="Descifrar Archivo", bg="blue")
        lblTitulo.place(x=200,y=5)
        lblTitulo.config(fg="white",font=(fuente,20, "bold"),height=1)
        
       # BtnSel = Button(self.wind,bg="gray",text="Seleccionar",font=(fuente,11,"bold")).place(x=475, y=88)
        largo_btns = 14
        ancho_btns = 4
        BtnClaveVoz = Button(self.wind,activebackground= "gray",text="Ingresar clave\nde voz", command= self.ing_voz, width=largo_btns, height=ancho_btns,cursor="hand2",font=(fuente,10,"bold"))
        BtnClaveVoz.place(x=120, y=120)
        BtnClaveRGB = Button(self.wind,activebackground= "gray",text="Ingresar clave \n RGB",command= self.ing_rgb, width=largo_btns, height=ancho_btns,cursor="hand2",font=(fuente,10,"bold"))
        BtnClaveRGB.place(x=380, y=120)
        BtnDescifrar = Button(self.wind,activebackground= "gray",text="Descifrar",command= self.ejec_des,width=10, height=2,cursor="hand2",font=(fuente,10,"bold"))
        BtnDescifrar.place(x=210, y=260)
        BtnCancelar = Button(self.wind,activebackground= "gray",text="Cancelar",command=self.cancelar,width=10, height=2,cursor="hand2",font=(fuente,10,"bold"))
        BtnCancelar.place(x=310, y=260)
        
        lblPolUso = Label(self.wind, text="Políticas de uso", bg = "blue", font=('Helveticabold', 9), fg="white", cursor="hand2")
        lblPolUso.place(x=45, y=310)
        lblPolUso.bind("<Button-1>", lambda e: self.funPolUso())
        
        window.mainloop()
        
    def cancelar(self):
        global user
        self.wind.destroy()
        menu.menu_principal(user)
        
    def ing_voz(self):
        global user, route, flag, rgbpass, voz
        self.wind.destroy()
        voz_des.grab_voz(user, route, flag, rgbpass, voz)
        
    def ing_rgb(self):
        global flag
        global route
        global rgbpass
        global voz
        global user
        self.wind.destroy()
        rgb.rgb_nueva(user, route, flag, rgbpass, voz)
        
    def ejec_des(self):
        global user, route, flag, rgbpass, voz
        if(len(voz) >= 6 and len(rgbpass) >= 54):
            validar_existencia = self.valExis()
            if(validar_existencia == 0):
                messagebox.showerror(message="No hay ningún archivo con este nombre.", title="Error")
            else:
                clave_bd, clavergb_bd, tipo = self.extraerDatos()
                if(clave_bd == "correcto" and clavergb_bd == "correcto"):
                    validacion_identidad = self.comGrab()
                    if(validacion_identidad == 1):
                        conf, ruta_dArchivo = descifrar(route, voz, tipo)
                        if(conf == "Hecho"):
                            self.borrarArchivo(ruta_dArchivo)
                            #comprobacion = self.valExis()
                            messagebox.showinfo(message="Tu archivo se ha descifrado", title="Cifrado éxitoso")
                            self.borrarGrab()
                            self.wind.destroy()
                            os.system('cls')
                            menu.menu_principal(user)
                        else:
                            messagebox.showerror(message="No se pudo realizar el descifrado.", title="Error")
                    else:
                        rgbpass = ""
                        voz = ""
                        messagebox.showerror(message="La autenticación de identidad no ha sido aprobada.", title="Error")
                        self.borrarGrab() 
                        os.system('cls')
                elif(clave_bd == "errorGrab" and clavergb_bd == "errorGrab"):
                    messagebox.showerror(message="Los archivos de audio han sido corrompidos", title="Error")
                    os.system('cls')
                else:
                    messagebox.showerror(message="Las contraseñas no coinciden", title="Error")
                    os.system('cls')
        else:
            messagebox.showerror(message="Faltan claves por ingresar.", title="Error")
            os.system('cls')
        
            
    def valExis(self):
        global route, user, nombreArc, tipo
        global host, userbd, passbd, nombd, portbd
        root, tipo = os.path.splitext(route)
        aux = root.split("/")
        nombreArc = aux[len(aux)-1]
        try:
            #connection = pymysql.connect(host="localhost", user="root", passwd="", database="cifrador")
            connection = pymysql.connect(host=host, user=userbd, passwd=passbd, database=nombd, port= portbd)
            cursor = connection.cursor()
            select = "SELECT COUNT(*) from archivos where Nombre_Archivo = '" + nombreArc + "' and Usuario_NombreUsuario =  '" + user + "';"
            cursor.execute(select)
            resultado = cursor.fetchone()
            resultadofinal = resultado[0]
            return resultadofinal
        except pymysql.Error:
            messagebox.showerror(message="Ha ocurrido un error al conectar con la base de datos\nVuelve a intentarlo por favor.", title="Error SQL")
        finally:
            connection.commit()
            connection.close()
    
    def extraerDatos(self):
        global route, user, nombreArc, tipo, rgbpass, voz
        global host, userbd, passbd, nombd, portbd
        root, tipo = os.path.splitext(route)
        aux = root.split("/")
        nombreArc = aux[len(aux)-1]
        try:
            #connection = pymysql.connect(host="localhost", user="root", passwd="", database="cifrador")
            connection = pymysql.connect(host=host, user=userbd, passwd=passbd, database=nombd, port=portbd)
            cursor = connection.cursor()
            select = "SELECT Nombre_Archivo, Tipo, Clave, ClaveRGB, UNHEX(grab1), UNHEX(grab2), UNHEX(grab3), UNHEX(grab4), UNHEX(grab5), Usuario_NombreUsuario from archivos where Nombre_Archivo = '" + nombreArc + "' and Usuario_NombreUsuario =  '" + user + "';"
            cursor.execute(select)
            resultado = cursor.fetchall()
            for a in resultado:
                nombre_archivo = a[0]
                tipo = a[1]
                clave = a[2]
                claveRGB = a[3]
                grab1 = a[4]
                grab2 = a[5]
                grab3 = a[6]
                grab4 = a[7]
                grab5 = a[8]
                NombreUsuario = a[9]
            
            print("Espera un momento...\n\n")
            ph = PasswordHasher(time_cost=3, memory_cost=2**16, parallelism=8, hash_len=32, salt_len=16)
            try:    
                if(ph.verify(clave, voz)): #Comparación de claves de voz
                    try:
                        if(ph.verify(claveRGB, rgbpass)): #Comparación de claves RGB
                            #Si coinciden se descifran las grabaciones
                            descifrado = descifrar_grab(grab1, rgbpass)
                            descifrado2 = descifrar_grab(grab2, rgbpass)
                            descifrado3 = descifrar_grab(grab3, rgbpass)
                            descifrado4 = descifrar_grab(grab4, rgbpass)
                            descifrado5 = descifrar_grab(grab5, rgbpass)

                            if(descifrado == "E" or descifrado2 == "E" or descifrado3 == "E" or descifrado4 == "E" or descifrado5 == "E"):
                                validacion1 = "errorGrab"
                                validacion2 = "errorGrab"
                            else:
                                with open('grabacion1.wav', 'wb') as file1:
                                    file1.write(descifrado)
                                    
                                with open('grabacion2.wav', 'wb') as file2:
                                    file2.write(descifrado2)
                                    
                                with open('grabacion3.wav', 'wb') as file3:
                                    file3.write(descifrado3)
                                
                                with open('grabacion4.wav', 'wb') as file4:
                                    file4.write(descifrado4)
                                
                                with open('grabacion5.wav', 'wb') as file5:
                                    file5.write(descifrado5)
                                    
                                validacion1 = "correcto"
                                validacion2 = "correcto"
                        else:
                            if(ph.check_needs_rehash(rgbpass)):
                               rehash = ph.hash(rgbpass)
                               self.actuPassRGB(user, rehash) 
                            validacion1 = "correcto"
                            validacion2 = "error"
                    except:
                        #messagebox.showerror(message="Las contraseñas no coinciden", title="Error")
                        validacion1 = "error"
                        validacion2 = "error"
                else:
                    if(ph.check_needs_rehash(voz)):
                        rehash = ph.hash(voz)
                        self.actuPassVoz(nombreArc, user, rehash)
                    validacion1 = "error"
                    validacion2 = "error"
            except:
                validacion1 = "error"
                validacion2 = "error"
            return validacion1, validacion2, tipo
        except pymysql.Error:
            messagebox.showerror(message="Ha ocurrido un error al conectar con la base de datos\nVuelve a intentarlo por favor.", title="Error SQL")
        finally:
            connection.commit()
            connection.close()
    
    def actuPassVoz(self, nombreArc, nomUser, acPass):
        global host, userbd, passbd, nombd, portbd
        try:
            #connection = pymysql.connect(host="localhost", user="root", passwd="", database="cifrador")
            connection = pymysql.connect(host=host, user=userbd, passwd=passbd, database=nombd, port=portbd)
            cursor = connection.cursor()
            update = "UPDATE archivos set Clave = '" + acPass + "' where Usuario_NombreUsuario = '"+ nomUser +"' and Nombre_Archivo = '"+ nombreArc +"';"
            cursor.execute(update)
            cursor.close()
            connection.commit()
            connection.close()
        except pymysql.Error:
            messagebox.showerror(message="Ha ocurrido un error al conectar con la base de datos\nVuelve a intentarlo por favor.", title="Error SQL")
            
            
    def actuPassVozRGB(self, nombreArc, nomUser, acPass):
        global host, userbd, passbd, nombd, portbd
        try:
            #connection = pymysql.connect(host="localhost", user="root", passwd="", database="cifrador")
            connection = pymysql.connect(host=host, user=userbd, passwd=passbd, database=nombd, port=portbd)
            cursor = connection.cursor()
            update = "UPDATE archivos set ClaveRGB = '" + acPass + "' where Usuario_NombreUsuario = '"+ nomUser +"' and Nombre_Archivo = '"+ nombreArc +"';"
            cursor.execute(update)
            cursor.close()
            connection.commit()
            connection.close()
        except pymysql.Error:
            messagebox.showerror(message="Ha ocurrido un error al conectar con la base de datos\nVuelve a intentarlo por favor.", title="Error SQL")
    
    
    def comGrab(self):
        os.system("cls")
        print("\n\nValidación de identidad en proceso\nEspera un momento...\n")
        contador = 0
        path = resource_Path("grabacion1.wav")
        y1, sr1 = librosa.load(path, sr=None) #Se carga el archivo de audio
        path2 = resource_Path("grabacion2.wav")
        y2, sr2 = librosa.load(path2, sr=None) #Se carga el archivo de audio
        path3 = resource_Path("grabacion3.wav")
        y3, sr3 = librosa.load(path3, sr=None) #Se carga el archivo de audio
        path4 = resource_Path("grabacion4.wav")
        y4, sr4 = librosa.load(path4, sr=None) #Se carga el archivo de audio
        path5 = resource_Path("grabacion5.wav")
        y5, sr5 = librosa.load(path5, sr=None) #Se carga el archivo de audio
        path6 = resource_Path("validacion1.wav")
        y6, sr6 = librosa.load(path6, sr=None) #Se carga el archivo de audio
        #Se extraen las características de voz de las 6 grabaciones
        melspec_args = {"hop_length":1024, "window": scipy.signal.get_window("hamming", 2048)}
        mfcc1 = librosa.feature.mfcc(y=y1, sr=sr1, **melspec_args)
        mfcc2 = librosa.feature.mfcc(y=y2, sr=sr2, **melspec_args)
        mfcc3 = librosa.feature.mfcc(y=y3, sr=sr3, **melspec_args)
        mfcc4 = librosa.feature.mfcc(y=y4, sr=sr4, **melspec_args)
        mfcc5 = librosa.feature.mfcc(y=y5, sr=sr5, **melspec_args)
        mfcc6 = librosa.feature.mfcc(y=y6, sr=sr6, **melspec_args)
        #Se calcula DTW para encontrar la similitud entre los resultados
        dist, cost, acc_cost, path = dtw(mfcc6.T, mfcc1.T, dist=lambda x, y: norm(x - y, ord=1))
        dist2, cost2, acc_cost2, path2 = dtw(mfcc6.T, mfcc2.T, dist=lambda x, y: norm(x - y, ord=1))
        dist3, cost3, acc_cost3, path3 = dtw(mfcc6.T, mfcc3.T, dist=lambda x, y: norm(x - y, ord=1))
        dist4, cost4, acc_cost4, path4 = dtw(mfcc6.T, mfcc4.T, dist=lambda x, y: norm(x - y, ord=1))
        dist5, cost5, acc_cost5, path5 = dtw(mfcc6.T, mfcc5.T, dist=lambda x, y: norm(x - y, ord=1))
        print("\n\nResultados autenticación identidad")
        print(dist)
        print(dist2)
        print(dist3)
        print(dist4)
        print(dist5)
        
        if(dist <= 38000):
            contador = contador + 1
        if(dist2 <= 38000):
            contador = contador + 1
        if(dist3 <= 38000):
            contador = contador + 1
        if(dist4 <= 38000):
            contador = contador + 1
        if(dist5 <= 38000):
            contador = contador + 1
        
        if(contador >= 3):
            return 1
        else:
            return 0
        
    def borrarGrab(self):
        path = resource_Path("grabacion1.wav")
        os.remove(path)
        path2 = resource_Path("grabacion2.wav")
        os.remove(path2)
        path3 = resource_Path("grabacion3.wav")
        os.remove(path3)
        path4 = resource_Path("grabacion4.wav")
        os.remove(path4)
        path5 = resource_Path("grabacion5.wav")
        os.remove(path5)
        path6 = resource_Path("validacion1.wav")
        os.remove(path6)
        
    def borrarArchivo(self, ruta_dArchivo):
        global route, user, nombreArc, tipo
        global host, userbd, passbd, nombd, portbd
        print("\n\nEspera un momento por favor...\n")
        print("Conectando con la base de datos...\n")
        try:
            #connection = pymysql.connect(host="localhost", user="root", passwd="", database="cifrador")
            connection = pymysql.connect(host=host, user=userbd, passwd=passbd, database=nombd, port=portbd)
            cursor = connection.cursor()
            query = "DELETE from archivos where Nombre_Archivo = '" + nombreArc + "' and Usuario_NombreUsuario =  '" + user + "';"
            cursor.execute(query)
            cursor.close()
            connection.commit()
            connection.close()
            print("Proceso finalizado")
        except pymysql.Error:
            messagebox.showerror(message="Ha ocurrido un error al conectar con la base de datos\nVuelve a intentarlo por favor.", title="Error SQL")
            os.remove(ruta_dArchivo)
            
    def funPolUso(self):
        politicaUso.nuevo()           
    
#if __name__ == '__main__':
   #ventana = Tk()
#   descifrar_archivo()
   #ventana.mainloop()'''