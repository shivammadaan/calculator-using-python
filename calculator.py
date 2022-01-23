from tkinter import*
from tkinter import messagebox

root=Tk()

def kd():
    e1.delete(0,END)
def click(num):
    current=e1.get()
    e1.delete(0,END)
    e1.insert(0,str(current)+str(num))
def add():
    num1=e1.get()
    global no1
    no1=float(num1)
    global xx
    xx="add"
    e1.delete(0,END)
def sub():
    num1 = e1.get()
    global no1
    no1 = float(num1)
    global xx
    xx = "sub"
    e1.delete(0, END)
def mul():
    num1 = e1.get()
    global no1
    no1 = float(num1)
    global xx
    xx = "mul"
    e1.delete(0, END)
def div():
    num1 = e1.get()
    global no1
    no1 = float(num1)
    global xx
    xx = "div"
    e1.delete(0, END)
def eq():
    num2=e1.get()
    e1.delete(0,END)
    if xx=="add":
     e1.insert(0,float(num2)+no1)
    elif xx=="sub":
     e1.insert(0,no1-float(num2))
    elif xx == "mul":
        e1.insert(0, no1*float(num2))
    elif xx == "div":
        if float(num2)==0:
            e1.insert(0,'ERROR')
            messagebox.showerror('ERROR','Cannot Divide By Zero')
        elif num2 !=0:
            e1.insert(0, no1/float(num2))
    else:
        e1.insert(0,'error')
def ext():
    response=messagebox.askyesno('exit','wanna exit')
    if response==1:
        root.quit()




e1=Entry(root, width=20,bd=5)
e1.grid(row=0,column=1,columnspan=3)

b1=Button(root,text="1",padx=30,pady=20,command=lambda: click(1)).grid(row=1,column=1)
b2=Button(root,text="2",padx=30,pady=20,command=lambda: click(2)).grid(row=1,column=2)
b3=Button(root,text="3",padx=30,pady=20,command=lambda: click(3)).grid(row=1,column=3)
b4=Button(root,text="4",padx=30,pady=20,command=lambda: click(4)).grid(row=2,column=1)
b5=Button(root,text="5",padx=30,pady=20,command=lambda: click(5)).grid(row=2,column=2)
b6=Button(root,text="6",padx=30,pady=20,command=lambda: click(6)).grid(row=2,column=3)
b7=Button(root,text="7",padx=30,pady=20,command=lambda: click(7)).grid(row=3,column=1)
b8=Button(root,text="8",padx=30,pady=20,command=lambda: click(8)).grid(row=3,column=2)
b9=Button(root,text="9",padx=30,pady=20,command=lambda: click(9)).grid(row=3,column=3)
badd=Button(root,text="+",padx=29,pady=20,command=add,bg="pink").grid(row=4,column=1)
b0=Button(root,text="0",padx=30,pady=20,command=lambda: click(0)).grid(row=4,column=2)
B=Button(root, text="C",padx=30,pady=20, command=kd,bg="red").grid(row=4,column=3)
bsub=Button(root,text="-",padx=32,pady=20,command=sub,bg="pink").grid(row=5,column=1)
bmul=Button(root,text="X",padx=30,pady=20,command=mul,bg="pink").grid(row=5,column=2)
bdiv=Button(root,text="/",padx=32,pady=20,command=div,bg="pink").grid(row=5,column=3)
bE=Button(root,text="=",padx=105,pady=20,command=eq,bg="green").grid(row=6,column=1,columnspan=3)
bexit=Button(root,text="EXIT",padx=95,pady=20,command=ext,bg="red").grid(row=7,column=1,columnspan=3)
root.resizable(False,False)
root.mainloop()
