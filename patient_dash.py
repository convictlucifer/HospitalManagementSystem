from tkinter import*
import mysql.connector
from tkinter import ttk
from tkinter import ttk,messagebox
from tkcalendar import DateEntry
from PIL import Image,ImageTk

def book_appointment():
    top.destroy()
    import patient_book_appointment

def manage_appointment():
    top.destroy()
    import patient_manage_appointment

top=Tk()
top.title("Patient Dash")
top.geometry("400x300")
top.iconbitmap(r'medkit.ico')
img =Image.open('home_bg.jpg')
bg = ImageTk.PhotoImage(img)
label = Label(top, image=bg)
label.place(x =0,y = 0,relwidth=1,relheight=1)
btn1=Button(top,text="Book Appointment",command=book_appointment,width=17,bg='lightblue').grid(row=1,column=0,padx=150,pady=90)
btn2=Button(top,text="Manage Appointment",command=manage_appointment,width=17,bg='lightblue').grid(row=2,column=0,padx=150,pady=0)
top.mainloop()