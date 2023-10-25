from tkinter import ttk
from tkinter import *

ventana_bienvenida=Tk()
ventana_bienvenida.geometry("800x600")


img_logo=PhotoImage(file="logo.png")
etiqueta=Label(ventana_bienvenida, text="Reparacion de coches", image=img_logo)
etiqueta.pack()

ventana_bienvenida.mainloop()