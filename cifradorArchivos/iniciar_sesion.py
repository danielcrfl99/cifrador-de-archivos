from tkinter import ttk
from tkinter import Label, Tk, Button, Entry, messagebox
import PIL.Image
import PIL.ImageTk
import home
import recuperar_pass
import pymysql
import menu
from argon2 import PasswordHasher
from obArchivos import resource_Path
from hilo import hilo
import os
import politicaUso

fuente = "Century Gothic"
color_etiqueta = ("black")
color_ventana=("blue")

class ini_ses:
    def __init__(self):
        window = Tk()
        self.wind = window
        self.wind.title("Iniciar sesión")
        self.wind.resizable(0,0)
        self.wind.geometry("620x370")
        self.wind.configure(background="blue")
        
        #img = PhotoImage(file = "fondo.png")
        #labelfondo = Label(self.wind, image = img)
        #labelfondo.place(x=0, y=0)
        path = resource_Path("fondo.png")
        image = PIL.Image.open(path)
        resize_image = image.resize((620, 370))
        img = PIL.ImageTk.PhotoImage(resize_image)
        labelfondo = Label(self.wind, image = img)
        labelfondo.place(x=-2, y=0)
        
        global host, userbd, passbd, nombd, portbd
        host = "brfvvzvjp0x6ye5yzxsa-mysql.services.clever-cloud.com"
        nombd = "brfvvzvjp0x6ye5yzxsa"
        userbd = "u2w8flswhjfoqbf0"
        passbd = "RuhbO7yQ9p7H3AzZ2Eud"
        portbd = 21401
        
        lblTitulo=Label(self.wind,text="Iniciar Sesión",bg=color_ventana)
        lblTitulo.place(x=220,y=10)
        lblTitulo.config(fg="white", bg=color_ventana,font=(fuente,20, "bold"),height=1)
        
        lblInicio = Label(self.wind,text="Usuario:",bg=color_ventana)
        lblInicio.place(x=140, y=90)
        lblInicio.config(fg="white", bg=color_ventana,font=(fuente,12, "bold"),height=1)
        
        self.entryUser = Entry(self.wind)
        self.entryUser.place(x=210,y=90)
        self.entryUser.config(font=(fuente,12),width=30,justify="left")
        
        lblPass = Label(self.wind,text="Contraseña:")
        lblPass.place(x=140, y=140)
        lblPass.config(fg="white", bg=color_ventana,font=(fuente,12, "bold"),height=1)
        
        self.entryPass = Entry(self.wind)
        self.entryPass.place(x=240,y=140)
        self.entryPass.config(font=(fuente,12),width=30,justify="left", show="*")
    
        btnOlPass = Button(self.wind,activebackground= "gray",text="Olvide mi contraseña", command=self.recuperar, cursor="hand2",font=(fuente,9,"bold"))
        btnOlPass.place(x=240, y=170)
        btnIngresar = Button(self.wind,activebackground= "gray",text="Ingresar", command=self.ingresar, cursor="hand2",font=(fuente,12,"bold"))
        btnIngresar.place(x=190, y=250)
        btnRegresar = Button(self.wind,activebackground= "gray",text="Regresar", command=self.regresar, cursor="hand2",font=(fuente,12,"bold"))
        btnRegresar.place(x=300, y=250)
        lblPolUso = Label(self.wind, text="Políticas de uso", bg = "blue", font=('Helveticabold', 9), fg="white", cursor="hand2")
        lblPolUso.place(x=45, y=310)
        lblPolUso.bind("<Button-1>", lambda e: self.funPolUso())
        
        window.mainloop()
       
    def regresar(self):
        self.wind.destroy()
        home.home_int()
     
    def recuperar(self):
        self.wind.destroy()
        recuperar_pass.rec_pass()
    
    def ingresar(self):
        nomUser = (self.entryUser.get())
        entrypass = (self.entryPass.get())
        if(not nomUser or not entrypass):
            messagebox.showerror(message="Hay campos vacíos", title="Error")
        else:
            bandera = self.verificar_user_ex(nomUser)

            if(bandera != 0):
                #ventananew = hilo.run()
                bandera3 = self.verifPassUser(nomUser, entrypass)
                #hilo.interrupt(ventananew)
                if(bandera3 != 0):
                    messagebox.showerror(message="El nombre de usuario o contraseña es incorrecto.", title="Datos Incorrectos")
                    os.system('cls')
                else:
                    self.wind.destroy()
                    os.system('cls')
                    menu.menu_principal(nomUser)
            else:
                messagebox.showinfo(message="No estas registrado. Crea una cuenta", title="No estas registrado")
                os.system('cls')
            
    def verificar_user_ex(self, nomUser):
        global host, userbd, passbd, nombd, portbd
        try:
            #connection = pymysql.connect(host="localhost", user="root", passwd="", database="cifrador")
            connection = pymysql.connect(host=host, user=userbd, passwd=passbd, database=nombd, port = portbd)
            cursor = connection.cursor()
            select = "SELECT COUNT(*) from usuarios where NombreUsuario = '" + nomUser + "';"
            cursor.execute(select)
            resultado = cursor.fetchone()
            resultadofinal = resultado[0]
            return resultadofinal
        except pymysql.Error:
            messagebox.showerror(message="Ha ocurrido un error al conectar con la base de datos\nVuelve a intentarlo por favor.", title="Error SQL")
        
    def verifPassUser(self, nomUser, passentry):
        global host, userbd, passbd, nombd, confVoz, portbd
        os.system("cls")
        print("Espera un momento por favor...")
        try:
            #connection = pymysql.connect(host="localhost", user="root", passwd="", database="cifrador")
            connection = pymysql.connect(host=host, user=userbd, passwd=passbd, database=nombd, port = portbd)
            cursor = connection.cursor()
            select = "SELECT Password from usuarios where NombreUsuario = '" + nomUser + "';"
            cursor.execute(select)
            resultado = cursor.fetchone()
            passUsuario = resultado[0]
            #print("Datos entrantes, nombre Usuario: "+ nomUserAc+ " Pass: "+ passUser)
            #print("Datos de la base: "+ nombreUsuario + "Pass: "+ passUsuario)
            ph = PasswordHasher(time_cost=3, memory_cost=2**16, parallelism=8, hash_len=32, salt_len=16)
            try:
                confVoz = ph.verify(passUsuario, passentry)
                if(ph.verify(passUsuario, passentry)):
                    os.system("cls")
                    resultadofinal = 0
                else:
                    os.system("cls")
                    resultadofinal = 1
                if(ph.check_needs_rehash(passUsuario)):
                    rehash = ph.hash(passUsuario)
                    self.actuPass(nomUser, rehash)
                #return resultadofinal
            except:
                os.system("cls")
                resultadofinal = 1
            return resultadofinal
            cursor.close()
            connection.commit()
            connection.close()
        except pymysql.Error:
            messagebox.showerror(message="Ha ocurrido un error al conectar con la base de datos\nVuelve a intentarlo por favor.", title="Error SQL")
        
        
    def actuPass(self, nomUser, acPass):
        global host, userbd, passbd, nombd, portbd
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
            
    def funPolUso(self):
        politicaUso.nuevo() 
        
        
#if __name__ == '__main__':
   #ventana = Tk()
#   ini_ses()
   #ventana.mainloop()'''