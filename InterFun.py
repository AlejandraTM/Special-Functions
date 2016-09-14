##InterfazFunciones
from Tkinter import *
import os
from scipy import special 
import numpy as np
import matplotlib.pyplot as plt

## Funciones

def graficar(j):
	j.destroy()
	if Valor.get()=="Bessel's Function":
		GrafBessel()
	elif Valor.get()=="Chebychev's polynomials":
		GrafChev()
	elif Valor.get()=="Associated Legendre polynomial":
		GrafAsLeg()
	elif Valor.get()=="Hypergeometric Function":
		GrafHyper()
	elif Valor.get()=="Gegenbauer's Functions":
		GrafGegen()
	elif Valor.get()=="Laguerre's Polynomials":
		GrafLague()
	elif Valor.get()=="Harmonic oscillator":
		GrafOsc()
	elif Valor.get()=="Hermite Polynomials":
		GrafHerm()
	else:
		print ":O"
def GrafBessel():
	ventana2=Tk()
	ventana2.title("Functions Plot")
	ventana2.geometry("550x200")
	Label(ventana2, text="Number of functions",font=("Arial",12)).place(x=200, y=10)
	colorFondo="#8A2BE2"
	v=IntVar()
	Radiobutton(ventana2,text="2",value=2,variable=v).place(x=120,y=40)
	Radiobutton(ventana2,text="3",value=3,variable=v).place(x=180,y=40)
	Radiobutton(ventana2,text="4",value=4,variable=v).place(x=240,y=40)
	Radiobutton(ventana2,text="5",value=5,variable=v).place(x=300,y=40)
	Radiobutton(ventana2,text="6",value=6,variable=v).place(x=360,y=40)
	Radiobutton(ventana2,text="7",value=7,variable=v).place(x=420,y=40)
	Label(ventana2, text="Individual function",font=("Arial",12)).place(x=200, y=80)
	Radiobutton(ventana2,text="n=0",value=8,variable=v).place(x=40,y=110)
	Radiobutton(ventana2,text="n=1",value=9,variable=v).place(x=100,y=110)
	Radiobutton(ventana2,text="n=2",value=10,variable=v).place(x=160,y=110)
	Radiobutton(ventana2,text="n=3",value=11,variable=v).place(x=220,y=110)
	Radiobutton(ventana2,text="n=4",value=12,variable=v).place(x=280,y=110)
	Radiobutton(ventana2,text="n=5",value=13,variable=v).place(x=340,y=110)
	Radiobutton(ventana2,text="n=6",value=14,variable=v).place(x=400,y=110)
	Radiobutton(ventana2,text="n=7",value=15,variable=v).place(x=460,y=110)
	Button(ventana2, text="First Order", command=lambda: Bessel(v)).place(x=90,y=150)
	Button(ventana2, text="Second Order", command=lambda: Bessel2(v)).place(x=240,y=150)
	Button(ventana2, text="Quit", command=lambda: comienzo(ventana2)).place(x=390,y=150)
	ventana2.mainloop()
def GrafAsLeg():
	ventana2=Tk()
	ventana2.title("Functions Plot")
	ventana2.geometry("350x300")
	Label(ventana2, text="Order of function",font=("Arial",12)).place(x=100, y=10)
	colorFondo="#FFFFFF"
	v=IntVar()
	w=IntVar()
	b=Radiobutton(ventana2,text="0",value=0,variable=v).place(x=100,y=50)
	Radiobutton(ventana2,text="1",value=1,variable=v).place(x=160,y=50)
	Radiobutton(ventana2,text="2",value=2,variable=v).place(x=220,y=50)
	Label(ventana2, text="Degree of function",font=("Arial",12)).place(x=95, y=80)
	Radiobutton(ventana2,text="0",value=0,variable=w).place(x=40,y=120)
	Radiobutton(ventana2,text="1",value=1,variable=w).place(x=100,y=120)
	Radiobutton(ventana2,text="2",value=2,variable=w).place(x=160,y=120)
	Radiobutton(ventana2,text="3",value=3,variable=w).place(x=220,y=120)
	Radiobutton(ventana2,text="4",value=4,variable=w).place(x=280,y=120)
	Radiobutton(ventana2,text="All degrees",value=5,variable=w).place(x=120,y=160)
	Button(ventana2, text="Accept", command=lambda: AsLegendre(v,w)).place(x=100,y=200)
	Button(ventana2, text="Salir", command=lambda: comienzo(ventana2)).place(x=180,y=200)
	ventana2.mainloop()
def GrafGegen():
	ventana2=Tk()
	ventana2.title("Functions Plot")
	ventana2.geometry("400x250")
	colorFondo="#FFFFFF"
	v=IntVar()
	w=IntVar()
	#text="Degree of function"
	Label(ventana2, text="Degree of function",font=("Arial",12)).place(x=30, y=30)
	Spinbox(ventana2,width=5,values=("1","2","3","4","5","6","7","8","9","10"),textvariable=v).place(x=200,y=30)
	Radiobutton(ventana2,text="All degrees",value=11,variable=v).place(x=120,y=80)
	Label(ventana2, text="Lambda",font=("Arial",12)).place(x=30, y=130)
	Radiobutton(ventana2,text="0",value=0,variable=w).place(x=100,y=130)
	Radiobutton(ventana2,text="1",value=1,variable=w).place(x=160,y=130)
	Radiobutton(ventana2,text="2",value=2,variable=w).place(x=220,y=130)
	Radiobutton(ventana2,text="3",value=3,variable=w).place(x=280,y=130)
	Radiobutton(ventana2,text="4",value=4,variable=w).place(x=340,y=130)
	Button (ventana2, text="Special Functions", command=lambda: Gegenspecial()).place(x=30,y=200)
	Button(ventana2, text="Accept", command=lambda: Gegen(v,w)).place(x=190,y=200)	
	Button(ventana2, text="Salir", command=lambda: comienzo(ventana2)).place(x=270,y=200)
	ventana2.mainloop()
def GrafChev():
	ventana2=Tk()
	ventana2.title("Functions Plot")
	ventana2.geometry("400x200")
	Label(ventana2, text="Number of functions",font=("Arial",12)).place(x=120, y=10)
	colorFondo="#FFFFFF"
	v=IntVar()
	Radiobutton(ventana2,text="2",value=6,variable=v).place(x=60,y=40)
	Radiobutton(ventana2,text="3",value=7,variable=v).place(x=120,y=40)
	Radiobutton(ventana2,text="4",value=8,variable=v).place(x=180,y=40)
	Radiobutton(ventana2,text="5",value=9,variable=v).place(x=240,y=40)
	Radiobutton(ventana2,text="6",value=10,variable=v).place(x=300,y=40)
	Label(ventana2, text="Individual function",font=("Arial",12)).place(x=120, y=80)
	Radiobutton(ventana2,text="n=0",value=0,variable=v).place(x=30,y=110)
	Radiobutton(ventana2,text="n=1",value=1,variable=v).place(x=90,y=110)
	Radiobutton(ventana2,text="n=2",value=2,variable=v).place(x=150,y=110)
	Radiobutton(ventana2,text="n=3",value=3,variable=v).place(x=210,y=110)
	Radiobutton(ventana2,text="n=4",value=4,variable=v).place(x=270,y=110)
	Radiobutton(ventana2,text="n=5",value=5,variable=v).place(x=330,y=110)
	Button(ventana2, text="First Kind", command=lambda: ChevI(v)).place(x=50,y=150)
	Button(ventana2, text="Second Kind", command=lambda: ChevII(v)).place(x=170,y=150)
	Button(ventana2, text="Quit", command=lambda: comienzo(ventana2)).place(x=300,y=150)
	ventana2.mainloop()
def GrafLague():
	ventana2=Tk()
	ventana2.title("Functions Plot")
	ventana2.geometry("400x200")
	Label(ventana2, text="Number of functions",font=("Arial",12)).place(x=120, y=10)
	colorFondo="#FFFFFF"
	v=IntVar()
	Radiobutton(ventana2,text="2",value=6,variable=v).place(x=60,y=40)
	Radiobutton(ventana2,text="3",value=7,variable=v).place(x=120,y=40)
	Radiobutton(ventana2,text="4",value=8,variable=v).place(x=180,y=40)
	Radiobutton(ventana2,text="5",value=9,variable=v).place(x=240,y=40)
	Radiobutton(ventana2,text="6",value=10,variable=v).place(x=300,y=40)
	Label(ventana2, text="Individual function",font=("Arial",12)).place(x=120, y=80)
	Radiobutton(ventana2,text="n=0",value=0,variable=v).place(x=30,y=110)
	Radiobutton(ventana2,text="n=1",value=1,variable=v).place(x=90,y=110)
	Radiobutton(ventana2,text="n=2",value=2,variable=v).place(x=150,y=110)
	Radiobutton(ventana2,text="n=3",value=3,variable=v).place(x=210,y=110)
	Radiobutton(ventana2,text="n=4",value=4,variable=v).place(x=270,y=110)
	Radiobutton(ventana2,text="n=5",value=5,variable=v).place(x=330,y=110)
	Button(ventana2, text="Plot", command=lambda: Lague(v)).place(x=150,y=150)
	Button(ventana2, text="Quit", command=lambda: comienzo(ventana2)).place(x=250,y=150)
	ventana2.mainloop()
def GrafOsc():
	ventana2=Tk()
	ventana2.title("Functions Plot")
	ventana2.geometry("500x250")
	colorFondo="#FFFFFF"
	Label(ventana2, text="Medium constant",font=("Arial",12)).place(x=50, y=50)
	Label(ventana2, text="Stiffness constant",font=("Arial",12)).place(x=50, y=100)
	Label(ventana2, text="Mass",font=("Arial",12)).place(x=50, y=150)
	v=IntVar()
	Entry(ventana2, textvariable=v).place(x=200,y=50)
	w=IntVar()
	Entry(ventana2, textvariable=w).place(x=200,y=100)
	z=IntVar()
	Entry(ventana2, textvariable=z).place(x=200,y=150)
	y=IntVar()
	Radiobutton(ventana2,text="Simple",value=0,variable=y).place(x=350,y=50)
	Radiobutton(ventana2,text="Damped",value=1,variable=y).place(x=350,y=80)
	Radiobutton(ventana2,text="Overdamped",value=2,variable=y).place(x=350,y=110)
	Radiobutton(ventana2,text="Subamortiguado",value=3,variable=y).place(x=350,y=140)
	Radiobutton(ventana2,text="all",value=4,variable=y).place(x=350,y=170)
	Button(ventana2, text="Plot", command=lambda: OsArm(v,w,z,y)).place(x=50,y=200)
	Button(ventana2, text="Quit", command=lambda: comienzo(ventana2)).place(x=150,y=200)
def GrafHerm():
	ventana2=Tk()
	ventana2.title("Functions Plot")
	ventana2.geometry("400x250")
	colorFondo="#FFFFFF"
	Label(ventana2, text="Polynomials", font=("Arial",12)).place(x=150,y=20)
	Label(ventana2, text="Number of functions",font=("Arial",12)).place(x=120, y=100)
	v=IntVar()
	Radiobutton(ventana2,text="n=0",value=0,variable=v).place(x=20,y=50)
	Radiobutton(ventana2,text="n=1",value=1,variable=v).place(x=70,y=50)
	Radiobutton(ventana2,text="n=2",value=2,variable=v).place(x=120,y=50)	
	Radiobutton(ventana2,text="n=3",value=3,variable=v).place(x=170,y=50)
	Radiobutton(ventana2,text="n=4",value=4,variable=v).place(x=220,y=50)
	Radiobutton(ventana2,text="n=5",value=5,variable=v).place(x=270,y=50)	
	Radiobutton(ventana2,text="n=6",value=6,variable=v).place(x=320,y=50)
	Radiobutton(ventana2,text="n from 0 to 3",value=7,variable=v).place(x=70,y=130)
	Radiobutton(ventana2,text="n from 4 to 6",value=8,variable=v).place(x=220,y=130)
	Button(ventana2, text="Plot", command=lambda: Hermite(v)).place(x=100,y=190)
	Button(ventana2, text="Quit", command=lambda: comienzo(ventana2)).place(x=200,y=190)
def GrafHyper():
	ventana2=Tk()
	ventana2.title("Functions Plot")
	ventana2.geometry("350x150")
	colorFondo="#FFFFFF"
	Label(ventana2, text="Parameters", font=("Arial",12)).place(x=150,y=20)
	v=IntVar()
	Label(ventana2, text="a", font=("Arial",12)).place(x=60,y=60)
	Entry(ventana2, width=5,textvariable=v).place(x=80,y=60)
	w=IntVar()
	Label(ventana2, text="b", font=("Arial",12)).place(x=160,y=60)
	Entry(ventana2, width=5,textvariable=w).place(x=180,y=60)
	z=IntVar()
	Label(ventana2, text="c", font=("Arial",12)).place(x=260,y=60)
	Entry(ventana2, width=5,textvariable=z).place(x=280,y=60)
	Button(ventana2, text="Plot", command=lambda: Hiper(v,w,z)).place(x=100,y=100)
	Button(ventana2, text="Quit", command=lambda: comienzo(ventana2)).place(x=180,y=100)
def quit():
	ventana.destroy()
def Bessel(a):
	os.system("python menu.py -i %i"%a.get())
def Bessel2(a):
	os.system("python menu3.py -i %i"%a.get())
def AsLegendre(a,c):
	os.system("python menu2.py -i %i %i"%(a.get(),c.get()))
def Gegen(a,c):
	os.system("python menu4.py -i %i %i"%(a.get(),c.get()))
def Gegenspecial():
        os.system("python menu5.py")
def ChevI(a):
	os.system("python menu6.py -i %i"%a.get())
def ChevII(a):
	os.system("python menu7.py -i %i"%a.get())
def Lague(a):
	os.system("python menu8.py -i %i"%a.get())
def OsArm(a,b,c,d):
	os.system("python menu9.py -i %i %i %i %i"%(a.get(),b.get(),c.get(),d.get()))
def Hermite(a):
	os.system("python menu10.py -i %i "%(a.get()))
def Hiper(a,b,c):
	os.system("python menu11.py -i %i %i %i"%(a.get(),b.get(),c.get()))
def comienzo(l):
	l.destroy()
	os.system("python InterFun.py ")
	
##Caracteristicas de la ventana

colorFondo="#515"
colorLetra="#FFF"

ventana=Tk()
ventana.geometry("650x300")
ventana.configure(background=colorFondo)
ventana.title("Special Functions Of Mathematical Physics")

etiqueta=Label(ventana, text="Special Function", bg=colorFondo, fg=colorLetra, font=("Helvetica",19)).place(x=200, y =10)

etiqueta=Label(ventana, text="Polynomial to graph", bg=colorFondo, fg=colorLetra, font=("Arial",12)).place(x=100, y =100)

Valor= StringVar()

combo=Spinbox(ventana,width=31, values=("Bessel's Function","Associated Legendre polynomial","Hypergeometric Function", "Gegenbauer's Functions", "Chebychev's polynomials","Laguerre's Polynomials", "Harmonic oscillator", "Hermite Polynomials"),textvariable=Valor).place(x=300,y=100)

Button(ventana, text="Plot",command=lambda: graficar(ventana)).place(x=240,y=200)
Button(ventana, text="Quit",command=quit).place(x=350,y=200)
ventana.mainloop()

																				
