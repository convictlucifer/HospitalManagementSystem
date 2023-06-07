from tkinter import*
import mysql.connector
from tkinter import ttk
from tkinter import ttk,messagebox
from tkcalendar import DateEntry
from PIL import Image,ImageTk

def register():
    if user_type_val.get()=="Patient":
        top.destroy()
        import reg_patient
    elif user_type_val.get()=="Doctor":
        top.destroy()
        import register_doctor

top=Tk()
top.title("HOSPITAL MANAGEMENT SYSTEM")
top.geometry("400x200")
top.iconbitmap(r'medkit.ico')
mangefrm=Frame(top,bd=2,relief=RIDGE,bg="light blue")
mangefrm.place(x=0,y=0,width=398,height=200)

user_type=Label(mangefrm,text="Register as: ",font=("Times New Roman",15,"bold"),bg="light blue")
user_type.grid(row=1,column=0,pady=20,padx=30,sticky="w")
user_type_val=ttk.Combobox(mangefrm,font=("Times New Roman",12,"bold"),state="readonly")
user_type_val["values"]=("SELECT","Patient","Doctor")
user_type_val.grid(row=1,column=1,pady=20,padx=30,sticky="w")
user_type_val.current(1)


registerbtn=Button(top,text="Register",command=register,width=12,bg='lightblue').grid(row=2,column=0,padx=150,pady=100)
top.mainloop()