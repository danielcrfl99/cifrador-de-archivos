import sys
import os
import cifrar_archivo
import descifrar_archivo

import numpy as np
import tkinter as ttk
from tkinter import Tk, messagebox, Button, Label, Entry
from PIL import Image, ImageTk
from obArchivos import resource_Path
import politicaUso

color_ventana=("blue")
color_1 = "#40CCD0"
color_2 = "#D04040"
color_3 = "#D04086"
color_4 = "#D040B6"
color_5 = "#BC40D0"
color_6 = "#8440D0"
color_7 = "#4940D0"
color_8 = "#4097D0"
color_9 = "#40D084"
color_10 = "#40D04D"
color_11 = "#79D040"
color_12 = "#A2D040"
color_13 = "#C5D040"
color_14 = "#D0B640"

color_15 = "#D09940"
color_16 = "#D04040"
color_17 = "#AF1C3C"
color_18 = "#AF1C91"
color_19 = "#9C1CAF"
color_20 = "#731CAF"
color_21 = "#4A1CAF"
color_22 = "#1C32AF"
color_23 = "#1C5DAF"
color_24 = "#1C89AF"
color_25 = "#1CA9AF"
color_26 = "#1CAF76"
color_27 = "#1CAF47"
color_28 = "#21AF1C"

color_29 = "#65AF1C"
color_30 = "#AFAC1C"
color_31 = "#AF8B1C"
color_32 = "#AF5D91"
color_33 = "#AF3C1C"
color_34 = "#AF3C1C"
color_35 = "#B11052"
color_36 = "#B1108D"
color_37 = "#A510B1"
color_38 = "#7C10B1"
color_39 = "#4010B1"
color_40 = "#1019B1"
color_41 = "#1055B1"
color_42 = "#1096B1"

color_43 = "#10B1A2"
color_44 = "#10B16A"
color_45 = "#10B114"
color_46 = "#5CB110"
color_47 = "#97B110"
color_48 = "#B17810"
color_49 = "#C10BC4"
color_50 = "#440BC4"
color_51 = "#0B39C4"
color_52 = "#0BA2C4"
color_53 = "#0BC4A5"
color_54 = "#0BC44D"
color_55 = "#51C40B"
color_56 = "#C4C20B"

color_57 = "#C4A20B"
color_58 = "#E00B3A"
color_59 = "#E00B7C"
color_60 = "#E00BDE"
color_61 = "#AA0BE0"
color_62 = "#0B14E0"
color_63 = "#0B53E0"
color_64 = "#0B91E0"
color_65 = "#0B7CD8"
color_66 = "#0BE08D"
color_67 = "#97E00B"
color_68 = "#DDE00B"
color_69 = "#E0C30B"
color_70 = "#E0840B"

color_71 = "#E0590B"
color_72 = "#E01E01"
color_73 = "#FF0000"
color_74 = "#FF0054"
color_75 = "#FF008D"
color_76 = "#FF00BC"
color_77 = "#D600FF"
color_78 = "#8700FF"
color_79 = "#5C00FF"
color_80 = "#0000FF"
color_81 = "#003FFF"
color_82 = "#00ECFF"
color_83 = "#00FF00"
color_84 = "#61FF00"

color_85 = "#E09898"
color_86 = "#E098B3"
color_87 = "#E098DC"
color_88 = "#CB98E0"
color_89 = "#B398E0"
color_90 = "#98A2E0"
color_91 = "#98C1E0"
color_92 = "#98DBE0"
color_93 = "#98E0B9"
color_94 = "#9AE098"
color_95 = "#C4E098"
color_96 = "#D7E098"
color_97 = "#E0D498"
color_98 = "#E0B898"

color_99 = "#735050"
color_100 = "#735061"
color_101 = "#735064"
color_102 = "#6E5073"
color_103 = "#5C5073"
color_104 = "#505D73"
color_105 = "#506D73"
color_106 = "#50735D"
color_107 = "#547350"
color_108 = "#667350"
color_109 = "#737150"
color_110 = "#736750"
color_111 = "#FFFFFF"
color_112 = "#000000"
color_113 = "#265A27"
color_114 = "#265A50"
color_115 = "#265A78"
color_116 = "#265ABE"
color_117 = "#265AFF"
color_118 = "#C8C850"
color_119 = "#C864C8"
color_120 = "#C800EB"
color_121 = "#D23F00"
color_122 = "#D23F3C"
color_123 = "#D23F64"
color_124 = "#D23F93"
color_124 = "#D26400"
color_125 = "#D29800"
color_126 = "#D2BB00"
color_127 = "#D2D200"
color_128 = "#D2FF00"
color_129 = "#59C800"
color_130 = "#59C82C"
color_131 = "#59C864"
color_132 = "#020080"
color_133 = "#028980"
color_134 = "#025FC0"
color_135 = "#0226E7"
color_136 = "#02B1E7"
color_137 = "#1EDEFB"
color_138 = "#66C808"
color_139 = "#66E63A"
color_140 = "#751D3A"
color_141 = "#751D3A"
color_142 = "#758025"
color_143 = "#758025"
color_144 = "#8A1D31"
color_145 = "#306BE9"
color_146 = "#44011C"
color_147 = "#440179"
color_148 = "#6D0C51"
color_149 = "#80C951"
color_150 = "#80C980"
color_151 = "#0C0CC9"
color_152 = "#0C80C9"
color_153 = "#0DC8E9"
color_154 = "#0DC817"
color_155 = "#0DC859"
color_156 = "#52C859"
color_157 = "#52C813"
color_158 = "#08FF81"
color_159 = "#08DF0C"
color_160 = "#68DE57"
color_etiqueta = ("black")
fuente = "Century Gothic"

password = ""

class rgb_nueva:
    def __init__(self, usuario, ruta, bandera, aux, voz_aux):
    #def __init__(self):
        ventana = Tk()
        self.vent = ventana
        self.vent.title("Clave RGB")
        self.vent.resizable(0,0)
        self.vent.geometry("940x580")
        self.vent.configure(background=color_ventana)
        
        #img = PhotoImage(file = "fondo.png")
        #labelfondo = Label(self.vent, image = img)
        #labelfondo.place(x=0, y=0)
        path = resource_Path("fondo.png")
        image = Image.open(path)
        resize_image = image.resize((940, 580))
        img = ImageTk.PhotoImage(resize_image)
        labelfondo = Label(self.vent, image = img)
        labelfondo.place(x=-2, y=0)
        
        lblTitulo=Label(self.vent,text="Clave RGB",bg=color_ventana)
        lblTitulo.place(x=340,y=5)
        lblTitulo.config(fg="white", bg=color_ventana,font=(fuente,20, "bold"),height=1)
        
        lblNota=Label(self.vent,text="Selecciona mínimo 6 colores, máximo 25. Puedes seleccionar el mismo color múltiples veces.",bg=color_ventana)
        lblNota.place(x=40,y=50)
        lblNota.config(fg="white", bg=color_ventana,font=(fuente,11, "bold"),height=1)
        
        ##Cuadro contraseña
        #cpass=ttk.StringVar()
        self.entry = Entry(self.vent)
        self.entry.place(x=60,y=460)
        self.entry.config(font=(fuente,8),width=140,justify="left", show="*", state="disabled")
        
        global flag
        global route
        global contra
        global voz
        global user
        flag = bandera
        route = ruta
        contra = aux
        voz = voz_aux
        user = usuario
        
        #print(flag)
        ancho_botonE=4
        alto_botonE=2
        ##Diferencia entre botones a lo ancho = 53, alto = 48
        ##Primera línea
        btnColor1 = Button(self.vent,bg=color_1,width=ancho_botonE,height=alto_botonE,cursor="hand2",command=lambda: self.colores(color_1)).place(x=78, y=90)
        btnColor2 = Button(self.vent,bg=color_2,width=ancho_botonE,height=alto_botonE,cursor="hand2",command=lambda: self.colores(color_2)).place(x=117, y=90)
        btnColor3 = Button(self.vent,bg=color_3,width=ancho_botonE,height=alto_botonE,cursor="hand2",command=lambda: self.colores(color_3)).place(x=156, y=90)
        btnColor4 = Button(self.vent,bg=color_4,width=ancho_botonE,height=alto_botonE,cursor="hand2",command=lambda: self.colores(color_4)).place(x=195, y=90)
        btnColor5 = Button(self.vent,bg=color_5,width=ancho_botonE,height=alto_botonE,cursor="hand2",command=lambda: self.colores(color_5)).place(x=234, y=90)
        btnColor6 = Button(self.vent,bg=color_6,width=ancho_botonE,height=alto_botonE,cursor="hand2",command=lambda: self.colores(color_6)).place(x=273, y=90)
        btnColor7 = Button(self.vent,bg=color_7,width=ancho_botonE,height=alto_botonE,cursor="hand2",command=lambda: self.colores(color_7)).place(x=312, y=90)
        btnColor8 = Button(self.vent,bg=color_8,width=ancho_botonE,height=alto_botonE,cursor="hand2",command=lambda: self.colores(color_8)).place(x=351, y=90)
        btnColor9 = Button(self.vent,bg=color_9,width=ancho_botonE,height=alto_botonE,cursor="hand2",command=lambda: self.colores(color_9)).place(x=390, y=90)
        btnColor10 = Button(self.vent,bg=color_10,width=ancho_botonE,height=alto_botonE,cursor="hand2",command=lambda: self.colores(color_10)).place(x=429, y=90)
        btnColor11 = Button(self.vent,bg=color_11,width=ancho_botonE,height=alto_botonE,cursor="hand2",command=lambda: self.colores(color_11)).place(x=468, y=90)
        btnColor12 = Button(self.vent,bg=color_12,width=ancho_botonE,height=alto_botonE,cursor="hand2",command=lambda: self.colores(color_12)).place(x=507, y=90)
        btnColor13 = Button(self.vent,bg=color_13,width=ancho_botonE,height=alto_botonE,cursor="hand2",command=lambda: self.colores(color_13)).place(x=546, y=90)
        btnColor14 = Button(self.vent,bg=color_14,width=ancho_botonE,height=alto_botonE,cursor="hand2",command=lambda: self.colores(color_14)).place(x=585, y=90)
        ##Segunda línea
        btnColor15 = Button(self.vent,bg=color_15,width=ancho_botonE,height=alto_botonE,cursor="hand2",command=lambda: self.colores(color_15)).place(x=78, y=132)
        btnColor16 = Button(self.vent,bg=color_16,width=ancho_botonE,height=alto_botonE,cursor="hand2",command=lambda: self.colores(color_16)).place(x=117, y=132)
        btnColor17 = Button(self.vent,bg=color_17,width=ancho_botonE,height=alto_botonE,cursor="hand2",command=lambda: self.colores(color_17)).place(x=156, y=132)
        btnColor18 = Button(self.vent,bg=color_18,width=ancho_botonE,height=alto_botonE,cursor="hand2",command=lambda: self.colores(color_18)).place(x=195, y=132)
        btnColor19 = Button(self.vent,bg=color_19,width=ancho_botonE,height=alto_botonE,cursor="hand2",command=lambda: self.colores(color_19)).place(x=234, y=132)
        btnColor20 = Button(self.vent,bg=color_20,width=ancho_botonE,height=alto_botonE,cursor="hand2",command=lambda: self.colores(color_20)).place(x=273, y=132)
        btnColor21 = Button(self.vent,bg=color_21,width=ancho_botonE,height=alto_botonE,cursor="hand2",command=lambda: self.colores(color_21)).place(x=312, y=132)
        btnColor22 = Button(self.vent,bg=color_22,width=ancho_botonE,height=alto_botonE,cursor="hand2",command=lambda: self.colores(color_22)).place(x=351, y=132)
        btnColor23 = Button(self.vent,bg=color_23,width=ancho_botonE,height=alto_botonE,cursor="hand2",command=lambda: self.colores(color_23)).place(x=390, y=132)
        btnColor24 = Button(self.vent,bg=color_24,width=ancho_botonE,height=alto_botonE,cursor="hand2",command=lambda: self.colores(color_24)).place(x=429, y=132)
        btnColor25 = Button(self.vent,bg=color_25,width=ancho_botonE,height=alto_botonE,cursor="hand2",command=lambda: self.colores(color_25)).place(x=468, y=132)
        btnColor26 = Button(self.vent,bg=color_26,width=ancho_botonE,height=alto_botonE,cursor="hand2",command=lambda: self.colores(color_26)).place(x=507, y=132)
        btnColor27 = Button(self.vent,bg=color_27,width=ancho_botonE,height=alto_botonE,cursor="hand2",command=lambda: self.colores(color_27)).place(x=546, y=132)
        btnColor28 = Button(self.vent,bg=color_28,width=ancho_botonE,height=alto_botonE,cursor="hand2",command=lambda: self.colores(color_28)).place(x=585, y=132)
        ##Tercera línea
        btnColor29 = Button(self.vent,bg=color_29,width=ancho_botonE,height=alto_botonE,cursor="hand2",command=lambda: self.colores(color_29)).place(x=78, y=174)
        btnColor30 = Button(self.vent,bg=color_30,width=ancho_botonE,height=alto_botonE,cursor="hand2",command=lambda: self.colores(color_30)).place(x=117, y=174)
        btnColor31 = Button(self.vent,bg=color_31,width=ancho_botonE,height=alto_botonE,cursor="hand2",command=lambda: self.colores(color_31)).place(x=156, y=174)
        btnColor32 = Button(self.vent,bg=color_32,width=ancho_botonE,height=alto_botonE,cursor="hand2",command=lambda: self.colores(color_32)).place(x=195, y=174)
        btnColor33 = Button(self.vent,bg=color_33,width=ancho_botonE,height=alto_botonE,cursor="hand2",command=lambda: self.colores(color_33)).place(x=234, y=174)
        btnColor34 = Button(self.vent,bg=color_34,width=ancho_botonE,height=alto_botonE,cursor="hand2",command=lambda: self.colores(color_34)).place(x=273, y=174)
        btnColor35 = Button(self.vent,bg=color_35,width=ancho_botonE,height=alto_botonE,cursor="hand2",command=lambda: self.colores(color_35)).place(x=312, y=174)
        btnColor36 = Button(self.vent,bg=color_36,width=ancho_botonE,height=alto_botonE,cursor="hand2",command=lambda: self.colores(color_36)).place(x=351, y=174)
        btnColor37 = Button(self.vent,bg=color_37,width=ancho_botonE,height=alto_botonE,cursor="hand2",command=lambda: self.colores(color_37)).place(x=390, y=174)
        btnColor38 = Button(self.vent,bg=color_38,width=ancho_botonE,height=alto_botonE,cursor="hand2",command=lambda: self.colores(color_38)).place(x=429, y=174)
        btnColor39 = Button(self.vent,bg=color_39,width=ancho_botonE,height=alto_botonE,cursor="hand2",command=lambda: self.colores(color_39)).place(x=468, y=174)
        btnColor40 = Button(self.vent,bg=color_40,width=ancho_botonE,height=alto_botonE,cursor="hand2",command=lambda: self.colores(color_40)).place(x=507, y=174)
        btnColor41 = Button(self.vent,bg=color_41,width=ancho_botonE,height=alto_botonE,cursor="hand2",command=lambda: self.colores(color_41)).place(x=546, y=174)
        btnColor42 = Button(self.vent,bg=color_42,width=ancho_botonE,height=alto_botonE,cursor="hand2",command=lambda: self.colores(color_42)).place(x=585, y=174)
        ##Cuarta línea
        btnColor43 = Button(self.vent,bg=color_43,width=ancho_botonE,height=alto_botonE,cursor="hand2",command=lambda: self.colores(color_43)).place(x=78, y=216)
        btnColor44 = Button(self.vent,bg=color_44,width=ancho_botonE,height=alto_botonE,cursor="hand2",command=lambda: self.colores(color_44)).place(x=117, y=216)
        btnColor45 = Button(self.vent,bg=color_45,width=ancho_botonE,height=alto_botonE,cursor="hand2",command=lambda: self.colores(color_45)).place(x=156, y=216)
        btnColor46 = Button(self.vent,bg=color_46,width=ancho_botonE,height=alto_botonE,cursor="hand2",command=lambda: self.colores(color_46)).place(x=195, y=216)
        btnColor47 = Button(self.vent,bg=color_47,width=ancho_botonE,height=alto_botonE,cursor="hand2",command=lambda: self.colores(color_47)).place(x=234, y=216)
        btnColor48 = Button(self.vent,bg=color_48,width=ancho_botonE,height=alto_botonE,cursor="hand2",command=lambda: self.colores(color_48)).place(x=273, y=216)
        btnColor49 = Button(self.vent,bg=color_49,width=ancho_botonE,height=alto_botonE,cursor="hand2",command=lambda: self.colores(color_49)).place(x=312, y=216)
        btnColor50 = Button(self.vent,bg=color_50,width=ancho_botonE,height=alto_botonE,cursor="hand2",command=lambda: self.colores(color_50)).place(x=351, y=216)
        btnColor51 = Button(self.vent,bg=color_51,width=ancho_botonE,height=alto_botonE,cursor="hand2",command=lambda: self.colores(color_51)).place(x=390, y=216)
        btnColor52 = Button(self.vent,bg=color_52,width=ancho_botonE,height=alto_botonE,cursor="hand2",command=lambda: self.colores(color_52)).place(x=429, y=216)
        btnColor53 = Button(self.vent,bg=color_53,width=ancho_botonE,height=alto_botonE,cursor="hand2",command=lambda: self.colores(color_53)).place(x=468, y=216)
        btnColor54 = Button(self.vent,bg=color_54,width=ancho_botonE,height=alto_botonE,cursor="hand2",command=lambda: self.colores(color_54)).place(x=507, y=216)
        btnColor55 = Button(self.vent,bg=color_55,width=ancho_botonE,height=alto_botonE,cursor="hand2",command=lambda: self.colores(color_55)).place(x=546, y=216)
        btnColor56 = Button(self.vent,bg=color_56,width=ancho_botonE,height=alto_botonE,cursor="hand2",command=lambda: self.colores(color_56)).place(x=585, y=216)
        ##Quinta línea
        btnColor57 = Button(self.vent,bg=color_57,width=ancho_botonE,height=alto_botonE,cursor="hand2",command=lambda: self.colores(color_57)).place(x=78, y=258)
        btnColor58 = Button(self.vent,bg=color_58,width=ancho_botonE,height=alto_botonE,cursor="hand2",command=lambda: self.colores(color_58)).place(x=117, y=258)
        btnColor59 = Button(self.vent,bg=color_59,width=ancho_botonE,height=alto_botonE,cursor="hand2",command=lambda: self.colores(color_59)).place(x=156, y=258)
        btnColor60 = Button(self.vent,bg=color_60,width=ancho_botonE,height=alto_botonE,cursor="hand2",command=lambda: self.colores(color_60)).place(x=195, y=258)
        btnColor61 = Button(self.vent,bg=color_61,width=ancho_botonE,height=alto_botonE,cursor="hand2",command=lambda: self.colores(color_61)).place(x=234, y=258)
        btnColor62 = Button(self.vent,bg=color_62,width=ancho_botonE,height=alto_botonE,cursor="hand2",command=lambda: self.colores(color_62)).place(x=273, y=258)
        btnColor63 = Button(self.vent,bg=color_63,width=ancho_botonE,height=alto_botonE,cursor="hand2",command=lambda: self.colores(color_63)).place(x=312, y=258)
        btnColor64 = Button(self.vent,bg=color_64,width=ancho_botonE,height=alto_botonE,cursor="hand2",command=lambda: self.colores(color_64)).place(x=351, y=258)
        btnColor65 = Button(self.vent,bg=color_65,width=ancho_botonE,height=alto_botonE,cursor="hand2",command=lambda: self.colores(color_65)).place(x=390, y=258)
        btnColor66 = Button(self.vent,bg=color_66,width=ancho_botonE,height=alto_botonE,cursor="hand2",command=lambda: self.colores(color_66)).place(x=429, y=258)
        btnColor67 = Button(self.vent,bg=color_67,width=ancho_botonE,height=alto_botonE,cursor="hand2",command=lambda: self.colores(color_67)).place(x=468, y=258)
        btnColor68 = Button(self.vent,bg=color_68,width=ancho_botonE,height=alto_botonE,cursor="hand2",command=lambda: self.colores(color_68)).place(x=507, y=258)
        btnColor69 = Button(self.vent,bg=color_69,width=ancho_botonE,height=alto_botonE,cursor="hand2",command=lambda: self.colores(color_69)).place(x=546, y=258)
        btnColor70 = Button(self.vent,bg=color_70,width=ancho_botonE,height=alto_botonE,cursor="hand2",command=lambda: self.colores(color_70)).place(x=585, y=258)
        ##Sexta línea
        btnColor71 = Button(self.vent,bg=color_71,width=ancho_botonE,height=alto_botonE,cursor="hand2",command=lambda: self.colores(color_71)).place(x=78, y=300)
        btnColor72 = Button(self.vent,bg=color_72,width=ancho_botonE,height=alto_botonE,cursor="hand2",command=lambda: self.colores(color_72)).place(x=117, y=300)
        btnColor73 = Button(self.vent,bg=color_73,width=ancho_botonE,height=alto_botonE,cursor="hand2",command=lambda: self.colores(color_73)).place(x=156, y=300)
        btnColor74 = Button(self.vent,bg=color_74,width=ancho_botonE,height=alto_botonE,cursor="hand2",command=lambda: self.colores(color_74)).place(x=195, y=300)
        btnColor75 = Button(self.vent,bg=color_75,width=ancho_botonE,height=alto_botonE,cursor="hand2",command=lambda: self.colores(color_75)).place(x=234, y=300)
        btnColor76 = Button(self.vent,bg=color_76,width=ancho_botonE,height=alto_botonE,cursor="hand2",command=lambda: self.colores(color_76)).place(x=273, y=300)
        btnColor77 = Button(self.vent,bg=color_77,width=ancho_botonE,height=alto_botonE,cursor="hand2",command=lambda: self.colores(color_77)).place(x=312, y=300)
        btnColor78 = Button(self.vent,bg=color_78,width=ancho_botonE,height=alto_botonE,cursor="hand2",command=lambda: self.colores(color_78)).place(x=351, y=300)
        btnColor79 = Button(self.vent,bg=color_79,width=ancho_botonE,height=alto_botonE,cursor="hand2",command=lambda: self.colores(color_79)).place(x=390, y=300)
        btnColor80 = Button(self.vent,bg=color_80,width=ancho_botonE,height=alto_botonE,cursor="hand2",command=lambda: self.colores(color_80)).place(x=429, y=300)
        btnColor81 = Button(self.vent,bg=color_81,width=ancho_botonE,height=alto_botonE,cursor="hand2",command=lambda: self.colores(color_81)).place(x=468, y=300)
        btnColor82 = Button(self.vent,bg=color_82,width=ancho_botonE,height=alto_botonE,cursor="hand2",command=lambda: self.colores(color_82)).place(x=507, y=300)
        btnColor83 = Button(self.vent,bg=color_83,width=ancho_botonE,height=alto_botonE,cursor="hand2",command=lambda: self.colores(color_83)).place(x=546, y=300)
        btnColor84 = Button(self.vent,bg=color_84,width=ancho_botonE,height=alto_botonE,cursor="hand2",command=lambda: self.colores(color_84)).place(x=585, y=300)
        ##Septima línea
        btnColor85 = Button(self.vent,bg=color_85,width=ancho_botonE,height=alto_botonE,cursor="hand2",command=lambda: self.colores(color_85)).place(x=78, y=342)
        btnColor86 = Button(self.vent,bg=color_86,width=ancho_botonE,height=alto_botonE,cursor="hand2",command=lambda: self.colores(color_86)).place(x=117, y=342)
        btnColor87 = Button(self.vent,bg=color_87,width=ancho_botonE,height=alto_botonE,cursor="hand2",command=lambda: self.colores(color_87)).place(x=156, y=342)
        btnColor88 = Button(self.vent,bg=color_88,width=ancho_botonE,height=alto_botonE,cursor="hand2",command=lambda: self.colores(color_88)).place(x=195, y=342)
        btnColor89 = Button(self.vent,bg=color_89,width=ancho_botonE,height=alto_botonE,cursor="hand2",command=lambda: self.colores(color_89)).place(x=234, y=342)
        btnColor90 = Button(self.vent,bg=color_90,width=ancho_botonE,height=alto_botonE,cursor="hand2",command=lambda: self.colores(color_90)).place(x=273, y=342)
        btnColor91 = Button(self.vent,bg=color_91,width=ancho_botonE,height=alto_botonE,cursor="hand2",command=lambda: self.colores(color_91)).place(x=312, y=342)
        btnColor92 = Button(self.vent,bg=color_92,width=ancho_botonE,height=alto_botonE,cursor="hand2",command=lambda: self.colores(color_92)).place(x=351, y=342)
        btnColor93 = Button(self.vent,bg=color_93,width=ancho_botonE,height=alto_botonE,cursor="hand2",command=lambda: self.colores(color_93)).place(x=390, y=342)
        btnColor94 = Button(self.vent,bg=color_94,width=ancho_botonE,height=alto_botonE,cursor="hand2",command=lambda: self.colores(color_94)).place(x=429, y=342)
        btnColor95 = Button(self.vent,bg=color_95,width=ancho_botonE,height=alto_botonE,cursor="hand2",command=lambda: self.colores(color_95)).place(x=468, y=342)
        btnColor96 = Button(self.vent,bg=color_96,width=ancho_botonE,height=alto_botonE,cursor="hand2",command=lambda: self.colores(color_96)).place(x=507, y=342)
        btnColor97 = Button(self.vent,bg=color_97,width=ancho_botonE,height=alto_botonE,cursor="hand2",command=lambda: self.colores(color_97)).place(x=546, y=342)
        btnColor98 = Button(self.vent,bg=color_98,width=ancho_botonE,height=alto_botonE,cursor="hand2",command=lambda: self.colores(color_98)).place(x=585, y=342)
        ##Octava línea
        btnColor99 = Button(self.vent,bg=color_99,width=ancho_botonE,height=alto_botonE,cursor="hand2",command=lambda: self.colores(color_99)).place(x=78, y=384)
        btnColor100 = Button(self.vent,bg=color_100,width=ancho_botonE,height=alto_botonE,cursor="hand2",command=lambda: self.colores(color_100)).place(x=117, y=384)
        btnColor101 = Button(self.vent,bg=color_101,width=ancho_botonE,height=alto_botonE,cursor="hand2",command=lambda: self.colores(color_101)).place(x=156, y=384)
        btnColor102 = Button(self.vent,bg=color_102,width=ancho_botonE,height=alto_botonE,cursor="hand2",command=lambda: self.colores(color_102)).place(x=195, y=384)
        btnColor103 = Button(self.vent,bg=color_103,width=ancho_botonE,height=alto_botonE,cursor="hand2",command=lambda: self.colores(color_103)).place(x=234, y=384)
        btnColor104 = Button(self.vent,bg=color_104,width=ancho_botonE,height=alto_botonE,cursor="hand2",command=lambda: self.colores(color_104)).place(x=273, y=384)
        btnColor105 = Button(self.vent,bg=color_105,width=ancho_botonE,height=alto_botonE,cursor="hand2",command=lambda: self.colores(color_105)).place(x=312, y=384)
        btnColor106 = Button(self.vent,bg=color_106,width=ancho_botonE,height=alto_botonE,cursor="hand2",command=lambda: self.colores(color_106)).place(x=351, y=384)
        btnColor107 = Button(self.vent,bg=color_107,width=ancho_botonE,height=alto_botonE,cursor="hand2",command=lambda: self.colores(color_107)).place(x=390, y=384)
        btnColor108 = Button(self.vent,bg=color_108,width=ancho_botonE,height=alto_botonE,cursor="hand2",command=lambda: self.colores(color_108)).place(x=429, y=384)
        btnColor109 = Button(self.vent,bg=color_109,width=ancho_botonE,height=alto_botonE,cursor="hand2",command=lambda: self.colores(color_109)).place(x=468, y=384)
        btnColor110 = Button(self.vent,bg=color_110,width=ancho_botonE,height=alto_botonE,cursor="hand2",command=lambda: self.colores(color_110)).place(x=507, y=384)
        btnColor111 = Button(self.vent,bg=color_111,width=ancho_botonE,height=alto_botonE,cursor="hand2",command=lambda: self.colores(color_111)).place(x=546, y=384)
        btnColor112 = Button(self.vent,bg=color_112,width=ancho_botonE,height=alto_botonE,cursor="hand2",command=lambda: self.colores(color_112)).place(x=585, y=384)
        
        btnColor113 = Button(self.vent,bg=color_113,width=ancho_botonE,height=alto_botonE,cursor="hand2",command=lambda: self.colores(color_113)).place(x=624, y=90)
        btnColor114 = Button(self.vent,bg=color_114,width=ancho_botonE,height=alto_botonE,cursor="hand2",command=lambda: self.colores(color_114)).place(x=663, y=90)
        btnColor115 = Button(self.vent,bg=color_115,width=ancho_botonE,height=alto_botonE,cursor="hand2",command=lambda: self.colores(color_115)).place(x=702, y=90)
        btnColor116 = Button(self.vent,bg=color_116,width=ancho_botonE,height=alto_botonE,cursor="hand2",command=lambda: self.colores(color_116)).place(x=741, y=90)
        btnColor117 = Button(self.vent,bg=color_117,width=ancho_botonE,height=alto_botonE,cursor="hand2",command=lambda: self.colores(color_117)).place(x=780, y=90)
        btnColor118 = Button(self.vent,bg=color_118,width=ancho_botonE,height=alto_botonE,cursor="hand2",command=lambda: self.colores(color_118)).place(x=819, y=90)
        
        btnColor119 = Button(self.vent,bg=color_119,width=ancho_botonE,height=alto_botonE,cursor="hand2",command=lambda: self.colores(color_119)).place(x=624, y=132)
        btnColor120 = Button(self.vent,bg=color_120,width=ancho_botonE,height=alto_botonE,cursor="hand2",command=lambda: self.colores(color_120)).place(x=663, y=132)
        btnColor121 = Button(self.vent,bg=color_121,width=ancho_botonE,height=alto_botonE,cursor="hand2",command=lambda: self.colores(color_121)).place(x=702, y=132)
        btnColor122 = Button(self.vent,bg=color_122,width=ancho_botonE,height=alto_botonE,cursor="hand2",command=lambda: self.colores(color_122)).place(x=741, y=132)
        btnColor123 = Button(self.vent,bg=color_123,width=ancho_botonE,height=alto_botonE,cursor="hand2",command=lambda: self.colores(color_123)).place(x=780, y=132)
        btnColor124 = Button(self.vent,bg=color_124,width=ancho_botonE,height=alto_botonE,cursor="hand2",command=lambda: self.colores(color_124)).place(x=819, y=132)
        
        btnColor125 = Button(self.vent,bg=color_125,width=ancho_botonE,height=alto_botonE,cursor="hand2",command=lambda: self.colores(color_125)).place(x=624, y=174)
        btnColor126 = Button(self.vent,bg=color_126,width=ancho_botonE,height=alto_botonE,cursor="hand2",command=lambda: self.colores(color_126)).place(x=663, y=174)
        btnColor127 = Button(self.vent,bg=color_127,width=ancho_botonE,height=alto_botonE,cursor="hand2",command=lambda: self.colores(color_127)).place(x=702, y=174)
        btnColor128 = Button(self.vent,bg=color_128,width=ancho_botonE,height=alto_botonE,cursor="hand2",command=lambda: self.colores(color_128)).place(x=741, y=174)
        btnColor129 = Button(self.vent,bg=color_129,width=ancho_botonE,height=alto_botonE,cursor="hand2",command=lambda: self.colores(color_129)).place(x=780, y=174)
        btnColor130 = Button(self.vent,bg=color_130,width=ancho_botonE,height=alto_botonE,cursor="hand2",command=lambda: self.colores(color_130)).place(x=819, y=174)
        
        btnColor131 = Button(self.vent,bg=color_131,width=ancho_botonE,height=alto_botonE,cursor="hand2",command=lambda: self.colores(color_131)).place(x=624, y=216)
        btnColor132 = Button(self.vent,bg=color_132,width=ancho_botonE,height=alto_botonE,cursor="hand2",command=lambda: self.colores(color_132)).place(x=663, y=216)
        btnColor133 = Button(self.vent,bg=color_133,width=ancho_botonE,height=alto_botonE,cursor="hand2",command=lambda: self.colores(color_133)).place(x=702, y=216)
        btnColor134 = Button(self.vent,bg=color_134,width=ancho_botonE,height=alto_botonE,cursor="hand2",command=lambda: self.colores(color_134)).place(x=741, y=216)
        btnColor135 = Button(self.vent,bg=color_135,width=ancho_botonE,height=alto_botonE,cursor="hand2",command=lambda: self.colores(color_135)).place(x=780, y=216)
        btnColor136 = Button(self.vent,bg=color_136,width=ancho_botonE,height=alto_botonE,cursor="hand2",command=lambda: self.colores(color_136)).place(x=819, y=216)
        
        btnColor137 = Button(self.vent,bg=color_137,width=ancho_botonE,height=alto_botonE,cursor="hand2",command=lambda: self.colores(color_137)).place(x=624, y=258)
        btnColor138 = Button(self.vent,bg=color_138,width=ancho_botonE,height=alto_botonE,cursor="hand2",command=lambda: self.colores(color_138)).place(x=663, y=258)
        btnColor139 = Button(self.vent,bg=color_139,width=ancho_botonE,height=alto_botonE,cursor="hand2",command=lambda: self.colores(color_139)).place(x=702, y=258)
        btnColor140 = Button(self.vent,bg=color_140,width=ancho_botonE,height=alto_botonE,cursor="hand2",command=lambda: self.colores(color_140)).place(x=741, y=258)
        btnColor141 = Button(self.vent,bg=color_141,width=ancho_botonE,height=alto_botonE,cursor="hand2",command=lambda: self.colores(color_141)).place(x=780, y=258)
        btnColor142 = Button(self.vent,bg=color_142,width=ancho_botonE,height=alto_botonE,cursor="hand2",command=lambda: self.colores(color_142)).place(x=819, y=258)
        
        btnColor143 = Button(self.vent,bg=color_143,width=ancho_botonE,height=alto_botonE,cursor="hand2",command=lambda: self.colores(color_143)).place(x=624, y=300)
        btnColor144 = Button(self.vent,bg=color_144,width=ancho_botonE,height=alto_botonE,cursor="hand2",command=lambda: self.colores(color_144)).place(x=663, y=300)
        btnColor145 = Button(self.vent,bg=color_145,width=ancho_botonE,height=alto_botonE,cursor="hand2",command=lambda: self.colores(color_145)).place(x=702, y=300)
        btnColor146 = Button(self.vent,bg=color_146,width=ancho_botonE,height=alto_botonE,cursor="hand2",command=lambda: self.colores(color_146)).place(x=741, y=300)
        btnColor147 = Button(self.vent,bg=color_147,width=ancho_botonE,height=alto_botonE,cursor="hand2",command=lambda: self.colores(color_147)).place(x=780, y=300)
        btnColor148 = Button(self.vent,bg=color_148,width=ancho_botonE,height=alto_botonE,cursor="hand2",command=lambda: self.colores(color_148)).place(x=819, y=300)
        
        btnColor149 = Button(self.vent,bg=color_149,width=ancho_botonE,height=alto_botonE,cursor="hand2",command=lambda: self.colores(color_149)).place(x=624, y=342)
        btnColor150 = Button(self.vent,bg=color_150,width=ancho_botonE,height=alto_botonE,cursor="hand2",command=lambda: self.colores(color_150)).place(x=663, y=342)
        btnColor151 = Button(self.vent,bg=color_151,width=ancho_botonE,height=alto_botonE,cursor="hand2",command=lambda: self.colores(color_151)).place(x=702, y=342)
        btnColor152 = Button(self.vent,bg=color_152,width=ancho_botonE,height=alto_botonE,cursor="hand2",command=lambda: self.colores(color_152)).place(x=741, y=342)
        btnColor153 = Button(self.vent,bg=color_153,width=ancho_botonE,height=alto_botonE,cursor="hand2",command=lambda: self.colores(color_153)).place(x=780, y=342)
        btnColor154 = Button(self.vent,bg=color_154,width=ancho_botonE,height=alto_botonE,cursor="hand2",command=lambda: self.colores(color_154)).place(x=819, y=342)
        
        btnColor155 = Button(self.vent,bg=color_155,width=ancho_botonE,height=alto_botonE,cursor="hand2",command=lambda: self.colores(color_155)).place(x=624, y=384)
        btnColor156 = Button(self.vent,bg=color_156,width=ancho_botonE,height=alto_botonE,cursor="hand2",command=lambda: self.colores(color_156)).place(x=663, y=384)
        btnColor157 = Button(self.vent,bg=color_157,width=ancho_botonE,height=alto_botonE,cursor="hand2",command=lambda: self.colores(color_157)).place(x=702, y=384)
        btnColor158 = Button(self.vent,bg=color_158,width=ancho_botonE,height=alto_botonE,cursor="hand2",command=lambda: self.colores(color_158)).place(x=741, y=384)
        btnColor159 = Button(self.vent,bg=color_159,width=ancho_botonE,height=alto_botonE,cursor="hand2",command=lambda: self.colores(color_159)).place(x=780, y=384)
        btnColor160 = Button(self.vent,bg=color_160,width=ancho_botonE,height=alto_botonE,cursor="hand2",command=lambda: self.colores(color_160)).place(x=819, y=384)
        
        ##Botones validar y salir
        largo_btns = 8
        ancho_btns = 1
        BtnValid = Button(self.vent,activebackground= "gray",text="Validar",command=self.validar,width=largo_btns,height=ancho_btns,cursor="hand2",font=(fuente,15,"bold")).place(x=190, y=510)
        BtnCancelar = Button(self.vent,activebackground= "gray",text="Cancelar",command=self.cancelar,width=largo_btns,height=ancho_btns,cursor="hand2",font=(fuente,15,"bold")).place(x=530, y=510)
        #BtnOcultar = Button(self.vent, activebackground= "gray", text="Ocultar", command=self.oculPass, width=5, height=2).place(x=780, y=460)
        #BtnMostrar = Button(self.vent, activebackground= "gray", text="Mostrar", command=self.mosPass, width=5, height=2).place(x=830, y=460)
        BtnReset = Button(self.vent,activebackground= "gray",text="Reset",command=self.reinicio,width=largo_btns,height=ancho_btns,cursor="hand2",font=(fuente,15,"bold")).place(x=360, y=510)

        lblPolUso = Label(self.vent, text="Políticas de uso", bg = "blue", font=('Helveticabold', 9), fg="white", cursor="hand2")
        lblPolUso.place(x=45, y=520)
        lblPolUso.bind("<Button-1>", lambda e: self.funPolUso())

        self.vent.mainloop()
        
    def cancelar(self):
        global flag, route, contra, voz, user, password
        contra = ""
        password = ""
        self.vent.destroy()
        if(flag == 1):
            cifrar_archivo.cifrar_archivo(user, route, flag, contra, voz)
        else:
            descifrar_archivo.descifrar_archivo(user, route, flag, contra, voz)
    
    def verif(self):
        global password
        p=password
        #print("P: "+p)
        self.entry.config(state = "normal")
        self.entry.delete(0, "end")
        self.entry.insert(0, p)
        self.entry.config(state = "disabled")
    
    def validar(self):
        global contra, route, flag, contra
        global voz, user, password
        self.entry.config(state = "normal")
        contra = self.entry.get()
        if(len(contra) >= 54 and len(contra) <=225):
            password = ""
            self.entry.delete(0, "end")
            print("Contraseña RGB validada\n\n")
            self.vent.destroy()
            if(flag == 1):
                cifrar_archivo.cifrar_archivo(user, route, flag, contra, voz)
            else:
                descifrar_archivo.descifrar_archivo(user, route, flag, contra, voz)
        else:
            messagebox.showinfo(message="La contraseña no cumple con la longitud esperada\n(Mínimo 6 colores).", title="Error")
    
    def reinicio(self):
        global password
        password = ""
        self.entry.config(state = "normal")
        self.entry.delete(0, "end")
        self.entry.config(state = "disabled")
    
    def ajuste(self, auxiliar):
        nuevo = ""
        trozos = auxiliar.replace("(", "").replace(")", "").split(", ")
        for i in trozos:
            if(len(i)==1):
                nuevo = nuevo + '00'+ i
            elif(len(i) == 2):
                nuevo = nuevo + '0' + i
            else:
                nuevo = nuevo + i
        return nuevo
    
    def colores(self, color):
        global password
        auxiliar = self.conversion(color)
        procesado = self.ajuste(auxiliar)
        password = password + procesado
        self.verif()
    
    #def oculPass(self):
    #    self.entry.config(show="*")
    
    #def mosPass(self):
    #    self.entry.config(show="")

    def conversion(self, col):
        h = col.lstrip('#')
        color = tuple(int(h[i:i+2], 16) for i in (0, 2, 4))
        auxiliar = str(color)
        return auxiliar
        
    def funPolUso(self):
        politicaUso.nuevo()   
        
#if __name__ == '__main__':
   #ventana = Tk()
#   rgb_nueva()
   #ventana.mainloop()'''