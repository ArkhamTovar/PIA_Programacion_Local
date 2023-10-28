from tkinter import ttk
from tkinter import *
from PIL import ImageTk, Image

def ventanaCarro():
    frameCarro=Tk()
    frameCarro.geometry('800x600')

def ventanaCliente():
    frameCliente=Tk()
    frameCliente.geometry('800x800')



ventanaBienvenida=Tk()
ventanaBienvenida.title('Inicio')
ventanaBienvenida.geometry('400x400')
ventanaBienvenida.config(bg='blue')

frameBienvenida=LabelFrame(text="Bienvenido al sistema", font=('arial',12), background='white')
frameBienvenida.pack(fill='both', expand='yes',padx=20,pady=15)

btnRegistroCarro=Button(ventanaBienvenida,text="registrar coche", width=12,height=9,command=ventanaCarro)
btnRegistroCarro.place(x=50,y=40)

btnRegistroCliente=Button(ventanaBienvenida,text="registrar cliente", width=12,height=9, command=ventanaCliente)
btnRegistroCliente.place(x=200,y=40)
    
ventanaBienvenida.mainloop()