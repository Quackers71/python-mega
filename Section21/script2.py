from tkinter import *

window=Tk()

def kg_conversions():
    t1.delete(1.0,END)
    grams=float(e1_value.get())*1000.0
    t1.insert(END,grams)

    t2.delete(1.0,END)
    pounds=float(e1_value.get())*2.20462
    t2.insert(END,pounds)

    t3.delete(1.0,END)
    ounces=float(e1_value.get())*35.274
    t3.insert(END,ounces)

# root=Tk()
# kgs=Label(root, text="Kgs")
# kgs.grid(row=0,column=0)

b1=Button(window,text="Convert", command=kg_conversions)
b1.grid(row=0,column=3)


e1_value=StringVar()
e1=Entry(window, textvariable=e1_value)
e1.grid(row=0,column=1)

e2_value=StringVar()
e2=Entry(window, textvariable=e1_value)

e3_value=StringVar()
e3=Entry(window, textvariable=e1_value)


t1=Text(window,height=1,width=20)
t1.grid(row=1,column=0)

t2=Text(window,height=1,width=20)
t2.grid(row=1,column=1)

t3=Text(window,height=1,width=20)
t3.grid(row=1,column=3)

window.mainloop()