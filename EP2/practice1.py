from tkinter import *
from tkinter import ttk

#Font
font1 = ("Arial", 22)
GUI = Tk()
GUI.title("EP2 Practice 1")
GUI.geometry("350x500+650+200")


### ROW 1 ###
L1 = Label(GUI, text="Product", font=font1)
L1.pack()

v_product = StringVar()

B1 = Entry(GUI, textvariable=v_product)
B1.pack()

### ROW 2 ###
L2 = Label(GUI, text="Product", font=font1)
L2.pack()

v_product = StringVar()

B2 = Entry(GUI, textvariable=v_product)
B2.pack()

### ROW 1 ###
L = Label(GUI, text="Product", font=font1)
L1.pack()

v_product = StringVar()

B1 = Entry(GUI, textvariable=v_product)
B1.pack()

GUI.mainloop()