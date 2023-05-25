from tkinter import *
from tkinter import ttk

def selec():
    monitor.config(text = "ha seleccionado {}".format(opcion.get() ))

def reset():
    opcion.set(None)
    monitor.config(text="")
    
root = Tk()
monitor = ttk.Label(root, foreground="#CF724A",justify="right")
print(monitor.config())
opcion = StringVar()
opcion.set(None)
monitor.grid(column=0,row=0)

ttk.Radiobutton(root, text="Hotdog", variable=opcion,value="Hotdog", command=selec).grid(column=0,row=1,ipadx=17)
ttk.Radiobutton(root, text="S.papa", variable=opcion,value="S.papa", command=selec).grid(column=0,row=2,ipadx=20)
ttk.Radiobutton(root, text="Burger", variable=opcion,value="Burger", command=selec).grid(column=0,row=3,ipadx=20)
ttk.Button(root,text="Borrar", command=reset).grid(column=1,row=4)

root.mainloop()