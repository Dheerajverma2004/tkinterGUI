from tkinter import *
import sqlite3

root=Tk()
root.geometry('2400x800')
root.title('busBookingSystem')

connections=sqlite3.connection("BxDB") #database
cur=connection.cursor()

cur.execute('create table if not exists busDetails(To varchar(30) , from varchar(30), journeyDate date)')
cur.execute('insert into busDetails values(guna,lucknow,1/12/2023')
cur.execute('insert into busDetails values(guna,indore,29/11/2023')
cur.execute('insert into busDetails values(guna,bhopal,29/12/2023')
cur.execute('select * from busDetails')
cur.fetchcall()
cur.commit()
