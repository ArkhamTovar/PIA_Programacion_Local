from tkinter import ttk
from tkinter import *
import sqlite3
from sqlite3 import Error
import sys




def ventanaCarro():
    ventCarro=Tk()
    ventCarro.title('Registro de coche')
    ventCarro.geometry('800x600')
    ventCarro.config(bg='blue')
    frameCarro=LabelFrame(ventCarro, text="Registro de carro",font=('Arial',12),background='white')
    frameCarro.pack(fill='both', expand='yes', padx=20, pady=15)

    lblMatricula=Label(frameCarro,text='Matricula', width=20)
    lblMatricula.grid(row=1,column=0,padx=5,pady=3)

    lblMarca=Label(frameCarro, text='Marca',width=20 )
    lblMarca.grid(row=1,column=1,padx=5,pady=3)

    lblColor=Label(frameCarro, text='Color', width=20)
    lblColor.grid(row=1,column=2,padx=5,pady=3)

    lblModelo=Label(frameCarro, text='Modelo', width=20)
    lblModelo.grid(row=1,column=3,padx=5,pady=3)

    def GuardarDatosCoche():
        matricula=etyMatricula.get()
        marca=etyMarca.get()
        color=etyColor.get()
        modelo=etyModelo.get()
        coche=[matricula,marca,color,modelo]
        lblTexto=Label(frameCarro, text="SE HAN GUARDADO LOS REGISTROS",font=('Arial',10),fg='red', width=50)
        lblTexto.place(x=100,y=200)
        def ImpresionDeCocheRegistrado():
            frameRegistroCoche=LabelFrame(ventCarro, text="Registro de carro",font=('Arial',12),background='white')
            frameRegistroCoche.pack(fill='both', expand='yes', padx=20, pady=15)

            lblMatricula=Label(frameRegistroCoche,text='Matricula', width=20)
            lblMatricula.grid(row=1,column=0,padx=5,pady=3)
            lblMatriculaCoche=Label(frameRegistroCoche,text=matricula, width=20,foreground='red')
            lblMatriculaCoche.grid(row=2,column=0,padx=5,pady=3)

            lblMarca=Label(frameRegistroCoche, text='Marca',width=20 )
            lblMarca.grid(row=1,column=1,padx=5,pady=3)
            lblMarcaCoche=Label(frameRegistroCoche, text=marca, width=20,foreground='red')
            lblMarcaCoche.grid(row=2,column=1,padx=5,pady=3)

            lblColor=Label(frameRegistroCoche, text='Color', width=20)
            lblColor.grid(row=1,column=2,padx=5,pady=3)
            lblColorCoche=Label(frameRegistroCoche, text=color, width=20,foreground='red')
            lblColorCoche.grid(row=2,column=2,padx=5,pady=3)

            lblModelo=Label(frameRegistroCoche, text='Modelo', width=20)
            lblModelo.grid(row=1,column=3,padx=5,pady=3)
            lblModeloCoche=Label(frameRegistroCoche, text=modelo, width=20,foreground='red')
            lblModeloCoche.grid(row=2,column=3,padx=5,pady=3)
        ImpresionDeCocheRegistrado()

    etyMatricula=Entry(frameCarro, width=30, background='white',foreground='red')
    etyMatricula.grid(row=2,column=0,padx=5,pady=3)

    etyMarca=Entry(frameCarro,width=30, background='white',foreground='red' )
    etyMarca.grid(row=2,column=1,padx=5,pady=3)

    etyColor=Entry(frameCarro,width=30, background='white',foreground='red' )
    etyColor.grid(row=2,column=2,padx=5,pady=3)

    etyModelo=Entry(frameCarro,width=25, background='white',foreground='red' )
    etyModelo.grid(row=2,column=3,padx=5,pady=3)

    btnDatosCoche=Button(frameCarro, text='GUARDAR DATOS',width=15,height=5,command=GuardarDatosCoche)
    btnDatosCoche.grid(row=5,column=3,padx=5,pady=3)
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
        nombre=etyNombre.get()
        telefono=etyTelefono.get()
        municipio=etyMunicipio.get()
        cp=etyCP.get()
        colonia=etyColonia.get()
        cliente=[nombre,telefono,municipio,cp,colonia]
        lblTexto=Label(frameCliente, text="SE HAN GUARDADO LOS REGISTROS",font=('Arial',10),fg='red', width=50)
        lblTexto.place(x=100,y=200)
        
        
        def ImpresionDeClienteRegistrado():
            frameRegistroCliente=LabelFrame(ventCliente,text='Datos Registrados', font=('Arial',12), background='white')
            frameRegistroCliente.pack(fill='both', expand='yes', padx=20, pady=15)

            lblClienteNombre=Label(frameRegistroCliente, text="Nombre", width=20)
            lblClienteNombre.grid(row=1,column=0,padx=5,pady=3)

            lblnombre=Label(frameRegistroCliente, text=nombre,fg='Red', width=20)
            lblnombre.grid(row=2,column=0,padx=5,pady=3)

            lblClienteTelefono=Label(frameRegistroCliente, text="Telefono", width=20)
            lblClienteTelefono.grid(row=1,column=1,padx=5,pady=3)

            lbltelefono=Label(frameRegistroCliente, text=telefono,fg='Red', width=20)
            lbltelefono.grid(row=2,column=1,padx=5,pady=3)

            lblClienteMunicipio=Label(frameRegistroCliente, text="Municipio", width=20)
            lblClienteMunicipio.grid(row=1,column=2,padx=5,pady=3)

            lblmunicipio=Label(frameRegistroCliente, text=municipio,fg='Red', width=20)
            lblmunicipio.grid(row=2,column=2,padx=5,pady=3)

            lblClienteCP=Label(frameRegistroCliente, text="C.P.", width=19)
            lblClienteCP.grid(row=1,column=3,padx=5,pady=3)

            lblcp=Label(frameRegistroCliente, text=cp,fg='Red', width=20)
            lblcp.grid(row=2,column=3,padx=5,pady=3)

            lblClienteColonia=Label(frameRegistroCliente, text="Colonia", width=19)
            lblClienteColonia.grid(row=3,column=0,padx=5,pady=3)

            lblcolonia=Label(frameRegistroCliente, text=colonia,fg='Red', width=20)
            lblcolonia.grid(row=4,column=0,padx=5,pady=3)



        ImpresionDeClienteRegistrado()

    etyNombre=Entry(frameCliente, width=30, background='white',foreground='red')
    etyNombre.grid(row=2,column=0,padx=5,pady=3)

    etyTelefono=Entry(frameCliente, width=15, background='white',foreground='red')
    etyTelefono.grid(row=2,column=1,padx=5,pady=3)

    etyMunicipio=Entry(frameCliente, width=20, background='white',foreground='red')
    etyMunicipio.grid(row=2,column=2,padx=5,pady=3)

    etyCP=Entry(frameCliente, width=10, background='white',foreground='red')
    etyCP.grid(row=2,column=3,padx=5,pady=3)

    etyColonia=Entry(frameCliente, width=30, background='white',foreground='red')
    etyColonia.grid(row=4,column=0,padx=5,pady=3)

    btnDatosCliente=Button(frameCliente,text="Guardar datos", width=12,height=5,command=GuardarDatosCliente)
    btnDatosCliente.grid(row=5,column=3,padx=5,pady=3)

def ventanaReparacion():
    ventReparacion=Tk()
    ventReparacion.title('Reparacion')
    ventReparacion.config(bg='blue')
    ventReparacion.geometry('700x600')
    frameReparacion=LabelFrame(ventReparacion,text='Reparacion', font=('Arial',12),background='white')
    frameReparacion.pack(fill='both', expand='yes', padx=20, pady=15)

    lblMatricula=Label(frameReparacion,text='Matricula', width=20)
    lblMatricula.grid(row=1,column=0,padx=5,pady=3)

    lblMecanico=Label(frameReparacion,text='Mecanico',width=20)
    lblMecanico.grid(row=1,column=1,padx=5,pady=3)

    lblFecha=Label(frameReparacion,text='Fecha', width=20)
    lblFecha.grid(row=1,column=2,padx=5,pady=3)

    lblTiempoRep=Label(frameReparacion, text='Tiempo reparacion', width=20)
    lblTiempoRep.grid(row=3,column=0,padx=5,pady=3)

    def GuardarDatosRep():
        matricula=etyMatricula.get()
        mecanico=etyMecanico.get()
        fecha=etyFecha.get()
        tiempoRep=etyTiempoRep.get()
        reparacion=[matricula,mecanico,fecha,tiempoRep]
        lblTexto=Label(frameReparacion, text="SE HAN GUARDADO LOS REGISTROS",font=('Arial',10),fg='red', width=50)
        lblTexto.place(x=100,y=200)

        def ImpresionDeDatosReparacion():
            frameReparacionRegistrada=LabelFrame(ventReparacion,text='Reparacion', font=('Arial',12),background='white')
            frameReparacionRegistrada.pack(fill='both', expand='yes', padx=20, pady=15)

            lblMatricula=Label(frameReparacionRegistrada,text='Matricula', width=20)
            lblMatricula.grid(row=1,column=0,padx=5,pady=3)

            lblMatriculaRegistrada=Label(frameReparacionRegistrada,text=matricula, width=20,fg='red')
            lblMatriculaRegistrada.grid(row=2,column=0,padx=5,pady=3)

            lblMecanico=Label(frameReparacionRegistrada,text='Mecanico',width=20)
            lblMecanico.grid(row=1,column=1,padx=5,pady=3)
            lblMecanicoRegistrado=Label(frameReparacionRegistrada,text=mecanico,width=20,fg='red')
            lblMecanicoRegistrado.grid(row=2,column=1,padx=5,pady=3)

            lblFecha=Label(frameReparacionRegistrada,text='Fecha', width=20)
            lblFecha.grid(row=1,column=2,padx=5,pady=3)
            lblFechaRegistrada=Label(frameReparacionRegistrada,text=fecha, width=20,fg='red')
            lblFechaRegistrada.grid(row=2,column=2,padx=5,pady=3)

            lblTiempoRep=Label(frameReparacionRegistrada, text='Tiempo reparacion', width=20)
            lblTiempoRep.grid(row=1,column=3,padx=5,pady=3)
            lblTiempoRepRegistrada=Label(frameReparacionRegistrada, text=tiempoRep, width=20,fg='red')
            lblTiempoRepRegistrada.grid(row=2,column=3,padx=5,pady=3)
        ImpresionDeDatosReparacion()

    etyMatricula=Entry(frameReparacion,width=30,background='white',foreground='red')
    etyMatricula.grid(row=2,column=0,padx=5,pady=3)

    etyMecanico=Entry(frameReparacion,width=30,background='white',foreground='red')
    etyMecanico.grid(row=2,column=1,padx=5,pady=3)

    etyFecha=Entry(frameReparacion,width=30,background='white',foreground='red')
    etyFecha.grid(row=2,column=2,padx=5,pady=3)

    etyTiempoRep=Entry(frameReparacion,width=30,background='white',foreground='red')
    etyTiempoRep.grid(row=4,column=0,padx=5,pady=3)

    btnDatosRep=Button(frameReparacion,text="Guardar datos", width=12,height=5,command=GuardarDatosRep)
    btnDatosRep.grid(row=5,column=2,padx=5,pady=3)
    
    
    







ventanaBienvenida=Tk()
ventanaBienvenida.title('Menu')
ventanaBienvenida.geometry('400x400')
ventanaBienvenida.config(bg='blue')

frameBienvenida=LabelFrame(text="Bienvenido al sistema", font=('arial',12), background='white')
frameBienvenida.pack(fill='both', expand='yes',padx=20,pady=15)

btnRegistroCarro=Button(ventanaBienvenida,text="registrar coche", width=12,height=9,command=ventanaCarro)
btnRegistroCarro.place(x=50,y=40)

btnRegistroCliente=Button(ventanaBienvenida,text="registrar cliente", width=12,height=9, command=ventanaCliente)
btnRegistroCliente.place(x=250,y=40)
    
btnReparacion=Button(ventanaBienvenida,text='Reparacion',width=12,height=9,command=ventanaReparacion )
btnReparacion.place(x=150,y=200)

ventanaBienvenida.mainloop()