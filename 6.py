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

Label(root,text="Add New Details To Database" , font=fst3).grid(row=1, column=2)


Button(root,text="New Operator", font=fst3).grid(row=2, column=1)
Button(root,text="New Bus", font=fst3).grid(row=2, column=2)
Button(root,text="New Route", font=fst3).grid(row=2, column=3)
Button(root,text="New Run", font=fst3).grid(row=2, column=4)

root.mainloop()


