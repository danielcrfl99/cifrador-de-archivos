from tkinter import ttk
from tkinter import Tk, Label, Button, messagebox, Entry
from PIL import Image, ImageTk
import home
import pymysql
from argon2 import PasswordHasher
from obArchivos import resource_Path
import time
import politicaUso
import os

color_etiqueta = ("black")
fuente = "Century Gothic"
color_ventana=("blue")

class crear_cuenta:
    def __init__(self):
        window = Tk()
        self.wind = window
        self.wind.title("Crear Cuenta")
        self.wind.resizable(0,0)
        self.wind.geometry("620x380")
        self.wind.configure(background="blue")
        
        #img = PhotoImage(file = "fondo.png")
        #labelfondo = Label(self.wind, image = img)
        #labelfondo.place(x=0, y=0)
        path = resource_Path("fondo.png")
        image = Image.open(path)
        resize_image = image.resize((620, 380))
        img = ImageTk.PhotoImage(resize_image)
        labelfondo = Label(self.wind, image = img)
        labelfondo.place(x=-2, y=0)
        
        global host, userbd, passbd, nombd, portbd
        host = "brfvvzvjp0x6ye5yzxsa-mysql.services.clever-cloud.com"
        nombd = "brfvvzvjp0x6ye5yzxsa"
        userbd = "u2w8flswhjfoqbf0"
        passbd = "RuhbO7yQ9p7H3AzZ2Eud"
        portbd = 21401
        
        lblTitulo=Label(self.wind,text="Crear Cuenta", bg = "blue")
        lblTitulo.place(x=210,y=5)
        lblTitulo.config(fg="white",font=(fuente,20, "bold"),height=1)
        
        lblNombreAc = Label(self.wind,text="Nombre de usuario:",bg=color_ventana)
        lblNombreAc.place(x=60, y=90)
        lblNombreAc.config(fg="white", bg=color_ventana,font=(fuente,11),height=1)
        
        self.entryUser = Entry(self.wind)
        self.entryUser.place(x=260,y=90)
        self.entryUser.config(font=(fuente,12),width=30,justify="left")
        
        lblCorreo = Label(self.wind,text="Correo Electrónico:",bg=color_ventana)
        lblCorreo.place(x=60, y=130)
        lblCorreo.config(fg="white", bg=color_ventana,font=(fuente,11),height=1)
        
        self.entryCorr = Entry(self.wind)
        self.entryCorr.place(x=260,y=130)
        self.entryCorr.config(font=(fuente,12),width=30,justify="left")
        
        lblPass = Label(self.wind,text="Contraseña:",bg=color_ventana)
        lblPass.place(x=60, y=170)
        lblPass.config(fg="white", bg=color_ventana,font=(fuente,11),height=1)
        
        self.entryPass = Entry(self.wind)
        self.entryPass.place(x=260,y=170)
        self.entryPass.config(font=(fuente,12),width=30,justify="left", show="*")
        
        lblPassConf = Label(self.wind,text="Confirma contraseña:",bg=color_ventana)
        lblPassConf.place(x=60, y=210)
        lblPassConf.config(fg="white", bg=color_ventana,font=(fuente,11),height=1)
        
        self.entryPassConf = Entry(self.wind)
        self.entryPassConf.place(x=260,y=210)
        self.entryPassConf.config(font=(fuente,12),width=30,justify="left", show="*")
        
        largo_btns = 16
        ancho_btns = 2
        BtnGuardar = Button(self.wind,activebackground= "gray",text="Confirmar",command=self.confirmar,width=largo_btns, height=ancho_btns,cursor="hand2",font=(fuente,10,"bold"))
        BtnGuardar.place(x=140, y=260)
        BtnCancelar = Button(self.wind,activebackground= "gray",text="Cancelar",command=self.cancelar,width=largo_btns, height=ancho_btns,cursor="hand2",font=(fuente,10,"bold"))
        BtnCancelar.place(x=360, y=260)
        
        lblPolUso = Label(self.wind, text="Políticas de uso", bg = "blue", font=('Helveticabold', 9), fg="white", cursor="hand2")
        lblPolUso.place(x=45, y=320)
        lblPolUso.bind("<Button-1>", lambda e: self.funPolUso())
        
        window.mainloop()
        
    def cancelar(self):
        self.wind.destroy()
        home.home_int()
        
    def confirmar(self):
        nomUser = (self.entryUser.get())
        corrElec = (self.entryCorr.get())
        nompass = (self.entryPass.get())
        passCon = (self.entryPassConf.get())
        if(not nomUser or not corrElec or not nompass or not passCon): #Verificación de campos vacíos
            messagebox.showerror(message="Hay campos vacíos", title="Error")
        else:
            if(len(nompass)>=8): #Longitud de la contraseña
                if(len(nomUser)<=12): #Longitud del nombre de usuario
                    bandera = self.confirmacion_usuario(nomUser) #Chequeo que no haya usuario registrado con mismo nombre de usuario
                    if(bandera == 0):
                        if(nompass == passCon): #Verificación de que las contraseñas coincidan
                            aux = self.verif_correo(corrElec) #Verificación de correo electrónico
                            if(aux == 0):
                                messagebox.showerror(message="El correo no cumple con el formato requerido, verificalo por favor", title="Error")
                                os.system('cls')
                            else:
                                self.insertar_datos(nomUser, corrElec, nompass, passCon) #Ingresar los datos a la base de datos
                                self.wind.destroy()
                                os.system('cls')
                                home.home_int()
                        else:
                            messagebox.showerror(message="Las contraseñas no coinciden", title="Error")
                            os.system('cls')
                    else:
                        messagebox.showerror(message="El nombre de usuario ya existe.\nPor favor selecciona otro.", title="Nombre de usuario existente")
                        os.system('cls')
                else:
                    messagebox.showerror(message="El nombre de usuario es muy largo\nIngresa otro recordando la longitud máxima (12).", title="Nombre de usuario existente")
                    os.system('cls')
            else:
                messagebox.showerror(message="La contraseña es menor a 8 caracteres", title="Error")
                os.system('cls')
                
    def verif_correo(self, corrElec):
        correo = corrElec
        if(correo.count('@') == 1):
            complemento = correo.split('@')
            if(complemento[1].count('.') == 1):
                return 1
            else:
                return 0
        else:
            return 0
                
    
    def confirmacion_usuario(self, nomUser):
        global host, userbd, passbd, nombd, portbd
        try:
            #connection = pymysql.connect(host="localhost", user="root", passwd="", database="cifrador")
            connection = pymysql.connect(host=host, user=userbd, passwd=passbd, database=nombd, port=portbd)
            cursor = connection.cursor()
            select = "SELECT COUNT(*) from usuarios where NombreUsuario = '" + nomUser + "';"
            cursor.execute(select)
            resultado = cursor.fetchone()
            resultadofinal = resultado[0]
            connection.commit()
            return resultadofinal
        except pymysql.Error:
            messagebox.showerror(message="Ha ocurrido un error al conectar con la base de datos\nVuelve a intentarlo por favor.", title="Error SQL")
        
    def insertar_datos(self, nomUser, corrElec, nompass, passCon):
        global host, userbd, passbd, nombd, portbd
        ph = PasswordHasher(time_cost=3, memory_cost=2**16, parallelism=8, hash_len=32, salt_len=16)
        clave_hash = ph.hash(nompass)
        print("Conectando con la base de datos...\nEspera un momento...\n\n")
        try:
            connection = pymysql.connect(host=host, user=userbd, passwd=passbd, database=nombd, port=portbd) #Establecer conexión
            cursor = connection.cursor() #Creación de cursor
            #Creación del query a ejecutar
            insert = "INSERT INTO usuarios(NombreUsuario, Correo_electronico, Password) VALUES ('" + nomUser + "', '" + corrElec + "', '" + clave_hash + "');"
            cursor.execute(insert)
            messagebox.showinfo(message="El registro se ha guardado", title="Registro éxitoso")
            cursor.close()
            connection.commit()
            connection.close() #Termino de conexión
        except pymysql.Error:
            messagebox.showerror(message="Ha ocurrido un error al conectar con la base de datos\nVuelve a intentarlo por favor.", title="Error SQL")
        
        
    def funPolUso(self):
        politicaUso.nuevo() 
        
if __name__ == '__main__':
   #ventana = Tk()
   crear_cuenta()
   #ventana.mainloop()'''