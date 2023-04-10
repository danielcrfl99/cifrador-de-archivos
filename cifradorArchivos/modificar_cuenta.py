from tkinter import ttk
from tkinter import Label, Button, Tk
from PIL import Image, ImageTk
import home
import c_n_usuario
import cambiar_correo
import cambiar_password
import borrar_cuenta
from obArchivos import resource_Path
import politicaUso

color_etiqueta = ("black")
fuente = "Century Gothic"
color_ventana=("blue")

class modificar_c:
    def __init__(self):
        window = Tk()
        self.wind = window
        self.wind.title("Modificar Cuenta")
        self.wind.resizable(0,0)
        self.wind.geometry("620x380")
        self.wind.configure(background="blue")
        
        path = resource_Path("fondo.png")
        image = Image.open(path)
        resize_image = image.resize((620, 380))
        img = ImageTk.PhotoImage(resize_image)
        labelfondo = Label(self.wind, image = img)
        labelfondo.place(x=-2, y=0)
        
        lblTitulo=Label(self.wind,text="Modificar Cuenta", bg="blue")
        lblTitulo.place(x=200,y=5)
        lblTitulo.config(fg="white",font=(fuente,20, "bold"),height=1)
        
       # BtnSel = Button(self.wind,bg="gray",text="Seleccionar",font=(fuente,11,"bold")).place(x=475, y=88)
        largo_btns = 14
        ancho_btns = 4
        BtnMNU = Button(self.wind,activebackground= "gray",text="Modificar\n nombre de\n usuario",command=self.mod_NombreUser,width=largo_btns, height=ancho_btns,cursor="hand2",font=(fuente,8,"bold"))
        BtnMNU.place(x=150, y=80)
        BtnMCE = Button(self.wind,activebackground= "gray",text="Modificar correo \n electrónico",command=self.mod_Correo,width=largo_btns, height=ancho_btns,cursor="hand2",font=(fuente,8,"bold"))
        BtnMCE.place(x=350, y=80)
        BtnCC = Button(self.wind,activebackground= "gray",text="Cambiar \ncontraseña",command=self.mod_Pass,width=largo_btns, height=ancho_btns,cursor="hand2",font=(fuente,8,"bold"))
        BtnCC.place(x=150, y=170)
        BtnEC = Button(self.wind,activebackground= "gray",text="Eliminar cuenta",command=self.eliminar,width=largo_btns, height=ancho_btns,cursor="hand2",font=(fuente,8,"bold"))
        BtnEC.place(x=350, y=170)
        BtnSalir = Button(self.wind,activebackground= "gray",text="Salir",command=self.salir,width=10, height=2,cursor="hand2",font=(fuente,10,"bold"))
        BtnSalir.place(x=260, y=260)
        lblPolUso = Label(self.wind, text="Políticas de uso", bg = "blue", font=('Helveticabold', 9), fg="white", cursor="hand2")
        lblPolUso.place(x=45, y=330)
        lblPolUso.bind("<Button-1>", lambda e: self.funPolUso())
        
        window.mainloop()
        
    def mod_NombreUser(self):
        self.wind.destroy()
        c_n_usuario.c_n_usuario()
    
    def mod_Correo(self):
        self.wind.destroy()
        cambiar_correo.c_correo()
        
    def mod_Pass(self):
        self.wind.destroy()
        cambiar_password.c_password()
        
    def eliminar(self):
        self.wind.destroy()
        borrar_cuenta.elim_cuenta()
    
    def salir(self):
        self.wind.destroy()
        home.home_int()
        
    def funPolUso(self):
        politicaUso.nuevo()  
        
        
#if __name__ == '__main__':
   #ventana = Tk()
#   modificar_c()
   #ventana.mainloop()'''