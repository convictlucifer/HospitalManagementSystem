from tkinter import*
import mysql.connector
from tkinter import ttk
from tkinter import ttk,messagebox
from tkcalendar import DateEntry
from PIL import Image,ImageTk

def login():
    top.destroy()
    import login

def register():
    top.destroy()
    import reg_doc_patient

top=Tk()
top.title("HOSPITAL MANAGEMENT SYSTEM")
top.geometry("400x300")
top.iconbitmap(r'medkit.ico')
img =Image.open('home_bg.jpg')
bg = ImageTk.PhotoImage(img)
label = Label(top, image=bg)
label.place(x =0,y = 0,relwidth=1,relheight=1)
loginbtn=Button(top,text="Login",command=login,width=12,bg='lightblue').grid(row=1,column=0,padx=150,pady=80)
registerbtn=Button(top,text="Register",command=register,width=12,bg='lightblue').grid(row=2,column=0,padx=150,pady=0)
top.mainloop()