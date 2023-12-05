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

Label(root,text="Add Bus Route Details",bg="green" , font=fst3).grid(row=1, column=2)

Label(root,text="Route id ", font=fst3).grid(row=2, column=0)
var1=Entry(root)
var1.grid(row=2, column=1)

Label(root,text="Station name ", font=fst3).grid(row=2, column=3)
var2=Entry(root)
var2.grid(row=2, column=4)

Label(root,text="Station id ", font=fst3).grid(row=2, column=5)
var3=Entry(root)
var3.grid(row=2, column=6)

Button(root,text="Add Route", font=fst3).grid(row=3, column=1)
Button(root,text="Delete Route", font=fst3).grid(row=3, column=2)
    

root.mainloop()


