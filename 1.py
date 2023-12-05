from tkinter import *
#from tkinter import PhotoImage

root=Tk()
root.geometry('2400x800')
root.title('busBookingSystem')

fs1=40
fst1=('Helvetica',fs1)
fs2=30
fst2=('Helvetica',fs2)
fs3=24
fst3=('Helvetica',fs3)

#image=PhotoImage(file="C:\Users\Dheeraj verma\Desktop\pythonPro\media\bus.jpg")
#Label.config(image=image).pack()

Label(root,text="Bus Booking System",  fg="red",bg="cyan", font=fst1).pack()
Label(root,text="Name: Dheeraj verma\n", fg="blue", font=fst3).pack()
Label(root,text="Enrl: 221B145\n", fg="blue", font=fst3).pack()
Label(root,text="Mobile: 8957250428\n", fg="blue", font=fst3).pack()

Label(root,text="Submitted To: Prof. Mahesh Kumar",  fg="red",bg="cyan",font=fst2).pack()
Label(root,text="Project based learning\n",  fg="red", font=fst3).pack()

root.mainloop()
