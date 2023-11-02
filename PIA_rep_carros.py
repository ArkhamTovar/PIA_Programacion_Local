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

    lblClienteNombre=Label(frameCliente, text="Nombre", width=20)
    lblClienteNombre.grid(row=1,column=0,padx=5,pady=3)

    lblClienteTelefono=Label(frameCliente, text="Telefono", width=20)
    lblClienteTelefono.grid(row=1,column=1,padx=5,pady=3)

    lblClienteMunicipio=Label(frameCliente, text="Municipio", width=20)
    lblClienteMunicipio.grid(row=1,column=2,padx=5,pady=3)

    lblClienteCP=Label(frameCliente, text="C.P.", width=19)
    lblClienteCP.grid(row=1,column=3,padx=5,pady=3)

    lblClienteColonia=Label(frameCliente, text="Colonia", width=19)
    lblClienteColonia.grid(row=3,column=0,padx=5,pady=3)


    def GuardarDatosCliente():
        cliente=list()
        nombre=etyNombre.get()
        telefono=etyTelefono.get()
        municipio=etyMunicipio.get()
        cp=etyCP.get()
        colonia=etyColonia.get()
        cliente=[nombre,telefono,municipio,cp,colonia]
        lblTexto=Label(frameCliente, text="SE HAN GUARDADO LOS REGISTROS",font=('Arial',10),fg='red', width=50)
        lblTexto.place(x=100,y=200)
        
        def Prueba():
            frameRegistro=LabelFrame(ventCliente,text='Datos Registrados', font=('Arial',12), background='white')
            frameRegistro.pack(fill='both', expand='yes', padx=20, pady=15)

            lblClienteNombre=Label(frameRegistro, text="Nombre", width=20)
            lblClienteNombre.grid(row=1,column=0,padx=5,pady=3)

            lblnombre=Label(frameRegistro, text=nombre,fg='Red', width=20)
            lblnombre.grid(row=2,column=0,padx=5,pady=3)

            lblClienteTelefono=Label(frameRegistro, text="Telefono", width=20)
            lblClienteTelefono.grid(row=1,column=1,padx=5,pady=3)

            lbltelefono=Label(frameRegistro, text=telefono,fg='Red', width=20)
            lbltelefono.grid(row=2,column=1,padx=5,pady=3)

            lblClienteMunicipio=Label(frameRegistro, text="Municipio", width=20)
            lblClienteMunicipio.grid(row=1,column=2,padx=5,pady=3)

            lblmunicipio=Label(frameRegistro, text=municipio,fg='Red', width=20)
            lblmunicipio.grid(row=2,column=2,padx=5,pady=3)

            lblClienteCP=Label(frameRegistro, text="C.P.", width=19)
            lblClienteCP.grid(row=1,column=3,padx=5,pady=3)

            lblcp=Label(frameRegistro, text=cp,fg='Red', width=20)
            lblcp.grid(row=2,column=3,padx=5,pady=3)

            lblClienteColonia=Label(frameRegistro, text="Colonia", width=19)
            lblClienteColonia.grid(row=3,column=0,padx=5,pady=3)

            lblcolonia=Label(frameRegistro, text=colonia,fg='Red', width=20)
            lblcolonia.grid(row=4,column=0,padx=5,pady=3)

        Prueba()
    etyNombre=Entry(frameCliente, width=30, background='grey',foreground='red')
    etyNombre.grid(row=2,column=0,padx=5,pady=3)

    etyTelefono=Entry(frameCliente, width=15, background='grey',foreground='red')
    etyTelefono.grid(row=2,column=1,padx=5,pady=3)

    etyMunicipio=Entry(frameCliente, width=20, background='grey',foreground='red')
    etyMunicipio.grid(row=2,column=2,padx=5,pady=3)

    etyCP=Entry(frameCliente, width=10, background='grey',foreground='red')
    etyCP.grid(row=2,column=3,padx=5,pady=3)

    etyColonia=Entry(frameCliente, width=30, background='grey',foreground='red')
    etyColonia.grid(row=4,column=0,padx=5,pady=3)

    btnDatosCliente=Button(frameCliente,text="Guardar datos", width=12,height=5,command=GuardarDatosCliente)
    btnDatosCliente.grid(row=5,column=3,padx=5,pady=3)


    
    







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