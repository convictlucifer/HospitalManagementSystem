from tkinter import*
import mysql.connector
from tkinter import ttk
from tkinter import ttk,messagebox
from tkcalendar import DateEntry
from PIL import Image,ImageTk


def login_func():
    if user_type_val.get()=='Admin':
        if email_val.get()=="" or pwd_val.get()=="":
            messagebox.showerror("error","All fields are required")
        else:
            em = email_val.get()
            pwd = pwd_val.get()

            db = mysql.connector.connect(host="localhost", user="root", password="", database="hospital")
            mycursor = db.cursor()
            try:
                mycursor.execute("select * from admin where email=%s and password=%s",(em,pwd))
                row=mycursor.fetchone()
                if row==None:
                    messagebox.showerror("error","Invalid UserID/Password")
                else:
                    messagebox.showinfo("Success", "Welcome admin")
                    top.destroy()
                    import home
                db.commit()

            except EXCEPTION as e:
                print(e)
                db.rollback()
                db.close()
    elif user_type_val.get()=='Patient':
        if email_val.get()=="" or pwd_val.get()=="":
            messagebox.showerror("error","All fields are required")
        else:
            em = email_val.get()
            pwd = pwd_val.get()

            db = mysql.connector.connect(host="localhost", user="root", password="", database="hospital")
            mycursor = db.cursor()
            try:
                mycursor.execute("select * from patient where email=%s and password=%s",(em,pwd))
                row=mycursor.fetchone()
                if row==None:
                    messagebox.showerror("error","Invalid UserID/Password")
                else:
                    messagebox.showinfo("Success", "Welcome Patient")
                    top.destroy()
                    import patient_dash
                db.commit()

            except EXCEPTION as e:
                print(e)
                db.rollback()
                db.close()

    elif user_type_val.get()=='Doctor':
        if email_val.get()=="" or pwd_val.get()=="":
            messagebox.showerror("error","All fields are required")
        else:
            em = email_val.get()
            pwd = pwd_val.get()

            db = mysql.connector.connect(host="localhost", user="root", password="", database="hospital")
            mycursor = db.cursor()
            try:
                mycursor.execute("select * from doctor where email=%s and password=%s",(em,pwd))
                row=mycursor.fetchone()
                if row==None:
                    messagebox.showerror("error","Invalid UserID/Password")
                else:
                    messagebox.showinfo("Success", "Welcome Doctor")
                    top.destroy()
                    import doctor_dash
                    doctor_dash.start_doctor_dash(top,em)
                db.commit()

            except EXCEPTION as e:
                print(e)
                db.rollback()
                db.close()

top=Tk()
top.title("Login")
top.geometry("400x300")
top.iconbitmap(r'medkit.ico')
mangefrm=Frame(top,bd=2,relief=RIDGE,bg="light blue")
mangefrm.place(x=0,y=0,width=398,height=298)

user_type=Label(mangefrm,text="Login as: ",font=("Times New Roman",15,"bold"),bg="light blue")
user_type.grid(row=1,column=0,pady=20,padx=30,sticky="w")
user_type_val=ttk.Combobox(mangefrm,font=("Times New Roman",12,"bold"),state="readonly")
user_type_val["values"]=("SELECT","Patient","Admin","Doctor")
user_type_val.grid(row=1,column=1,pady=20,padx=30,sticky="w")
user_type_val.current(0)

email=Label(mangefrm,text="Email",font=("Times New Roman",15,"bold"),bg="light blue")
email.grid(row=2,column=0,pady=20,padx=30,sticky="w")
email_val=Entry(mangefrm,font=("Times New Roman",12,"bold"),bd=5,relief=GROOVE)
email_val.grid(row=2,column=1,pady=20,padx=30,sticky="w")

pwd=Label(mangefrm,text="Password",font=("Times New Roman",15,"bold"),bg="light blue")
pwd.grid(row=3,column=0,pady=20,padx=30,sticky="w")
pwd_val=Entry(mangefrm,show="*",font=("Times New Roman",12,"bold"),bd=5,relief=GROOVE)
pwd_val.grid(row=3,column=1,pady=20,padx=30,sticky="w")

loginbtn=Button(top,text="Login",command=login_func,width=12,bg='orange').grid(row=4,column=1,padx=150,pady=250)
top.mainloop()