from tkinter import *

def hero(value):
    variable.set(value)
    print("You have choosen path of",variable.get() + ".")

root = Tk()
variable = StringVar(root)
variable.set("Classes")

choose = OptionMenu(root,variable,"Warrior","Mage","Thief",command = hero)
choose.config(bg = "black",fg = "red")
choose.config(activeforeground = "white",activebackground = "blue")
choose.pack()

mainloop()
