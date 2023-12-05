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

Label(root,text="Add Bus Operator Details",bg="green" , font=fst3).grid(row=1, column=2)

Label(root,text="Operator id", font=fst3).grid(row=2, column=0)
var1=Entry(root)
var1.grid(row=2, column=1)

Label(root,text="Name", font=fst3).grid(row=2, column=2)
var2=Entry(root)
var2.grid(row=2, column=3)

Label(root,text="Address", font=fst3).grid(row=2, column=4)
var3=Entry(root)
var3.grid(row=2, column=5)

Label(root,text="Phone", font=fst3).grid(row=2, column=6)
var3=Entry(root)
var3.grid(row=2, column=7)

Label(root,text="Email", font=fst3).grid(row=3, column=1)
var3=Entry(root)
var3.grid(row=3, column=2)


Button(root,text="Add", font=fst3).grid(row=3, column=3)
Button(root,text="Edit", font=fst3).grid(row=3, column=4)

#adding database functionality later
'''
def fun():
'''  
    

root.mainloop()


