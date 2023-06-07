from tkinter import*

import mysql.connector

from tkinter import ttk

from tkinter import ttk,messagebox

from PIL import Image,ImageTk #pip install Pillow

rt=Tk()

rt.title("Update Medicine")

rt.geometry("1600x900+0+0")

title=Label(rt,text="Welcome to ABC Hospital",bd=10,relief=GROOVE,font=("Monotype Corsiva",35,"bold"),fg="darkgreen",bg="red")

title.pack(side=TOP,fill=X)

mangefrm=Frame(rt,bd=4,relief=RIDGE,bg="light blue")

mangefrm.place(x=20,y=100,width=450,height=550)

mtitle=Label(mangefrm,text="Manage Medicine",font=("Times New Roman",20,"bold"),fg="darkgreen",bg="light blue")

mtitle.grid(row=0,columnspan=2,pady=20)

icd=Label(mangefrm,text="Item Code",font=("Times New Roman",15,"bold"),bg="light blue")

icd.grid(row=1,column=0,pady=10,padx=20,sticky="w")

icd1=Entry(mangefrm,font=("Times New Roman",15,"bold"),bd=5,relief=GROOVE)

icd1.grid(row=1,column=1,pady=10,padx=20,sticky="w")

inm=Label(mangefrm,text="Item Name",font=("Times New Roman",15,"bold"),bg="light blue")

inm.grid(row=2,column=0,pady=10,padx=20,sticky="w")

inm1=Entry(mangefrm,font=("Times New Roman",15,"bold"),bd=5,relief=GROOVE)

inm1.grid(row=2,column=1,pady=10,padx=20,sticky="w")

unitp=Label(mangefrm,text="Unit Price",font=("Times New Roman",15,"bold"),bg="light blue")

unitp.grid(row=3,column=0,pady=10,padx=20,sticky="w")

unitp1=Entry(mangefrm,font=("Times New Roman",15,"bold"),bd=5,relief=GROOVE)

unitp1.grid(row=3,column=1,pady=10,padx=20,sticky="w")

qty=Label(mangefrm,text="Quantity",font=("Times New Roman",15,"bold"),bg="light blue")

qty.grid(row=4,column=0,pady=10,padx=20,sticky="w")

qty1=Entry(mangefrm,font=("Times New Roman",15,"bold"),bd=5,relief=GROOVE)

qty1.grid(row=4,column=1,pady=10,padx=20,sticky="w")

unit1=Label(mangefrm,text="Units",font=("Times New Roman",15,"bold"),bg="light blue")

unit1.grid(row=5,column=0,pady=10,padx=20,sticky="w")

unit2=Entry(mangefrm,font=("Times New Roman",15,"bold"),bd=5,relief=GROOVE)

unit2.grid(row=5,column=1,pady=10,padx=20,sticky="w")

btnfrm=Frame(mangefrm,bd=4,relief=RIDGE,bg="black")

btnfrm.place(x=10,y=400,width=400,height=50)

def add():

    if icd1.get()=="" or inm1.get()=="" or unitp1.get()=="" or qty1.get()=="" or unit2.get()=="":

       messagebox.showerror("Error","All fields are required")

    else:

     ic=icd1.get()

     nm=inm1.get()

     up=unitp1.get()

     qt=qty1.get()

     pac=unit2.get()

     db=mysql.connector.connect(host="localhost",user="root",password="",database="hospital")

     mycursor=db.cursor()

     try:

        sql="insert into medicine(itemcode,name,unitpr,quantity,unit)values(%s,%s,%s,%s,%s)"

        val=(ic,nm,up,qt,pac)

        mycursor.execute(sql,val)

        db.commit()

        messagebox.showinfo("information","Record Inserted successfully")

        fectdata()

        cleardata()

     except EXCEPTION as e:

        print(e)

        db.rollback()

        db.close()

def fectdata():

    ic = icd1.get()

    nm = inm1.get()

    up = unitp1.get()

    qt = qty1.get()

    pac = unit2.get()

    db = mysql.connector.connect(host="localhost", user="root", password="", database="hospital")

    mycursor = db.cursor()

    mycursor.execute("select * from medicine")

    rows=mycursor.fetchall()

    if len(rows)!=0:

        medtab.delete(*medtab.get_children())

    for row in rows:

       medtab.insert('',END,values=row)

    db.commit()

    db.close()

def cleardata():

    icd1.delete(0, 'end')

    inm1.delete(0, 'end')

    unitp1.delete(0, 'end')

    qty1.delete(0, 'end')

    unit2.delete(0 ,'end')

    icd1.focus_set()

def getdata(event):

    currow=medtab.focus()

    contents=medtab.item(currow)

    row=contents['values']

    icd1.delete(0, END)

    inm1.delete(0, END)

    unitp1.delete(0, END)

    qty1.delete(0, END)

    unit2.delete(0, END)

    icd1.insert(0,row[0])

    inm1.insert(0,row[1])

    unitp1.insert(0,row[2])

    qty1.insert(0,row[3])

    unit2.insert(0,row[4])

def update():

    ic = icd1.get()

    nm = inm1.get()

    up = unitp1.get()

    qt = qty1.get()

    pac = unit2.get()

    db = mysql.connector.connect(host="localhost", user="root", password="", database="hospital")

    mycursor = db.cursor()

    try:

        sql = "update medicine set name=%s,unitpr=%s,quantity=%s,unit=%s where itemcode=%s"

        val = (nm, up, qt, pac, ic)

        mycursor.execute(sql, val)

        db.commit()

        messagebox.showinfo("information", "Record Updated successfully")

        icd1.delete(0, END)

        inm1.delete(0, END)

        unitp1.delete(0, END)

        qty1.delete(0, END)

        unit2.delete(0, END)

        fectdata()

        cleardata()

    except EXCEPTION as e:

        print(e)

        db.rollback()

        db.close()

def delete1():

    ic = icd1.get()

    db = mysql.connector.connect(host="localhost", user="root", password="", database="hospital")

    mycursor = db.cursor()

    try:

        sql = "delete from medicine where itemcode=%s"

        val = (ic,)

        mycursor.execute(sql, val)

        db.commit()

        messagebox.showinfo("information", "Record Deleted successfully")

        icd1.delete(0, END)

        inm1.delete(0, END)

        unitp1.delete(0, END)

        qty1.delete(0, END)

        unit2.delete(0, END)

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

    mycursor.execute("select * from medicine where "+str(ser1)+" LIKE '%"+str(lsearch1)+"%'")

    rows=mycursor.fetchall()

    if len(rows)!=0:

        medtab.delete(*medtab.get_children())

    for row in rows:

       medtab.insert('',END,values=row)

    db.commit()

    db.close()



addbt=Button(btnfrm,text="ADD",command=add,width=10).grid(row=0,column=0,padx=10,pady=10)

updatebt=Button(btnfrm,text="UPDATE",command=update,width=10).grid(row=0,column=1,padx=10,pady=10)

detebt=Button(btnfrm,text="DELETE",command=delete1,width=10).grid(row=0,column=2,padx=10,pady=10)

clrt=Button(btnfrm,text="CLEAR",command=cleardata,width=10).grid(row=0,column=3,padx=10,pady=10)

detfrm=Frame(rt,bd=4,relief=RIDGE,bg="light blue")

detfrm.place(x=500,y=100,width=850,height=550)

lsearch=Label(detfrm,text="Search By",font=("Times New Roman",20,"bold"),bg="light blue")

lsearch.grid(row=0,column=0,pady=10,padx=20,sticky="w")

comboser=ttk.Combobox(detfrm,width=10,font=("Times New Roman",20,"bold"),state='readonly')

comboser['values']=("itemcode","name")

comboser.grid(row=0,column=1,padx=20,pady=10)

lsearch=Entry(detfrm,font=("Times New Roman",15,"bold"),bd=5,relief=GROOVE)

lsearch.grid(row=0,column=2,pady=10,padx=20,sticky="w")

serbt=Button(detfrm,text="Search",command=fectdata1,font=("Times New Roman",10,"bold"),width=10,pady=5).grid(row=0,column=3,padx=10,pady=10)

showbt=Button(detfrm,text="Show All",command=fectdata,font=("Times New Roman",10,"bold"),width=10,pady=5).grid(row=0,column=4,padx=10,pady=10)

tabfrm=Frame(detfrm,bd=4,relief=RIDGE,bg="lightblue")

tabfrm.place(x=10,y=70,width=800,height=450)

scrollx=Scrollbar(tabfrm,orient=HORIZONTAL)

scrolly=Scrollbar(tabfrm,orient=VERTICAL)

medtab=ttk.Treeview(tabfrm,columns=("icode","name","up1","qyty","units"),xscrollcommand=scrollx.set,yscrollcommand=scrolly.set)

scrollx.pack(side=BOTTOM,fill=X)

scrolly.pack(side=RIGHT,fill=Y)

scrollx.config(command=medtab.xview)

scrolly.config(command=medtab.yview)

medtab.heading("icode",text="Item Code")

medtab.heading("name",text="Name")

medtab.heading("up1",text="Unit Price")

medtab.heading("qyty",text="Quantity")

medtab.heading("units",text="Units")

medtab['show']="headings"

medtab.column("icode",width=100)

medtab.column("name",width=100)

medtab.column("up1",width=100)

medtab.column("qyty",width=100)

medtab.column("units",width=100)

medtab.pack(fill=BOTH,expand=1)

medtab.bind("<ButtonRelease-1>",getdata)

fectdata()

rt.mainloop()