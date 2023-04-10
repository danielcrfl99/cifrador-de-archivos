import sys
import os
import io
from tkinter import ttk
from tkinter import Label, Tk, Button, Entry, filedialog, messagebox
from PIL import Image, ImageTk
import cifrar_archivo
import descifrar_archivo
import iniciar_sesion
from obArchivos import resource_Path
import politicaUso

fuente = "Century Gothic"
color_etiqueta = ("black")
color_ventana=("blue")

class menu_principal:
    def __init__(self, nomUser):
        ####Poner nomUser para que funcione en conjunto
        window = Tk()
        self.wind = window
        self.wind.title("Menú")
        self.wind.resizable(0,0)
        self.wind.geometry("620x350")
        self.wind.configure(background="blue")
        os.system('cls')
        global usuario
        usuario = nomUser
        #img = PhotoImage(file = "fondo.png")
        #labelfondo = Label(self.wind, image = img)
        #labelfondo.place(x=0, y=0)
        path = resource_Path("fondo.png")
        image = Image.open(path)
        resize_image = image.resize((620, 350))
        img = ImageTk.PhotoImage(resize_image)
        labelfondo = Label(self.wind, image = img)
        labelfondo.place(x=-2, y=0)
        
        lblTitulo=Label(self.wind,text="Menú", bg="blue")
        lblTitulo.place(x=260,y=5)
        lblTitulo.config(fg="white",font=(fuente,20, "bold"),height=1)
        
        lblArchivo = Label(self.wind,text="Archivo:",bg=color_ventana)
        lblArchivo.place(x=40, y=90)
        lblArchivo.config(fg="white", bg=color_ventana,font=(fuente,12, "bold"),height=1)
        
        self.entryUser = Entry(self.wind)
        self.entryUser.place(x=110,y=90)
        self.entryUser.config(font=(fuente,12),width=40,justify="left")
        
        BtnSel = Button(self.wind,activebackground= "gray",text="Seleccionar",command=self.sel,cursor="hand2",font=(fuente,11,"bold"))
        BtnSel.place(x=475, y=88)
        largo_btns = 8
        ancho_btns = 2
        BtnCifrar = Button(self.wind,activebackground= "gray",text="Cifrar",command=self.cif,width=largo_btns, height=ancho_btns,cursor="hand2",font=(fuente,11,"bold"))
        BtnCifrar.place(x=200, y=160)
        BtnDescifrar = Button(self.wind,activebackground= "gray",text="Descifrar",command=self.descif,width=largo_btns, height=ancho_btns,cursor="hand2",font=(fuente,11,"bold"))
        BtnDescifrar.place(x=350, y=160)
        BtnSalir = Button(self.wind,activebackground= "gray",text="Salir",command=self.salir,width=largo_btns, height=ancho_btns,cursor="hand2",font=(fuente,11,"bold"))
        BtnSalir.place(x=270, y=240)
        lblPolUso = Label(self.wind, text="Políticas de uso", bg = "blue", font=('Helveticabold', 9), fg="white", cursor="hand2")
        lblPolUso.place(x=45, y=310)
        lblPolUso.bind("<Button-1>", lambda e: self.funPolUso())
        #print(nomUser)
        
        window.mainloop()
        
    def salir(self):
        self.wind.destroy()
        iniciar_sesion.ini_ses()
        
    def sel(self):
        #print("Nuevo")
        filename = filedialog.askopenfilename(initialdir = "/",
                                              title = "Select a File",
                                              filetypes = (("All files",
                                                            "*.*"),))
        if filename:
            self.entryUser.delete(0, "end")
            self.entryUser.insert(0, filename)
        
    def cif(self):
        global usuario
        ruta = self.entryUser.get()
        if(not ruta):
            messagebox.showerror(message="No ha seleccionado ningún archivo.", title="Error")
        else:
            tipoArc = ruta.find('.encrypted')
            if(tipoArc == -1):
                self.wind.destroy()
                cifrar_archivo.cifrar_archivo(usuario, ruta, 1, "", "")
                #cifarc.cifrar_archivo(usuario, ruta)
            else:
                messagebox.showerror(message="Estas seleccionando un archivo cifrado.", title="Error")
        
                
        
    def descif(self):
        global usuario
        ruta = self.entryUser.get()
        if(not ruta):
            messagebox.showerror(message="No ha seleccionado ningún archivo.", title="Error")
        else:
            tipoArc = ruta.find('.encrypted')
            if(tipoArc != -1):
                self.wind.destroy()
                descifrar_archivo.descifrar_archivo(usuario, ruta, 2, "", "")
                #descif.descifrar_archivo(usuario, ruta)
            else:
                messagebox.showerror(message="Estas seleccionando un archivo que no esta cifrado.", title="Error")    


    def funPolUso(self):
        politicaUso.nuevo()       

#if __name__ == '__main__':
   #ventana = Tk()
#   menu_principal()
   #ventana.mainloop()'''