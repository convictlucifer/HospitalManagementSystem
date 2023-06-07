from tkinter import*
import mysql.connector
from tkinter import ttk
from tkcalendar import DateEntry
from tkinter import ttk,messagebox
from PIL import Image,ImageTk

rt=Tk()

rt.title("Update Doctor")

rt.geometry("1600x900+0+0")

title=Label(rt,text="Welcome to ABC Hospital",bd=10,relief=GROOVE,font=("Monotype Corsiva",35,"bold"),fg="darkgreen",bg="red")

title.pack(side=TOP,fill=X)

mangefrm=Frame(rt,bd=4,relief=RIDGE,bg="light blue")

mangefrm.place(x=20,y=100,width=450,height=680)

mtitle=Label(mangefrm,text="Manage Doctor",font=("Times New Roman",20,"bold"),fg="darkgreen",bg="light blue")

mtitle.grid(row=0,columnspan=2,pady=20)

days=Label(mangefrm,text="Availability",font=("Times New Roman",15,"bold"),bg="light blue")
days.grid(row=1,column=0,pady=10,padx=20,sticky="w")
days_box=Entry(mangefrm,font=("Times New Roman",15,"bold"),bd=5,relief=GROOVE)
days_box.grid(row=1,column=1,pady=10,padx=20,sticky="w")

name=Label(mangefrm,text="Name",font=("Times New Roman",15,"bold"),bg="light blue")
name.grid(row=2,column=0,pady=10,padx=20,sticky="w")
name_box=Entry(mangefrm,font=("Times New Roman",15,"bold"),bd=5,relief=GROOVE)
name_box.grid(row=2,column=1,pady=10,padx=20,sticky="w")

address=Label(mangefrm,text="Address",font=("Times New Roman",15,"bold"),bg="light blue")
address.grid(row=3,column=0,pady=10,padx=20,sticky="w")
address_box=Entry(mangefrm,font=("Times New Roman",15,"bold"),bd=5,relief=GROOVE)
address_box.grid(row=3,column=1,pady=10,padx=20,sticky="w")

contact=Label(mangefrm,text="Contact",font=("Times New Roman",15,"bold"),bg="light blue")
contact.grid(row=4,column=0,pady=10,padx=20,sticky="w")
contact_box=Entry(mangefrm,font=("Times New Roman",15,"bold"),bd=5,relief=GROOVE)
contact_box.grid(row=4,column=1,pady=10,padx=20,sticky="w")


email=Label(mangefrm,text="Email",font=("Times New Roman",15,"bold"),bg="light blue")
email.grid(row=5,column=0,pady=10,padx=20,sticky="w")
email_box=Entry(mangefrm,font=("Times New Roman",15,"bold"),bd=5,relief=GROOVE)
email_box.grid(row=5,column=1,pady=10,padx=20,sticky="w")

password=Label(mangefrm,text="Password",font=("Times New Roman",15,"bold"),bg="light blue")
password.grid(row=6,column=0,pady=10,padx=20,sticky="w")
password_box=Entry(mangefrm,font=("Times New Roman",15,"bold"),bd=5,relief=GROOVE,show='*')
password_box.grid(row=6,column=1,pady=10,padx=20,sticky="w")

btnfrm=Frame(mangefrm,bd=4,relief=RIDGE,bg="black")

btnfrm.place(x=40,y=600,width=320,height=50)

def fectdata():

    # nm = inm1.get()
    #
    # up = unitp1.get()
    #
    # qt = qty1.get()
    #
    # pac = unit2.get()

    db = mysql.connector.connect(host="localhost", user="root", password="", database="hospital")

    mycursor = db.cursor()

    mycursor.execute("select name,address,contact,email,password,available_days from doctor")

    rows=mycursor.fetchall()

    if len(rows)!=0:

        medtab.delete(*medtab.get_children())

    for row in rows:

       medtab.insert('',END,values=row)

    db.commit()

    db.close()

def cleardata():

    days_box.delete(0, 'end')

    name_box.delete(0, 'end')

    address_box.delete(0, 'end')

    contact_box.delete(0, 'end')

    email_box.delete(0 ,'end')

    password_box.delete(0, 'end')

    days_box.focus_set()

def getdata(event):

    currow=medtab.focus()

    contents=medtab.item(currow)

    row=contents['values']

    name_box.delete(0, END)

    address_box.delete(0, END)

    contact_box.delete(0, END)

    email_box.delete(0, END)

    password_box.delete(0, END)

    days_box.delete(0, END)

    name_box.insert(0,row[0])

    address_box.insert(0,row[1])

    contact_box.insert(0,row[2])

    email_box.insert(0,row[3])

    password_box.insert(0, row[4])

    days_box.insert(0, row[5])

def update():

    days = days_box.get()

    nm = name_box.get()

    ad = address_box.get()

    co = contact_box.get()

    em = email_box.get()

    pwd = password_box.get()

    db = mysql.connector.connect(host="localhost", user="root", password="", database="hospital")

    mycursor = db.cursor()

    try:

        sql = "update doctor set name=%s,address=%s,contact=%s,email=%s,password=%s,available_days=%s where name=%s"

        val = (nm, ad, co, em, pwd, days, nm)

        mycursor.execute(sql, val)

        db.commit()

        messagebox.showinfo("information", "Record Updated successfully")

        fectdata()

        cleardata()

    except EXCEPTION as e:

        print(e)

        db.rollback()

        db.close()

def delete1():

    em = email_box.get()

    db = mysql.connector.connect(host="localhost", user="root", password="", database="hospital")

    mycursor = db.cursor()

    try:

        sql = "delete from doctor where email=%s"

        val = (em,)

        mycursor.execute(sql, val)

        db.commit()

        messagebox.showinfo("information", "Record Deleted successfully")

        fectdata()

        cleardata()

    except EXCEPTION as e:

        print(e)

        db.rollback()

        db.close()

def fectdata1():

    ser1=comboser.get()

    lsearch1 = lsearch.get()

    db = mysql.connector.connect(host="localhost", user="root", password="", database="hospital")

    mycursor = db.cursor()

    mycursor.execute("select name,address,contact,email,password,available_days from doctor where "+str(ser1)+" LIKE '%"+str(lsearch1)+"%'")

    rows=mycursor.fetchall()

    if len(rows)!=0:

        medtab.delete(*medtab.get_children())

    for row in rows:

       medtab.insert('',END,values=row)

    db.commit()

    db.close()


updatebt=Button(btnfrm,command=update,text="UPDATE",width=10).grid(row=0,column=0,padx=10,pady=10)

detebt=Button(btnfrm,command=delete1,text="DELETE",width=10).grid(row=0,column=1,padx=10,pady=10)

clrt=Button(btnfrm,command=cleardata,text="CLEAR",width=10).grid(row=0,column=2,padx=10,pady=10)

detfrm=Frame(rt,bd=4,relief=RIDGE,bg="light blue")

detfrm.place(x=500,y=100,width=850,height=550)

lsearch=Label(detfrm,text="Search By",font=("Times New Roman",20,"bold"),bg="light blue")

lsearch.grid(row=0,column=0,pady=10,padx=20,sticky="w")

comboser=ttk.Combobox(detfrm,width=10,font=("Times New Roman",20,"bold"),state='readonly')

comboser['values']=("name")

comboser.grid(row=0,column=1,padx=20,pady=10)

lsearch=Entry(detfrm,font=("Times New Roman",15,"bold"),bd=5,relief=GROOVE)

lsearch.grid(row=0,column=2,pady=10,padx=20,sticky="w")

serbt=Button(detfrm,command=fectdata1,text="Search",font=("Times New Roman",10,"bold"),width=10,pady=5).grid(row=0,column=3,padx=10,pady=10)

showbt=Button(detfrm,command=fectdata,text="Show All",font=("Times New Roman",10,"bold"),width=10,pady=5).grid(row=0,column=4,padx=10,pady=10)

tabfrm=Frame(detfrm,bd=4,relief=RIDGE,bg="lightblue")

tabfrm.place(x=10,y=70,width=800,height=450)

scrollx=Scrollbar(tabfrm,orient=HORIZONTAL)

scrolly=Scrollbar(tabfrm,orient=VERTICAL)

medtab=ttk.Treeview(tabfrm,columns=("Name","Address","Contact","Email","Password","Availability"),xscrollcommand=scrollx.set,yscrollcommand=scrolly.set)

scrollx.pack(side=BOTTOM,fill=X)

scrolly.pack(side=RIGHT,fill=Y)

scrollx.config(command=medtab.xview)

scrolly.config(command=medtab.yview)

medtab.heading("Name",text="Name")

medtab.heading("Address",text="Address")

medtab.heading("Contact",text="Contact")

medtab.heading("Email",text="Email")

medtab.heading("Password",text="Password")

medtab.heading("Availability",text="Availability")

medtab['show']="headings"

medtab.column("Name",width=150)

medtab.column("Address",width=150)

medtab.column("Contact",width=150)

medtab.column("Email",width=150)

medtab.column("Password",width=150)

medtab.column("Availability",width=250)

medtab.pack(fill=BOTH,expand=1)

medtab.bind("<ButtonRelease-1>",getdata)

fectdata()

rt.mainloop()