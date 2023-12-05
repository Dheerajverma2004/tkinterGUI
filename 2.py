from tkinter import *
root=Tk()
root.geometry('2400x800')
root.title('busBookingSystem')

fs1=40
fst1=('Helvetica',fs1)
fs2=30
fst2=('Helvetica',fs2)
fs3=24
fst3=('Helvetica',fs3)


Label(root,text="Online Bus Booking System", fg="green",bg="cyan", font=fst1).grid(row=0, column=2)

Label(root,text="Seat Booking",bg="green", font=fst2).grid(row=1,column=1)
Label(root,text="Check Booked Seat",bg="green", font=fst2).grid(row=1,column=2)
Label(root,text="Add Bus Details",bg="green", font=fst2).grid(row=1,column=3)

Label(root,text="For Admin Only", fg="red", font=fst3).grid(row=2,column=3)

root.mainloop()
