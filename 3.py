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

Label(root,text="Enter Journey Details",bg="green" , font=fst3).grid(row=1, column=2)

Label(root,text="To", font=fst3).grid(row=2, column=0)
var1=Entry(root)
var1.grid(row=2, column=1)

Label(root,text="From", font=fst3).grid(row=2, column=2)
var2=Entry(root)
var2.grid(row=2, column=3)

Label(root,text="Journey date", font=fst3).grid(row=2, column=4)
var3=Entry(root)
var3.grid(row=2, column=5)


Button(root,text="Show Bus",font=fst3).grid(row=2, column=6)

#adding database functionality later
'''
def fun():
'''  
    

root.mainloop()


