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

Label(root,text="Check your booking",bg="green" , font=fst3).grid(row=1, column=2)

Label(root,text="Enter your mobile number: ", font=fst3).grid(row=2, column=0)
var1=Entry(root)
var1.grid(row=2, column=1)



Button(root,text="Check Booking", font=fst3).grid(row=2, column=2)  
    

root.mainloop()


