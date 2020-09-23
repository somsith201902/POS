from tkinter import *
from tkinter import ttk
import csv

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
L2 = Label(GUI, text="Price", font=font1)
L2.pack()

v_price = StringVar()

B2 = Entry(GUI, textvariable=v_price)
B2.pack()

### ROW 3 ###
L3 = Label(GUI, text="Amount", font=font1)
L3.pack()

v_amount = StringVar()

B1 = Entry(GUI, textvariable=v_amount)
B1.pack()

### Button ###

#function
def Write(texts):
    print("Writing")
    with open("data_p.csv", "a", newline="", encoding="UTF-8") as file:
        f = csv.writer(file)
        f.writerow(texts)
    print("finished")

def Calc():
    pd = v_product.get()
    pc = v_price.get()
    am = v_amount.get()
    total = int(pc) * int(am)
    rs = f"Product : {pd}, Price : {pc}, Amount : {am}\n Total = {total}"
    v_result.set(rs)
    Write([pd,pc,am,total])

but1 = Button(GUI, text="Calculater",command=Calc)
but1.pack(pady=10)

### Result ###
v_result = StringVar()
v_result.set("--------- Result Here! ---------")

result = Label(GUI, textvariable=v_result)
result.pack()

GUI.mainloop()