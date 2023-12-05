from tkinter import *
root=Tk()

root.geometry('2400x600')
root.title('busBookingSystem')

fs1=40
fst1=('Helvetica',fs1)
fs2=30
fst2=('Helvetica',fs2)
fs3=18
fst3=('Helvetica',fs3)


Label(root,text="Online Bus Booking System", fg="red",bg="cyan", font=fst1).grid(row=0, column=2)

Label(root,text="Add Bus Details",bg="green" , font=fst3).grid(row=1, column=2)

Label(root,text="Bus id", font=fst3).grid(row=2, column=0)
var1=Entry(root)
var1.grid(row=2, column=1)

#dropdown
op=StringVar()
op.set("Bus type")
option=["AC2X2","AC3X2","Non AC2X2","Non AC3X2","AC-Sleeper 2x1","Non-AC Sleeper 2X1"]
OptionMenu(root,op,*option).grid(row=2,column=2)

Label(root,text="Capacity", font=fst3).grid(row=2, column=3)
var2=Entry(root)
var2.grid(row=2, column=4)

Label(root,text="Fare Rs", font=fst3).grid(row=2, column=5)
var3=Entry(root)
var3.grid(row=2, column=6)

Label(root,text="Option ID", font=fst3).grid(row=3, column=0)
var4=Entry(root)
var4.grid(row=3, column=1)

Label(root,text="Route ID", font=fst3).grid(row=3, column=2)
var5=Entry(root)
var5.grid(row=3, column=3)




Button(root,text="Add Bus", font=fst3).grid(row=3, column=4)
Button(root,text="Edit Bus", font=fst3).grid(row=3, column=5)
   

root.mainloop()


