from tkinter import *

cc=0
def clicks(event):
    global cc
    cc+=1
    btn.config(text=cc)

def remove_clicks(event):
    global cc
    cc-=1
    btn.config(text=cc)

def txt_to_lbl(event):
    text=txt.get()
    lbl.configure(text=text)
    txt.delete(0,END)

def valimine():
    valik=var.get()
    lbl.configure(text=valik)


window=Tk()
window.title("Window's name")
window.geometry("800x620")
btn=Button(window,text="Click me, or noob",font="Sans 20",width=20,bg="#cbbeb5",fg="Black",relief=RAISED)
btn.pack()#side - LEFT
btn.bind("<Button-1>",clicks)
btn.bind("<Button-3>",remove_clicks)
lbl=Label(window,text="...",height=3,width=20,font="Arial 20",fg="Black",bg="#00d1dc",relief="solid")
lbl.pack()
txt=Entry(window,width=20,font="Sans 20",fg="Black",bg="#00d1dc",justify=CENTER)
txt.pack()
txt.bind("<Return>",txt_to_lbl)#Enter
i1=PhotoImage(file="1.gif")
i2=PhotoImage(file="2.png")
i3=PhotoImage(file="3.gif")
var=StringVar()
var.set("One")

r1=Radiobutton(window,image=i1,variable=var,value="One",command=valimine)
r2=Radiobutton(window,image=i2,variable=var,value="Two",command=valimine)
r3=Radiobutton(window,image=i3,variable=var,value="Three",command=valimine)
r1.pack(side=LEFT)
r2.pack(side=LEFT)
r3.pack(side=LEFT)

window.mainloop()