from tkinter import*
import mysql.connector
from tkinter import ttk
from tkinter import ttk,messagebox
from tkcalendar import DateEntry
from PIL import Image,ImageTk


def reg_func():
    if days_box.get()=="" or name_box.get()=="" or address_box.get()=="" or contact_box.get()=="" or dg_box.get()=="" or email_box.get()=="" or password_box.get()=="":
        messagebox.showerror("Error","All fields are required")
    else:
        days_val=days_box.get()
        name_val=name_box.get()
        address_val=address_box.get()
        contact_val=contact_box.get()
        dob_val=dob_box.get()
        dg_val=dg_box.get()
        gender_val=radio.get()
        email_val=email_box.get()
        pwd_val=password_box.get()
        db = mysql.connector.connect(host="localhost", user="root", password="", database="hospital")
        mycursor = db.cursor()
        try:
            sql="insert into doctor(name,address,contact,dob,speciality,gender,email,password,available_days,slots,fees)values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
            val=(name_val,address_val,contact_val,dob_val,dg_val,gender_val,email_val,pwd_val,days_val,50,int(fees_box.get())+300)
            mycursor.execute(sql,val)
            db.commit()
            messagebox.showinfo("Information","Record Inserted Successfully")
            days_box.delete(0, END)
            name_box.delete(0, END)
            address_box.delete(0, END)
            contact_box.delete(0, END)
            dob_box.delete(0, END)
            dg_box.delete(0, END)
            email_box.delete(0, END)
            password_box.delete(0, END)
            fees_box.delete(0, END)
            days_box.focus_set()

        except EXCEPTION as e:
            print(e)
            db.rollback()
            db.close()

def lg_func():
    root.destroy()
    import home


root=Tk()
root.title('Doctor Register Page')
root.geometry('900x900')
root.iconbitmap(r'medkit.ico')
frame1=Frame(root,bg='red',highlightbackground='black',highlightthickness=4)
frame1.place(x=0,y=0,width=1528,height=100)
banner=Label(frame1,text="Welcome to ABC Hospital",font=("Monotype Corsiva",25,"bold"),fg="black")
banner.place(x=300,y=20)
frame2=Frame(root,bg='lightblue',highlightbackground='black',highlightthickness=2)
frame2.place(x=0,y=102,width=1500,height=680)
fr2_heading=Label(frame2,text="Doctor Registration Form",font=("Monotype Corsiva",20,"bold"),fg='black',bg='lightblue')
fr2_heading.place(x=360,y=50)

days=Label(frame2,text="Availablity",font=("Times",15,"bold"),fg='black',bg='lightblue')
days.place(x=340,y=150)
days_box=Entry(frame2)
days_box.place(x=440,y=155,width=140,bordermode='outside')

name=Label(frame2,text="Name",font=("Times",15,"bold"),fg='black',bg='lightblue')
name.place(x=340,y=200)
name_box=Entry(frame2)
name_box.place(x=440,y=205,width=140,bordermode='outside')

address=Label(frame2,text="Address",font=("Times",15,"bold"),fg='black',bg='lightblue')
address.place(x=340,y=250)
address_box=Entry(frame2)
address_box.place(x=440,y=255,width=140,bordermode='outside')

contact=Label(frame2,text="Contact",font=("Times",15,"bold"),fg='black',bg='lightblue')
contact.place(x=340,y=300)
contact_box=Entry(frame2)
contact_box.place(x=440,y=305,width=140,bordermode='outside')

dob=Label(frame2,text="DOB",font=("Times",15,"bold"),fg='black',bg='lightblue')
dob.place(x=340,y=350)
dob_box = DateEntry(frame2,font=("Times New Roman",15,"bold"),background='gray',foreground='white',borderwidth=2)
dob_box.place(x=440,y=355,width=140,height=20)

designation=Label(frame2,text="Spiciality",font=("Times",15,"bold"),fg='black',bg='lightblue')
designation.place(x=340,y=400)
dg_box=ttk.Combobox(frame2,textvariable="vcourse",font=("Times New Roman",10,"bold"),state="readonly")
dg_box["values"]=("SELECT","General Surgeon","Opthalmologist","Pedeiatric","Neurologist")
dg_box.place(x=440,y=405,width=140,height=20)
dg_box.current(0)

gender=Label(frame2,text="Gender",font=("Times",15,"bold"),fg='black',bg='lightblue')
gender.place(x=340,y=450)
radio = StringVar()
m = Radiobutton(frame2,text="Male",variable=radio,value="Male",bg="lightblue",font=("Times New Roman",15,"bold"))
m.place(x=410,y=455,width=180,height=20)
f=Radiobutton(frame2, text="Female", variable=radio, value="Female",bg="lightblue",font=("Times New Roman",15,"bold"))
f.place(x=550,y=455,width=180,height=20)

email=Label(frame2,text="Email",font=("Times",15,"bold"),fg='black',bg='lightblue')
email.place(x=340,y=500)
email_box=Entry(frame2)
email_box.place(x=440,y=505,width=140,bordermode='outside')

password=Label(frame2,text="Password",font=("Times",15,"bold"),fg='black',bg='lightblue')
password.place(x=340,y=550)
password_box=Entry(frame2,show="*")
password_box.place(x=440,y=555,width=140,bordermode='outside')

fees=Label(frame2,text="Fees",font=("Times",15,"bold"),fg='black',bg='lightblue')
fees.place(x=340,y=600)
fees_box=Entry(frame2)
fees_box.place(x=440,y=605,width=140,bordermode='outside')

reg_btn=Button(frame2,text="Register",command=reg_func,font=("Times New Roman",12,"bold"))
reg_btn.place(x=400,y=640)

lg_btn=Button(frame2,text="Login",command=lg_func,font=("Times New Roman",12,"bold"))
lg_btn.place(x=500,y=640)

root.mainloop()
