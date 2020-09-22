#GUIcalculator.py
from tkinter import *
from tkinter import ttk #theme for lable and entry
import csv

font_title = ("arial", 22)
font_result= ("arial", 14)
GUI = Tk()
GUI.title('Program calculator')
GUI.geometry('300x380+500+200') 

## TAB 
from tkinter.ttk import Notebook

Tab = Notebook(GUI)
F1 = Frame(Tab)
F2 = Frame(Tab)
F3 = Frame(Tab)

Tab.add(F1, text="Sales")
Tab.add(F2, text="Product")
Tab.add(F3, text="History")
Tab.pack(fill=BOTH, expand=1)




## Row1
L1 = ttk.Label(F1, text='Product', font=font_title)
L1.pack(pady=10) # for c center aglin

v_product = StringVar() #String var คือกล่อง ใส่ตัวแปรที่เปี่ยนแปลงได้

B1 = ttk.Entry(F1, textvariable=v_product) 
B1.pack()

## Row2
L2 = ttk.Label(F1, text='Price', font=font_title)
L2.pack(pady=10) # for c center aglin

v_price = StringVar() #box2 

B2 = ttk.Entry(F1, textvariable=v_price) 
B2.pack()

## Row3
L3 = ttk.Label(F1, text='Amount', font=font_title)
L3.pack(pady=10) # for c center aglin

v_amount = StringVar() #box3

B3 = ttk.Entry(F1, textvariable=v_amount) 
B3.pack()

#button

def Write(listdata): 
    print("Writing...")
    with open('EP2/data.csv', 'a', newline='', encoding='UTF-8') as file:
	    f = csv.writer(file)
	    f.writerow(listdata)
    print("Finished")

def Calc():
    pd = v_product.get() # .get() พนักงานเปีดกล่องดุว่ามีอะไรบ้างในนั้น
    pc = v_price.get()
    am = v_amount.get()
    cal = int(pc) * int(am)
    Write([pd,pc,am,cal])
    text_result = f'สินค้า : {pd}, ลาคา : {pc}, จำนวน : {am}'
    text_result = text_result + f'\nรวมคา {cal} '
    v_result.set(text_result)

But_1 = ttk.Button(F1, text='calculate',command=Calc)
But_1.pack(ipadx=10, ipady=5, pady = 20)

#result
v_result = StringVar()
v_result.set("----------RESULT----------")

R1 = ttk.Label(F1, textvariable=v_result,font=font_result) 
R1.pack()

GUI.mainloop()