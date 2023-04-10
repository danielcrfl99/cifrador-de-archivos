from tkinter import ttk
from tkinter import Label, Button, Tk, messagebox
from PIL import Image, ImageTk
import crear_cuenta
import iniciar_sesion
import modificar_cuenta
from obArchivos import resource_Path
import politicaUso
import subprocess
import os

color_etiqueta = ("black")
fuente = "Century Gothic"
color_ventana=("blue")

class home_int:
    def __init__(self):
        window = Tk()
        self.wind = window
        self.wind.title("Cifrador de Archivos")
        self.wind.resizable(0,0)
        self.wind.geometry("520x300")
        self.wind.configure(background="royalblue")
        #self.wind.wm_attributes("-transparentcolor", 'green')
        #img = PhotoImage(file = "fondo.png")
        #labelfondo = Label(self.wind, image = img)
        #labelfondo.place(x=0, y=0)
        path = resource_Path("fondo.png")
        image = Image.open(path)
        resize_image = image.resize((520, 300))
        img = ImageTk.PhotoImage(resize_image)
        labelfondo = Label(self.wind, image = img)
        labelfondo.place(x=-2, y=0)
        
        lblTitulo=Label(self.wind, bg = color_ventana,  text="Sistema de Cifrado de Archivos")
        lblTitulo.place(x=90,y=5)
        lblTitulo.config(fg="white",font=(fuente,16, "bold"),height=1)
        #lblTitulo.wm_attributes('-transparentcolor', 'green')
        
        largo_btns = 9
        ancho_btns = 2
        BtnValid = Button(self.wind,activebackground= "gray",text="Crear \nCuenta", command=self.crearCuenta,width=largo_btns,height=ancho_btns,cursor="hand2",font=(fuente,11,"bold"))
        BtnValid.place(x=70, y=140)
        BtnSalir = Button(self.wind,activebackground= "gray",text="Iniciar \nSesión", command=self.iniciarSesion,width=largo_btns,height=ancho_btns,cursor="hand2",font=(fuente,11,"bold"))
        BtnSalir.place(x=200, y=140)
        BtnEditar = Button(self.wind,activebackground= "gray",text="Modificar \nCuenta", command=self.modificar,width=largo_btns,height=ancho_btns,cursor="hand2",font=(fuente,11,"bold"))
        BtnEditar.place(x=330, y=140)
        lblPolUso = Label(self.wind, text="Políticas de uso", bg = "blue", font=('Helveticabold', 9), fg="white", cursor="hand2")
        lblPolUso.place(x=45, y=230)
        lblPolUso.bind("<Button-1>", lambda e : self.funPolUso())
        lblManUsu = Label(self.wind, text="¿Tienes dudas?\nConsulta nuestro manual de usuario", bg = "blue", font=('Helveticabold', 9), fg="white", cursor="hand2")
        lblManUsu.place(x=300, y=215)
        lblManUsu.bind("<Button-1>", lambda e : self.funManUsu())
        
        window.mainloop()
        
    def crearCuenta(self):
        self.wind.destroy()
        crear_cuenta.crear_cuenta()
    
    def iniciarSesion(self):
        self.wind.destroy()
        iniciar_sesion.ini_ses()
    
    def modificar(self):
        self.wind.destroy()
        modificar_cuenta.modificar_c()
    
    def funPolUso(self):
        politicaUso.nuevo()
        
    def funManUsu(self):
        print("Espera un momento por favor...")
        try:
            path= 'ManualUsuario.pdf'
            subprocess.Popen([path], shell=True)
        except:
            messagebox.showerror(message="No se ha podido abrir el archivo", title="Ha ocurrido un error")
        os.system('cls')
        
    
#if __name__ == '__main__':
    #window = Tk()
#    home_int()
    #window.mainloop()
        