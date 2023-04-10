from tkinter import ttk
from tkinter import Label, Entry, Button, messagebox, Tk
from PIL import Image, ImageTk
import modificar_cuenta
import pymysql
from argon2 import PasswordHasher
from obArchivos import resource_Path
import politicaUso
import os

color_etiqueta = ("black")
fuente = "Century Gothic"
color_ventana=("blue")

class c_password:
    def __init__(self):
        window = Tk()
        self.wind = window
        self.wind.title("Cambiar Password")
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
        
        lblTitulo=Label(self.wind,text="Cambiar Contraseña", bg="blue")
        lblTitulo.place(x=200,y=5)
        lblTitulo.config(fg="white",font=(fuente,20, "bold"),height=1)
        
        lblNombreAc = Label(self.wind,text="Nombre de usuario:",bg=color_ventana)
        lblNombreAc.place(x=60, y=90)
        lblNombreAc.config(fg="white", bg=color_ventana,font=(fuente,11),height=1)
        
        self.entryUserAc = Entry(self.wind)
        self.entryUserAc.place(x=260,y=90)
        self.entryUserAc.config(font=(fuente,12),width=30,justify="left")
        
        lblPassAc = Label(self.wind,text="Contraseña actual:",bg=color_ventana)
        lblPassAc.place(x=60, y=130)
        lblPassAc.config(fg="white",bg=color_ventana,font=(fuente,11),height=1)
        
        self.entryPassAc = Entry(self.wind)
        self.entryPassAc.place(x=260,y=130)
        self.entryPassAc.config(font=(fuente,12),width=30,justify="left", show="*")
        
        lblConfNombre = Label(self.wind,text="Nueva contraseña:",bg=color_ventana)
        lblConfNombre.place(x=60, y=170)
        lblConfNombre.config(fg="white", bg=color_ventana,font=(fuente,11),height=1)
        
        self.entryPassNu = Entry(self.wind)
        self.entryPassNu.place(x=260,y=170)
        self.entryPassNu.config(font=(fuente,12),width=30,justify="left", show="*")
        
        lblPass = Label(self.wind,text="Confirma contraseña:",bg=color_ventana)
        lblPass.place(x=60, y=210)
        lblPass.config(fg="white", bg=color_ventana,font=(fuente,11),height=1)
        
        self.entryPassConf = Entry(self.wind)
        self.entryPassConf.place(x=260,y=210)
        self.entryPassConf.config(font=(fuente,12),width=30,justify="left", show="*")
        
        largo_btns = 16
        ancho_btns = 2
        BtnGuardar = Button(self.wind,activebackground= "gray",text="Guardar Cambios",command=self.guardarCambios,width=largo_btns, height=ancho_btns,cursor="hand2",font=(fuente,10,"bold"))
        BtnGuardar.place(x=140, y=260)
        BtnCancelar = Button(self.wind,activebackground= "gray",text="Cancelar",command=self.cancelar,width=largo_btns, height=ancho_btns,cursor="hand2",font=(fuente,10,"bold"))
        BtnCancelar.place(x=360, y=260)
        
        lblPolUso = Label(self.wind, text="Políticas de uso", bg = "blue", font=('Helveticabold', 9), fg="white", cursor="hand2")
        lblPolUso.place(x=45, y=330)
        lblPolUso.bind("<Button-1>", lambda e: self.funPolUso())
        
        window.mainloop()
        
    def cancelar(self):
        self.wind.destroy()
        modificar_cuenta.modificar_c()
        
    def guardarCambios(self):
        nomUserAc = (self.entryUserAc.get())
        userPassAc = (self.entryPassAc.get())
        userPassNu = (self.entryPassNu.get())
        userPassConf = (self.entryPassConf.get())
        if(not nomUserAc or not userPassAc or not userPassNu or not userPassConf):
            messagebox.showerror(message="Hay campos vacíos", title="Error")
        else:
            if(userPassNu == userPassConf):
                bandera = self.verifExistenciaUser(nomUserAc)
                if(bandera == 0):
                    messagebox.showerror(message="El usuario no está registrado en la Base de Datos, verifica los datos por favor", title="Usuario no encontrado")
                    os.system('cls')
                else:
                    bandera3 = self.verifDatosUser(nomUserAc, userPassAc)
                    if(bandera3 != 0):
                        messagebox.showerror(message="La contraseña actual es incorrecta", title="Contraseña Incorrecta")
                        os.system('cls')
                    else:
                        self.actualizarPass(nomUserAc, userPassNu)
                        self.wind.destroy()
                        os.system('cls')
                        modificar_cuenta.modificar_c()
            else:
                messagebox.showerror(message="Las contraseñas ingresadas no coinciden no coinciden", title="Error")
                os.system('cls')
        
    def verifExistenciaUser(self, nomUserAc):
         global host, userbd, passbd, nombd, portbd
         try:
             #connection = pymysql.connect(host="localhost", user="root", passwd="", database="cifrador")
             connection = pymysql.connect(host=host, user=userbd, passwd=passbd, database=nombd, port= portbd)
             cursor = connection.cursor()
             select = "SELECT COUNT(*) from usuarios where NombreUsuario = '" + nomUserAc + "';"
             cursor.execute(select)
             resultado = cursor.fetchone()
             resultadofinal = resultado[0]
             cursor.close()
             connection.commit()
             connection.close()
             return resultadofinal
         except pymysql.Error:
             messagebox.showerror(message="Ha ocurrido un error al conectar con la base de datos\nVuelve a intentarlo por favor.", title="Error SQL")
         
             
             
    def verifDatosUser(self, nomUserAc, passAc):
        global host, userbd, passbd, nombd, portbd
        try:
            #connection = pymysql.connect(host="localhost", user="root", passwd="", database="cifrador")
            connection = pymysql.connect(host=host, user=userbd, passwd=passbd, database=nombd, port = portbd)
            cursor = connection.cursor()
            select = "SELECT NombreUsuario, Password from usuarios where NombreUsuario = '" + nomUserAc + "';"
            cursor.execute(select)
            resultado = cursor.fetchall()
            for a in resultado:
                nombreUsuario = a[0]
                passUsuario = a[1]

            ph = PasswordHasher(time_cost=3, memory_cost=2**16, parallelism=8, hash_len=32, salt_len=16)
            try:
                if(nomUserAc == nombreUsuario):
                    if(ph.verify(passUsuario, passAc)):
                        resultadofinal = 0
                    else:
                        resultadofinal = 1
                    if(ph.check_needs_rehash(passUsuario)):
                        rehash = ph.hash(passUsuario)
                        self.actuPass(nomUserAc, rehash)
                else:
                    resultadofinal = 1
                cursor.close()
                connection.commit()
                connection.close()
                return resultadofinal
            except:
                #messagebox.showerror(message="Ha ocurrido un error de autenticación.", title="Error")
                resultadofinal = 1
        except pymysql.Error:
            messagebox.showerror(message="Ha ocurrido un error al conectar con la base de datos\nVuelve a intentarlo por favor.", title="Error SQL")
        

    def actuPass(self, nomUser, acPass):
        global host, userbd, passbd, nombd, portbd
        print("Conectando con la base de datos...\nEspera un momento...\n\n")
        try:
            #connection = pymysql.connect(host="localhost", user="root", passwd="", database="cifrador")
            connection = pymysql.connect(host=host, user=userbd, passwd=passbd, database=nombd, port = portbd)
            cursor = connection.cursor()
            update = "UPDATE usuarios set Password = '" + acPass + "' where NombreUsuario = '"+ nomUser +"';"
            cursor.execute(update)
            cursor.close()
            connection.commit()
            connection.close()
        except pymysql.Error:
            messagebox.showerror(message="Ha ocurrido un error al conectar con la base de datos\nVuelve a intentarlo por favor.", title="Error SQL")
                

    def actualizarPass(self, nomUserAc, userPassNu):
        global host, userbd, passbd, nombd, portbd
        ph = PasswordHasher(time_cost=3, memory_cost=2**16, parallelism=8, hash_len=32, salt_len=16)
        clave_hash = ph.hash(userPassNu)
        try:
            #connection = pymysql.connect(host="localhost", user="root", passwd="", database="cifrador")
            connection = pymysql.connect(host=host, user=userbd, passwd=passbd, database=nombd, port = portbd)
            cursor = connection.cursor()
            update = "UPDATE usuarios set Password = '" + clave_hash + "' where NombreUsuario = '"+ nomUserAc +"';"
            cursor.execute(update)
            messagebox.showinfo(message="La actualización ha sido éxitosa", title="Cambios Guardados")
            cursor.close()
            connection.commit()
            connection.close()
        except pymysql.Error:
            messagebox.showerror(message="Ha ocurrido un error al conectar con la base de datos\nVuelve a intentarlo por favor.", title="Error SQL")
        
    def funPolUso(self):
        politicaUso.nuevo()
        
#if __name__ == '__main__':
   #ventana = Tk()
#   c_password()
   #ventana.mainloop()'''