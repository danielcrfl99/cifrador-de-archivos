from tkinter import ttk
from tkinter import Tk, Label, Button, messagebox
import rgb
import voz_cif
import menu
import pymysql
import os
import io
import sys
import ejecCifDec
from ejecCifDec import cifrar, cifrar_grab
from PIL import Image, ImageTk
import hashlib
from argon2 import PasswordHasher
from obArchivos import resource_Path
import politicaUso


fuente = "Century Gothic"

class cifrar_archivo:
    def __init__(self, usuario, ruta, bandera, con_rgb, con_voz):
    #def __init__(self, usuario, ruta):
        window = Tk()
        self.wind = window
        self.wind.title("Cifrar Archivo")
        self.wind.resizable(0,0)
        self.wind.geometry("620x350")
        self.wind.configure(background="blue")
        
        global flag
        global route
        global rgbpass
        global voz
        global user
        
        flag= bandera
        route = ruta
        rgbpass = con_rgb
        voz = con_voz
        user = usuario
        
        #img = PhotoImage(file = "fondo.png")
        #labelfondo = Label(self.wind, image = img)
        #labelfondo.place(x=0, y=0)
        path = resource_Path("fondo.png")
        image = Image.open(path)
        resize_image = image.resize((620, 350))
        img = ImageTk.PhotoImage(resize_image)
        labelfondo = Label(self.wind, image = img)
        labelfondo.place(x=-2, y=0)
        
        lblTitulo=Label(self.wind,text="Cifrar Archivo", bg="blue")
        lblTitulo.place(x=210,y=5)
        lblTitulo.config(fg="white",font=(fuente,20, "bold"),height=1)
        
        global host, userbd, passbd, nombd, portbd
        host = "brfvvzvjp0x6ye5yzxsa-mysql.services.clever-cloud.com"
        nombd = "brfvvzvjp0x6ye5yzxsa"
        userbd = "u2w8flswhjfoqbf0"
        passbd = "RuhbO7yQ9p7H3AzZ2Eud"
        portbd = 21401
        
       # BtnSel = Button(self.wind,bg="gray",text="Seleccionar",font=(fuente,11,"bold")).place(x=475, y=88)
        largo_btns = 14
        ancho_btns = 4
        BtnClaveVoz = Button(self.wind,activebackground= "gray",text="Ingresar clave\nde voz",command=self.ing_voz,width=largo_btns, height=ancho_btns,cursor="hand2",font=(fuente,10,"bold"))
        BtnClaveVoz.place(x=120, y=120)
        
        BtnClaveRGB = Button(self.wind,activebackground= "gray",text="Ingresar clave \n RGB",command=self.ing_rgb,width=largo_btns, height=ancho_btns,cursor="hand2",font=(fuente,10,"bold"))
        BtnClaveRGB.place(x=380, y=120)
        
        global btnCifrar
        BtnCifrar = Button(self.wind,activebackground= "gray",text="Cifrar",command=self.realizar_cif,width=10, height=2,cursor="hand2",font=(fuente,10,"bold"))
        BtnCifrar.place(x=210, y=260)
        
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
        voz_cif.voz(user, route, flag, rgbpass, voz)
        
    def ing_rgb(self):
        global flag
        global route
        global rgbpass
        global voz
        global user
        self.wind.destroy()
        rgb.rgb_nueva(user, route, flag, rgbpass, voz)
        
    def realizar_cif(self):
        global user, route, flag, rgbpass, voz, tipo
        if(len(voz) >= 6 and len(rgbpass) >= 54):
            validar_nombre = self.valNombre()
            if(validar_nombre == 0):
                conf, ruta_narchivo = cifrar(route, voz)
                if(conf == "Hecho"):
                    self.nuevoArchivo(ruta_narchivo)
                    self.borrarGrab()
                    messagebox.showinfo(message="Tu archivo ha sido cifrado", title="Cifrado éxitoso")
                    self.wind.destroy()
                    os.system('cls')
                    menu.menu_principal(user)
                else:
                    messagebox.showerror(message="No se pudo realizar el cifrado", title="Error")
                    os.system('cls')
            else:
                messagebox.showerror(message="Ya existe un archivo con este nombre, cambie el nombre del archivo por favor.", title="Error")
                os.system('cls')
        else:
            messagebox.showerror(message="Se requieren las claves RGB y de voz para continuar con el proceso. Asegurate que han sido ingresadas.", title="Error")
            os.system('cls')
    
    def valNombre(self):
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
    
    def nuevoArchivo(self, ruta_narchivo):
        global nombreArc, tipo, user, voz, rgbpass
        global host, userbd, passbd, nombd, portbd
        print("\n\nEspera un momento...\n")
        ph = PasswordHasher(time_cost=3, memory_cost=2**16, parallelism=8, hash_len=32, salt_len=16)
        clave_hash = ph.hash(voz)
        clavergb_hash = ph.hash(rgbpass)
        ciphertext = cifrar_grab("grabacion1.wav", rgbpass)
        ciphertext2 = cifrar_grab("grabacion2.wav", rgbpass)
        ciphertext3 = cifrar_grab("grabacion3.wav", rgbpass)
        ciphertext4 = cifrar_grab("grabacion4.wav", rgbpass)
        ciphertext5 = cifrar_grab("grabacion5.wav", rgbpass)
        if(ciphertext == "E" or ciphertext2 == "E" or ciphertext3 == "E" or ciphertext4 == "E" or ciphertext == "E"):
            messagebox.showerror(message="Ha ocurrido un error, vuelve a intentarlo por favor.", title="Error")
            os.remove(ruta_narchivo)
        else:
            print("\nConectando con la base de datos...\n")
            try:
                #connection = pymysql.connect(host="localhost", user="root", passwd="", database="cifrador")
                connection = pymysql.connect(host=host, user=userbd, passwd=passbd, database=nombd, port = portbd)
                cursor = connection.cursor()
                query = """ INSERT INTO archivos(Nombre_Archivo, Tipo, Clave, ClaveRGB, grab1, grab2, grab3, grab4, grab5, Usuario_NombreUsuario)\
                VALUES (%s,%s,%s,%s,HEX(%s),HEX(%s),HEX(%s),HEX(%s),HEX(%s),%s)"""
                cursor.execute(query, (nombreArc, tipo, clave_hash, clavergb_hash, ciphertext, ciphertext2, ciphertext3, ciphertext4, ciphertext5, user))
                connection.commit()
                print("Espera un momento...\n\n")
            except pymysql.Error:
                messagebox.showerror(message="Ha ocurrido un error al conectar con la base de datos\nVuelve a intentarlo por favor.", title="Error SQL")
                os.remove(ruta_narchivo)
            finally:
                cursor.close()
                connection.close()
            
    def borrarGrab(self):
        os.remove('grabacion1.wav')
        os.remove('grabacion2.wav')
        os.remove('grabacion3.wav')
        os.remove('grabacion4.wav')
        os.remove('grabacion5.wav')
        
    def funPolUso(self):
        politicaUso.nuevo()   
        
#if __name__ == '__main__':
   #ventana = Tk()
#   cifrar_archivo()
   #ventana.mainloop()'''