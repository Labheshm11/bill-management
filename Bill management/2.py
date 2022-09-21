from cgitb import reset, text
from tkinter import*
root=Tk()
root.geometry("1000x500")
root.title("bill management")
root.resizable(False,False)
def Reset():
    entry_coffee.delete(0,END)
    entry_dosa.delete(0,END)
    entry_mango_shake.delete(0,END)
    entry_eggs.delete(0,END)
    entry_pizza.delete(0,END)

def Total():
    try:a1=int(dosa.get())
    except:a1=0 
    
    try:a2=int(coffee.get())
    except:a2=0 
    
    try:a3=int(pizza.get())
    except:a3=0 
    
    try:a4=int(mango_shake.get())
    except:a4=0 
    
    try:a5=int(eggs.get())
    except:a5=0 

    c1=60*a1
    c2=70*a2
    c3=16*a3
    c4=20*a4
    c5=36*a5

    lbl_total=Label(f2,font=("aria",20,"bold"),text="Total",width=16,fg="lightgreen",bg="black")
    lbl_total.place(x=0,y=50)

    entry_total=Entry(f2,font=("aria",20,"bold"),textvariable=Total_bill,bd=6,width=15,bg="lightgreen")
    entry_total.place(x=20,y=100)

    total_cost=c1+c2+c3+c4+c5
    string_bill="Rs.",str("%.2f" %total_cost)
    Total_bill.set(string_bill)

Label(text="Bill management",bg="black",fg="white",font=("calibri",33),width="300",height="2").pack()

#menu  card
f=Frame(root,bg="lightgreen",highlightbackground="black",highlightthickness=1,width=312,height=370)
f.place(x=10,y=118)

Label(f,text="Menu",font=("Gabriola",40,"bold"),fg="black",bg="lightgreen").place(x=80,y=0)
Label(f,font=("Lucida Calligraphy",15,"bold"),text="dosa......Rs.60/plate",fg="black",bg="lightgreen").place(x=10,y=80)
Label(f,font=("Lucida Calligraphy",15,"bold"),text="pizza......Rs.70/base",fg="black",bg="lightgreen").place(x=10,y=110)
Label(f,font=("Lucida Calligraphy",15,"bold"),text="coffe......Rs.16/cup",fg="black",bg="lightgreen").place(x=10,y=140)
Label(f,font=("Lucida Calligraphy",15,"bold"),text="mango-shake...Rs.20/glass",fg="black",bg="lightgreen").place(x=6,y=170)
Label(f,font=("Lucida Calligraphy",15,"bold"),text="eggs......Rs.36/pack",fg="black",bg="lightgreen").place(x=10,y=200)

#Bill
f2=Frame(root,bg="lightyellow",highlightbackground="black",highlightthickness=1,width=300,height=370)
f2.place(x=690,y=118)

Bill=Label(f2,text="Bill",font=("calibri",20),bg="lightyellow")
Bill.place(x=120,y=10)

#entry work
f1=Frame(root,bd=5,height=370,width=300,relief=RAISED)
f1.pack()

dosa=StringVar()
pizza=StringVar()
coffee=StringVar()
mango_shake=StringVar()
eggs=StringVar()
Total_bill=StringVar()

#label
l_dosa=Label(f1,font=("aria",20,"bold"),text="dosa",width=12,fg="blue4")
l_pizza=Label(f1,font=("aria",20,"bold"),text="pizza",width=12,fg="blue4")
l_coffee=Label(f1,font=("aria",20,"bold"),text="coffee",width=12,fg="blue4")
l_mango_shake=Label(f1,font=("aria",20,"bold"),text="mango_shake",width=12,fg="blue4")
l_eggs=Label(f1,font=("aria",20,"bold"),text="eggs",width=12,fg="blue4")

l_dosa.grid(row=1,column=0)
l_pizza.grid(row=2,column=0)
l_coffee.grid(row=3,column=0)
l_mango_shake.grid(row=4,column=0)
l_eggs.grid(row=5,column=0)


#entry
entry_dosa=Entry(f1,font=("aria",20,"bold"),textvariable=dosa,bd=6,width=8,bg="lightpink")
entry_dosa.grid(row=1,column=1)
entry_pizza=Entry(f1,font=("aria",20,"bold"),textvariable=pizza,bd=6,width=8,bg="lightpink")
entry_pizza.grid(row=2,column=1)
entry_coffee=Entry(f1,font=("aria",20,"bold"),textvariable=coffee,bd=6,width=8,bg="lightpink")
entry_coffee.grid(row=3,column=1)
entry_mango_shake=Entry(f1,font=("aria",20,"bold"),textvariable=mango_shake,bd=6,width=8,bg="lightpink")
entry_mango_shake.grid(row=4,column=1)
entry_eggs=Entry(f1,font=("aria",20,"bold"),textvariable=eggs,bd=6,width=8,bg="lightpink")
entry_eggs.grid(row=5,column=1)

#buttons
btn_reset=Button(f1,bd=5,fg="black",bg="lightblue",font=("ariel",16,"bold"),width=10,text="Reset",command=Reset)
btn_reset.grid(row=8,column=0)

btn_total=Button(f1,bd=5,fg="black",bg="lightblue",font=("ariel",16,"bold"),width=10,text="Total",command=Total)
btn_total.grid(row=8,column=1)
root.mainloop()