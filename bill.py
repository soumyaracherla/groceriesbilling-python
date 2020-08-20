from typing import Any

from tkinter import*
import random
import time

root = Tk()
root.geometry("890x580+0+0")
root.title("GROCERIES BILLING")


Tops = Frame(root,bg="white",width = 2000,height=50)
Tops.pack(side=TOP)

f1 = Frame(root,width = 900,height=700)
f1.pack(side=LEFT)

f2 = Frame(root ,width = 400,height=700)
f2.pack(side=RIGHT)

#TIME
localtime=time.asctime(time.localtime(time.time()))

#INFO TOP
info = Label(Tops, font=( 'aria',30,'bold'),text="GENERAL STORE",fg="blue",bd=10)
info.grid(row=0,column=0)

info = Label(Tops, font=( 'aria',20 ),text=localtime,fg="steel blue")
info.grid(row=1,column=0)


def Ref():
    x = random.randint(12980, 50876)
    randomRef = str(x)
    rand.set(randomRef)

    cor =float(Rice.get())
    cow= float(Wheat.get())
    coo= float(Oil.get())
    cos= float(Sugar.get())
    cod= float(Dal.get())
    coc= float(Cornflakes.get())

    costofrice = cor*120
    costofwheat = cow*25
    costofoil = coo*100
    costofsugar = cos*60
    costofdal = cod*70
    costofcornflakes = coc*180

    costofitems = "Rs.", str('%.2f' % (costofrice + costofwheat + costofoil + costofsugar + costofdal + costofcornflakes))
    PayTax = ((costofrice + costofwheat + costofoil + costofsugar + costofdal + costofcornflakes) * 0.33)
    Totalcost = (costofrice + costofwheat + costofoil + costofsugar + costofdal + costofcornflakes)
    Ser_Charge = ((costofrice + costofwheat + costofoil + costofsugar + costofdal + costofcornflakes) / 99)
    Service = "Rs.", str('%.2f' % Ser_Charge)
    OverAllCost = "Rs.", str(PayTax + Totalcost + Ser_Charge)
    PaidTax = "Rs.", str('%.2f' % PayTax)

    Service_Charge.set(Service)
    cost.set(costofitems)
    Tax.set(PaidTax)
    Subtotal.set(costofitems)
    Total.set(OverAllCost)


def qexit():
    root.destroy()

def reset():
    rand.set("")
    Rice.set("")
    Wheat.set("")
    Oil.set("")
    Sugar.set("")
    Total.set("")
    Dal.set("")
    Cornflakes.set("")
    Subtotal.set("")
    Service_Charge.set("")
    Tax.set("")
    cost.set("")


rand = StringVar()
Rice = StringVar()
Wheat = StringVar()
Oil = StringVar()
Sugar = StringVar()
Dal = StringVar()
Total = StringVar()
Cornflakes = StringVar()
Tax = StringVar()
cost = StringVar()
Service_Charge = StringVar()
Subtotal = StringVar()

lbreference = Label(f1, font=( 'aria' ,16, 'bold' ),text="Order No.",fg="black",bd=20,anchor='w')
lbreference.grid(row=0,column=0)
txtreference = Entry(f1,font=('ariel' ,16,'bold'),textvariable=rand , bd=6,insertwidth=6,bg="red" ,justify='right')
txtreference.grid(row=0,column=1)

lbwheat = Label(f1, font=( 'aria' ,16, 'bold' ),text=" Wheat ",fg="black",bd=10,anchor='w')
lbwheat.grid(row=2,column=0)
txtwheat = Entry(f1,font=('ariel' ,16,'bold'), textvariable=Wheat, bd=6,insertwidth=4,bg="gray" ,justify='right')
txtwheat.grid(row=2,column=1)

lboil = Label(f1, font=( 'aria' ,16, 'bold' ),text="Oil ",fg="black",bd=10,anchor='w')
lboil.grid(row=3,column=0)
txtoil = Entry(f1,font=('ariel' ,16,'bold'), textvariable=Oil ,bd=6,insertwidth=4,bg="gray" ,justify='right')
txtoil.grid(row=3,column=1)


lbsugar = Label(f1, font=( 'aria' ,16, 'bold' ),text="Sugar",fg="black",bd=10,anchor='w')
lbsugar.grid(row=4,column=0)
txtsugar = Entry(f1,font=('ariel' ,16,'bold'), textvariable=Sugar, bd=6,insertwidth=4,bg="gray" ,justify='right')
txtsugar.grid(row=4,column=1)

lbdal = Label(f1, font=( 'aria' ,16, 'bold' ),text="Dal",fg="black",bd=10,anchor='w')
lbdal.grid(row=5,column=0)
txtdal= Entry(f1,font=('ariel' ,16,'bold'), textvariable=Dal ,bd=6,insertwidth=4,bg="gray" ,justify='right')
txtdal.grid(row=5,column=1)

lbcornflakes = Label(f1, font=( 'aria' ,16, 'bold' ),text="CornFlakes",fg="black",bd=10,anchor='w')
lbcornflakes.grid(row=6,column=0)
txtcornflakes = Entry(f1,font=('ariel' ,16,'bold'),textvariable=Cornflakes , bd=6,insertwidth=4,bg="gray",justify='right')
txtcornflakes.grid(row=6,column=1)


lbrice = Label(f1, font=( 'aria' ,16, 'bold'),text="Rice",fg="black",bd=10,anchor='w')
lbrice.grid(row=1,column=0)
txtrice = Entry(f1,font=('ariel' ,16,'bold'), textvariable=Rice ,bd=6,insertwidth=4,bg="gray" ,justify='right')
txtrice.grid(row=1,column=1)

lbcost = Label(f1, font=( 'aria' ,16, 'bold' ),text="Cost",fg="black",bd=10,anchor='w')
lbcost.grid(row=2,column=2)
txtcost = Entry(f1,font=('ariel' ,16,'bold'), textvariable=cost , bd=6,insertwidth=4,bg="red" ,justify='right')
txtcost.grid(row=2,column=3)

lbService_Charge = Label(f1, font=( 'aria' ,16, 'bold' ),text="Service Charge",fg="black",bd=10,anchor='w')
lbService_Charge.grid(row=3,column=2)
txtService_Charge = Entry(f1,font=('ariel' ,16,'bold'), textvariable=Service_Charge , bd=6,insertwidth=4,bg="red" ,justify='right')
txtService_Charge.grid(row=3,column=3)

lbTax = Label(f1, font=( 'aria' ,16, 'bold' ),text="Tax",fg="black",bd=10,anchor='w')
lbTax.grid(row=4,column=2)
txtTax = Entry(f1,font=('ariel' ,16,'bold'), textvariable=Tax , bd=6,insertwidth=4,bg="red" ,justify='right')
txtTax.grid(row=4,column=3)

lbSubtotal = Label(f1, font=( 'aria' ,16, 'bold' ),text="Subtotal",fg="black",bd=10,anchor='w')
lbSubtotal.grid(row=5,column=2)
txtSubtotal = Entry(f1,font=('ariel' ,16,'bold'), textvariable=Subtotal , bd=6,insertwidth=4,bg="red" ,justify='right')
txtSubtotal.grid(row=5,column=3)

lbTotal = Label(f1, font=( 'aria' ,16, 'bold'),text="Total",fg="black",bd=10,anchor='w')
lbTotal.grid(row=6,column=2)
txtTotal = Entry(f1,font=('ariel' ,16,'bold'), textvariable=Total, bd=6,insertwidth=4,bg="red" ,justify='right')
txtTotal.grid(row=6,column=3)

#buttons

lbTotal = Label(f1,text="---------------------",fg="white")
lbTotal.grid(row=7,columnspan=3)

btnTotal=Button(f1,padx=16,pady=8, bd=10 ,fg="black",font=('ariel' ,16,'bold'),width=10, text="TOTAL",bg="orange",command=Ref)
btnTotal.grid(row=8, column=1)

btnreset=Button(f1,padx=16,pady=8, bd=10 ,fg="black",font=('ariel' ,16,'bold'),width=10, text="RESET",bg="orange",command=reset)
btnreset.grid(row=8, column=2)

btnexit=Button(f1,padx=16,pady=8, bd=10 ,fg="black",font=('ariel',16,'bold'),width=10, text="EXIT", bg="orange",command=qexit)
btnexit.grid(row=8, column=3)

def price():
    roo = Tk()
    roo.geometry("600x220+0+0")
    roo.title("Price List")
    lbinfo = Label(roo, font=('aria', 15, 'bold'), text="Item",fg="black", bd=5)
    lbinfo.grid(row=0, column=0)

    lbinfo = Label(roo, font=('aria', 15,'bold'),text="_____________", fg="white", anchor=W)
    lbinfo.grid(row=0, column=2)

    lbinfo = Label(roo, font=('aria', 15, 'bold'),text="Price/kg", fg="black", anchor=W)
    lbinfo.grid(row=0, column=3)

    lbinfo = Label(roo, font=('aria', 15, 'bold'), text="Wheat",fg="steel blue", anchor=W)
    lbinfo.grid(row=1, column=0)
    lbinfo = Label(roo, font=('aria', 15, 'bold'), text="25",fg="steel blue", anchor=W)
    lbinfo.grid(row=1, column=3)

    lbinfo = Label(roo, font=('aria', 15, 'bold'), text="Oil ",fg="steel blue", anchor=W)
    lbinfo.grid(row=2, column=0)
    lbinfo = Label(roo, font=('aria', 15, 'bold'), text="100",fg="steel blue", anchor=W)
    lbinfo.grid(row=2, column=3)

    lbinfo = Label(roo, font=('aria', 15, 'bold'), text="Sugar ",fg="steel blue", anchor=W)
    lbinfo.grid(row=3, column=0)
    lbinfo = Label(roo, font=('aria', 15, 'bold'), text="60",fg="steel blue", anchor=W)
    lbinfo.grid(row=3, column=3)

    lbinfo = Label(roo, font=('aria', 15, 'bold'), text="Dal ",fg="steel blue", anchor=W)
    lbinfo.grid(row=4, column=0)
    lbinfo = Label(roo, font=('aria', 15, 'bold'), text="70",fg="steel blue", anchor=W)
    lbinfo.grid(row=4, column=3)

    lbinfo = Label(roo, font=('aria', 15, 'bold'), text="CornFlakes", fg="steel blue", anchor=W)
    lbinfo.grid(row=5, column=0)
    lbinfo = Label(roo, font=('aria', 15, 'bold'), text="180",fg="steel blue", anchor=W)
    lbinfo.grid(row=5, column=3)

    lbinfo = Label(roo, font=('aria', 15, 'bold'), text="Rice",fg="steel blue", anchor=W)
    lbinfo.grid(row=6, column=0)
    lbinfo = Label(roo, font=('aria', 15, 'bold'), text="120",fg="steel blue", anchor=W)
    lbinfo.grid(row=6, column=3)

    roo.mainloop()

btnprice=Button(f1,padx=16,pady=8, bd=10 ,fg="black",font=
('ariel' ,16,'bold'),width=10, text="PRICES",
bg="orange",command=price)
btnprice.grid(row=8, column=0)

root.mainloop()