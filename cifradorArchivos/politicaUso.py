from tkinter import Tk, Text, Label, Button
import tkinter.font as tkFont
from PIL import Image, ImageTk
from obArchivos import resource_Path

def nuevo():
    global ventanaNueva
    ventanaNueva = Tk()
    ventanaNueva.geometry("720x400")
    ventanaNueva.resizable(False, False)
    ventanaNueva.title("Políticas de Uso")
    ventanaNueva.configure(background = "white")
    

    
    text=Text(ventanaNueva, width = 68, height=1)
    text.place(x=00, y=00)    
    #myFont = tkFont.Font(family="Times New Roman", size=20, weight="bold", slant="italic")
    text.config(font=("Times New Roman",20,"bold", "italic"))
    text.insert('1.0', "\t\tPolíticas de Uso\n\n")
    text.config(state="disabled")

    texto = "\tEn el TT2021-A031:\n\n\tNo nos hacemos responsables del uso que de a la información que ingrese\n\teste desarrollo, y su uso estará sujeto a su autorización, conforme al Artículo\n\t16 de la Constitución Política de los Estados Unidos Mexicanos."
    texto2 = texto+"\n\n\tSe debe realizar un tratamiento de la información ingresada para poder\n\tproporcionarle el servicio de cifrado-descifrado, pero en ningún momento\n\testará disponible a terceros y se emplea de manera exclusiva para la puesta en\n\tmarcha de los algoritmos empleados en el sistema. El tipo de información que\n\trecopilamos depende de la forma en la que utiliza nuestro servicio."
    text2 = Text(ventanaNueva, width = 80, height=15)
    text2.place(x=0, y=66)
    text2.config(font=("Times New Roman",14))
    text2.tag_configure('tag-center', justify='center')
    text2.insert('1.0', texto2)
    text2.config(state="disabled")
    
    BtnCerrar = Button(ventanaNueva,activebackground= "gray", bg= "gray", text="Salir",command=salir,width=10, height=2,cursor="hand2",font=("Century Gothic",10,"bold"))
    BtnCerrar.place(x=560, y=340)
    ventanaNueva.mainloop()
    
def salir():
    global ventanaNueva
    ventanaNueva.destroy()
