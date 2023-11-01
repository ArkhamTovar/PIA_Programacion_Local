from tkinter import ttk
from tkinter import *
from PIL import ImageTk, Image

def ventanaCarro():
    frameCarro=Tk()
    frameCarro.geometry('800x600')


def ventanaCliente():
    
    ventCliente=Tk()
    ventCliente.title('Registro cliente')
    ventCliente.geometry('700x600')
    ventCliente.config(bg='blue')
    frameCliente=LabelFrame(ventCliente,text='Registro de cliente', font=('Arial',12), background='white')
    frameCliente.pack(fill='both', expand='yes', padx=20, pady=15)

    lblCliente=Label(frameCliente, text="Nombre", width=20)
    lblCliente.grid(row=1,column=0,padx=5,pady=3)

    def GuardarDatosCliente():
        nombre=etyNombre.get()
        print(nombre)

    etyNombre=Entry(frameCliente, width=30, background='grey',foreground='red')
    etyNombre.grid(row=2,column=0,padx=5,pady=3)

    btnDatosCliente=Button(frameCliente,text="registrar cliente", width=12,height=9,command=GuardarDatosCliente)
    btnDatosCliente.grid(row=3,column=0,padx=5,pady=3)


    
    







ventanaBienvenida=Tk()
ventanaBienvenida.title('Menu')
ventanaBienvenida.geometry('400x400')
ventanaBienvenida.config(bg='blue')

frameBienvenida=LabelFrame(text="Bienvenido al sistema", font=('arial',12), background='white')
frameBienvenida.pack(fill='both', expand='yes',padx=20,pady=15)

btnRegistroCarro=Button(ventanaBienvenida,text="registrar coche", width=12,height=9,command=ventanaCarro)
btnRegistroCarro.place(x=50,y=40)

btnRegistroCliente=Button(ventanaBienvenida,text="registrar cliente", width=12,height=9, command=ventanaCliente)
btnRegistroCliente.place(x=200,y=40)
    
ventanaBienvenida.mainloop()