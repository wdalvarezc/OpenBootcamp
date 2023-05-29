from tkinter import *

window = Tk()
listbox = Listbox(window, bg="#4C4C4C",fg="#F3F3F3",selectforeground="#4C4C4C",selectbackground="#F3F3F3")
razasDog = ["akita","bull dog","beagle","boxer","chihuahua","collie","doberman"]
for raza in razasDog:
 listbox.insert(END,raza)
listbox.pack()
label = Label(text="Razas Caninas")
label.pack()
window.mainloop()