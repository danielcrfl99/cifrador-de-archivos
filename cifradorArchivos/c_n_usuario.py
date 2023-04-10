from tkinter import ttk
from tkinter import Label, Button, messagebox, Entry, Tk
from PIL import Image, ImageTk
import modificar_cuenta
import pymysql
from argon2 import PasswordHasher
from obArchivos import resource_Path
import politicaUso
import os

fuente = "Century Gothic"
color_ventana=("blue")
color_etiqueta = ("black")

class c_n_usuario:
    def __init__(self):
        window = Tk()
        self.wind = window
        self.wind.title("Menú")
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
        
        lblTitulo=Label(self.wind,text="Cambiar Nombre de Usuario", bg="blue")
        lblTitulo.place(x=108,y=5)
        lblTitulo.config(fg="white",font=(fuente,20, "bold"),height=1)
        
        lblNombreAc = Label(self.wind,text="Nombre de usuario actual:",bg=color_ventana)
        lblNombreAc.place(x=20, y=90)
        lblNombreAc.config(fg="white", bg=color_ventana,font=(fuente,11),height=1)
        
        self.entryUserAc = Entry(self.wind)
        self.entryUserAc.place(x=260,y=90)
        self.entryUserAc.config(font=(fuente,12),width=30,justify="left")
        
        lblNombreNu = Label(self.wind,text="Nuevo nombre de usuario:",bg=color_ventana)
        lblNombreNu.place(x=20, y=130)
        lblNombreNu.config(fg="white", bg=color_ventana,font=(fuente,11),height=1)
        
        self.entryUserNu = Entry(self.wind)
        self.entryUserNu.place(x=260,y=130)
        self.entryUserNu.config(font=(fuente,12),width=30,justify="left")
        
        lblConfNombre = Label(self.wind,text="Confirma nombre de usuario:",bg=color_ventana)
        lblConfNombre.place(x=20, y=170)
        lblConfNombre.config(fg="white", bg=color_ventana,font=(fuente,11),height=1)
        
        self.entryUserConf = Entry(self.wind)
        self.entryUserConf.place(x=260,y=170)
        self.entryUserConf.config(font=(fuente,12),width=30,justify="left")
        
        lblPass = Label(self.wind,text="Ingresa tu contraseña:",bg=color_ventana)
        lblPass.place(x=20, y=210)
        lblPass.config(fg="white", bg=color_ventana,font=(fuente,11),height=1)
        
        self.entryPass = Entry(self.wind)
        self.entryPass.place(x=260,y=210)
        self.entryPass.config(font=(fuente,12),width=30,justify="left", show="*")
        
        largo_btns = 16
        ancho_btns = 2
        BtnGuardar = Button(self.wind,activebackground= "gray",text="Guardar Cambios",command=self.guardarCambios,width=largo_btns, height=ancho_btns,cursor="hand2",font=(fuente,10,"bold"))
        BtnGuardar.place(x=140, y=260)
        BtnCancelar = Button(self.wind,activebackground= "gray",text="Cancelar", command=self.cancelar, width=largo_btns, height=ancho_btns,cursor="hand2",font=(fuente,10,"bold"))
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
        nombreUserNu = (self.entryUserNu.get())
        userNuConf = (self.entryUserConf.get())
        passUser = (self.entryPass.get())
        if(not nomUserAc or not nombreUserNu or not userNuConf or not passUser):
            messagebox.showerror(message="Hay campos vacíos", title="Error")
        else:
            if(nombreUserNu == userNuConf):
                bandera = self.verifExistenciaUser(nomUserAc)
                bandera2 = self.verifExistenciaUser(userNuConf)
                if(bandera == 0):
                    messagebox.showerror(message="El usuario no está registrado en la Base de Datos, verifica los datos por favor", title="Usuario no encontrado")
                    os.system('cls')
                else:
                    if(bandera2 != 0):
                        messagebox.showerror(message="El nombre de usuario seleccionado ya está registrado, intenta con otro nombre de usuario por favor", title="Usuario Existente")
                        os.system('cls')
                    else:
                        bandera3 = self.verifDatosUser(nomUserAc, passUser)
                        if(bandera3 != 0):
                            messagebox.showerror(message="La contraseña es incorrecta", title="Contraseña Incorrecta")
                        else:
                            #print("Se realizará el proceso de actualización")
                            self.actualizarNomUser(nomUserAc, nombreUserNu, passUser)
                            self.wind.destroy()
                            os.system('cls')
                            modificar_cuenta.modificar_c()
            else:
                messagebox.showerror(message="Los nombres de usuario no coinciden", title="Error")
                os.system('cls')
            
    def verifExistenciaUser(self, nomUser):
        global host, userbd, passbd, nombd, portbd
        try:
            #connection = pymysql.connect(host="localhost", user="root", passwd="", database="cifrador")
            connection = pymysql.connect(host=host, user=userbd, passwd=passbd, database=nombd, port=portbd)
            cursor = connection.cursor()
            select = "SELECT COUNT(*) from usuarios where NombreUsuario = '" + nomUser + "';"
            cursor.execute(select)
            resultado = cursor.fetchone()
            resultadofinal = resultado[0]
            cursor.close()
            connection.commit()
            connection.close()
            return resultadofinal
        except pymysql.Error:
            messagebox.showerror(message="Ha ocurrido un error al conectar con la base de datos\nVuelve a intentarlo por favor.", title="Error SQL")
            
                
    def verifDatosUser(self, nomUserAc, passUser):
        global host, userbd, passbd, nombd, portbd
        print("Verificando los datos ingresados...\nEspera un momento...\n\n")
        try:
            #connection = pymysql.connect(host="localhost", user="root", passwd="", database="cifrador")
            connection = pymysql.connect(host=host, user=userbd, passwd=passbd, database=nombd, port=portbd)
            cursor = connection.cursor()
            select = "SELECT NombreUsuario, Password from usuarios where NombreUsuario = '" + nomUserAc + "';"
            cursor.execute(select)
            resultado = cursor.fetchall()
            for a in resultado:
                nombreUsuario = a[0]
                passUsuario = a[1]
            #print("Datos entrantes, nombre Usuario: "+ nomUserAc+ " Pass: "+ passUser)
            #print("Datos de la base: "+ nombreUsuario + "Pass: "+ passUsuario)
            ph = PasswordHasher(time_cost=3, memory_cost=2**16, parallelism=8, hash_len=32, salt_len=16)
            try:
                if(nomUserAc == nombreUsuario):
                    if(ph.verify(passUsuario, passUser)):
                        resultadofinal = 0
                    else:
                        resultadofinal = 1
                    if(ph.check_needs_rehash(passUsuario)):
                        rehash = ph.hash(passUsuario)
                        self.actuPass(nomUserAc, rehash)
                else:
                    resultadofinal = 1
            except:
                #messagebox.showerror(message="Error de autenticación.", title="Error")
                resultadofinal = 1
            return resultadofinal
        except pymysql.Error:
            messagebox.showerror(message="Ha ocurrido un error al conectar con la base de datos\nVuelve a intentarlo por favor.", title="Error SQL")
        finally:
            connection.commit()
            connection.close()
            
    def actuPass(self, nomUser, acPass):
        global host, userbd, passbd, nombd, portbd
        try:
            #connection = pymysql.connect(host="localhost", user="root", passwd="", database="cifrador")
            connection = pymysql.connect(host=host, user=userbd, passwd=passbd, database=nombd, port=portbd)
            cursor = connection.cursor()
            update = "UPDATE usuarios set Password = '" + acPass + "' where NombreUsuario = '"+ nomUser +"';"
            cursor.execute(update)
            cursor.close()
            connection.commit()
            connection.close()
        except pymysql.Error:
            messagebox.showerror(message="Ha ocurrido un error al conectar con la base de datos\nVuelve a intentarlo por favor.", title="Error SQL")
        
        
    def actualizarNomUser(self, nomUserAc, nombreUserNu, passUser):
        global host, userbd, passbd, nombd, portbd
        print("Conectando con la base de datos\nEspera un momento...")
        try:
            #connection = pymysql.connect(host="localhost", user="root", passwd="", database="cifrador")
            connection = pymysql.connect(host=host, user=userbd, passwd=passbd, database=nombd, port=portbd)
            cursor = connection.cursor()
            update = "UPDATE usuarios set NombreUsuario = '" + nombreUserNu + "' where NombreUsuario = '"+ nomUserAc +"';"
            cursor.execute(update)
            messagebox.showinfo(message="La actualización ha sido éxitosa", title="Cambios Guardados")
        except pymysql.Error:
            messagebox.showerror(message="Ha ocurrido un error al conectar con la base de datos\nVuelve a intentarlo por favor.", title="Error SQL")
        finally:
            connection.commit()
            connection.close()
        
    def funPolUso(self):
        politicaUso.nuevo()
        
#if __name__ == '__main__':
   #ventana = Tk()
#   c_n_usuario()
   #ventana.mainloop()'''