from tkinter import ttk, messagebox
from tkinter import Label, Button, Tk, Entry
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from PIL import Image, ImageTk
import iniciar_sesion
import smtplib
import pymysql
import string
import random
from argon2 import PasswordHasher
from obArchivos import resource_Path
import os

fuente = "Century Gothic"
color_etiqueta = ("black")
color_ventana=("blue")


class rec_pass:
    def __init__(self):
        window = Tk()
        self.wind = window
        self.wind.title("Recuperar Contraseña")
        self.wind.resizable(0,0)
        self.wind.geometry("620x370")
        self.wind.configure(background="blue")
        
        #img = PhotoImage(file = "fondo.png")
        #labelfondo = Label(self.wind, image = img)
        #labelfondo.place(x=0, y=0)
        path = resource_Path("fondo.png")
        image = Image.open(path)
        resize_image = image.resize((620, 370))
        img = ImageTk.PhotoImage(resize_image)
        labelfondo = Label(self.wind, image = img)
        labelfondo.place(x=-2, y=0)
        
        global host, userbd, passbd, nombd, portbd
        host = "brfvvzvjp0x6ye5yzxsa-mysql.services.clever-cloud.com"
        nombd = "brfvvzvjp0x6ye5yzxsa"
        userbd = "u2w8flswhjfoqbf0"
        passbd = "RuhbO7yQ9p7H3AzZ2Eud"
        portbd = 21401
        
        lblTitulo=Label(self.wind,text="Recuperar Contraseña",bg=color_ventana)
        lblTitulo.place(x=180,y=10)
        lblTitulo.config(fg="white", bg=color_ventana,font=(fuente,20, "bold"),height=1)
        
        lblInicio = Label(self.wind,text="Nombre de Usuario:",bg=color_ventana)
        lblInicio.place(x=100, y=90)
        lblInicio.config(fg="white", bg=color_ventana,font=(fuente,12, "bold"),height=1)
        
        self.entryUser = Entry(self.wind)
        self.entryUser.place(x=270,y=90)
        self.entryUser.config(font=(fuente,12),width=30,justify="left")
        
        btnIngresar = Button(self.wind,activebackground= "gray",text="Confirmar", command=self.ingresar, cursor="hand2",font=(fuente,12,"bold"))
        btnIngresar.place(x=190, y=200)
        btnRegresar = Button(self.wind,activebackground= "gray",text="Cancelar", command=self.cancelar, cursor="hand2",font=(fuente,12,"bold"))
        btnRegresar.place(x=300, y=200)
        
        window.mainloop()
    
        
    def cancelar(self):
        self.wind.destroy()
        iniciar_sesion.ini_ses()
        
    def ingresar(self):
        nombreUser = (self.entryUser.get())
        if(not nombreUser):
            messagebox.showerror(message="Hay campos vacíos", title="Campos vacíos")
        else:
            bandera = self.verifExistenciaUser(nombreUser)
            if(bandera == 0):
                messagebox.showerror(message="El usuario no está registrado", title="Usuario no encontrado")
            else:
                nuevaPass = self.generarNuevaPass()
                correo = self.recopilarDatos(nombreUser)
                #print(correo)
                #print(password)
                confirmacion = self.actualizarInfo(nombreUser, nuevaPass)
                if(confirmacion == 1):
                    self.mandarCorreo(correo, nuevaPass)
                    self.wind.destroy()
                    os.system('cls')
                    iniciar_sesion.ini_ses()
                else:
                    messagebox.showerror(message="Ha ocurrido un error, vuelve a intentarlo.", title="Error")
                    os.system('cls')
        
    def actualizarInfo(self, nombreUser, nuevaPass):
        global host, userbd, passbd, nombd, portbd
        ph = PasswordHasher(time_cost=3, memory_cost=2**16, parallelism=8, hash_len=32, salt_len=16)
        clave_hash = ph.hash(nuevaPass)
        print("Espera un momento...\n")
        try:
            #connection = pymysql.connect(host="localhost", user="root", passwd="", database="cifrador")
            connection = pymysql.connect(host=host, user=userbd, passwd=passbd, database=nombd, port = portbd)
            cursor = connection.cursor()
            update = "UPDATE usuarios set Password = '" + clave_hash + "' where NombreUsuario = '"+ nombreUser +"';"
            cursor.execute(update)
            cursor.close()
            connection.commit()
            connection.close()
            return 1
        except pymysql.Error:
            return 0
    
    def generarNuevaPass(self):
        length_of_string = 8
        cadena = ''.join(random.choice(string.ascii_letters + string.digits) for _ in range(length_of_string)).lower()
        return cadena
        
    def mandarCorreo(self, correo, password):
        message = "Se ha generado una nueva contraseña. Considera cambiarla.\nTu contraseña nueva es:\n\n\t" + password
        #subject = 'Prueba de correo'

        msg = MIMEMultipart()
        msg['From'] = "cifrador98@gmail.com"
        msg['To'] = correo
        msg['Subject'] = "Recuperación de contraseña"
        msg.attach(MIMEText(message,'plain'))
        server = smtplib.SMTP('smtp.gmail.com: 587')
        try:
            server.starttls()
            server.login(msg['From'], 'CifradorTT98>')
            server.sendmail(msg['From'], msg['To'], msg.as_string())
            messagebox.showinfo(message="Tu contraseña se ha enviado a tu correo electrónico", title="Correo enviado")
        except:
            messagebox.showerror(message="Ha ocurrido un error", title="Intentalo nuevamente")
        server.quit()
        
        
    def verifExistenciaUser(self, nomUser):
        global host, userbd, passbd, nombd, portbd
        try:
            #connection = pymysql.connect(host="localhost", user="root", passwd="", database="cifrador")
            connection = pymysql.connect(host=host, user=userbd, passwd=passbd, database=nombd, port = portbd)
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

    
    def recopilarDatos(self, nomUser):
        global host, userbd, passbd, nombd, portbd
        try:
            #connection = pymysql.connect(host="localhost", user="root", passwd="", database="cifrador")
            connection = pymysql.connect(host=host, user=userbd, passwd=passbd, database=nombd, port = portbd)
            cursor = connection.cursor()
            select = "SELECT Correo_electronico from usuarios where NombreUsuario = '" + nomUser + "';"
            cursor.execute(select)
            resultado = cursor.fetchone()
            resultadofinal = resultado[0]
            cursor.close()
            connection.commit()
            connection.close()
            return resultadofinal
        except pymysql.Error:
            messagebox.showerror(message="Ha ocurrido un error al conectar con la base de datos\nVuelve a intentarlo por favor.", title="Error SQL")
    
#if __name__ == '__main__':
   #ventana = Tk()
#   rec_pass()
   #ventana.mainloop()