from tkinter import*
import mysql.connector
from tkinter import ttk
from tkcalendar import DateEntry
from tkinter import ttk,messagebox
from PIL import Image,ImageTk

class Patient_history:
    def __init__(self, doctor_name):
        self.rt=Tk()

        self.doctor_name=doctor_name

        self.rt.title("Patient History")

        self.rt.geometry("1600x900+0+0")

        title=Label(self.rt,text="Welcome to ABC Hospital",bd=10,relief=GROOVE,font=("Monotype Corsiva",35,"bold"),fg="darkgreen",bg="red")

        title.pack(side=TOP,fill=X)

        mangefrm=Frame(self.rt,bd=4,relief=RIDGE,bg="light blue")

        mangefrm.place(x=20,y=100,width=450,height=680)

        mtitle=Label(mangefrm,text="Manage Patient History",font=("Times New Roman",20,"bold"),fg="darkgreen",bg="light blue")

        mtitle.grid(row=0,columnspan=2,pady=20)

        id=Label(mangefrm,text="ID",font=("Times New Roman",15,"bold"),bg="light blue")
        id.grid(row=1,column=0,pady=10,padx=20,sticky="w")
        self.id_box=Entry(mangefrm,font=("Times New Roman",15,"bold"),bd=5,relief=GROOVE)
        self.id_box.grid(row=1,column=1,pady=10,padx=20,sticky="w")

        pname=Label(mangefrm,text="Patient Name",font=("Times New Roman",15,"bold"),bg="light blue")
        pname.grid(row=2,column=0,pady=10,padx=20,sticky="w")
        self.pname_box=Entry(mangefrm,font=("Times New Roman",15,"bold"),bd=5,relief=GROOVE)
        self.pname_box.grid(row=2,column=1,pady=10,padx=20,sticky="w")

        docname=Label(mangefrm,text="Doctor Name",font=("Times New Roman",15,"bold"),bg="light blue")
        docname.grid(row=3,column=0,pady=10,padx=20,sticky="w")
        self.docname_box=Entry(mangefrm,font=("Times New Roman",15,"bold"),bd=5,relief=GROOVE)
        self.docname_box.grid(row=3,column=1,pady=10,padx=20,sticky="w")


        disease=Label(mangefrm,text="Disease Caused",font=("Times New Roman",15,"bold"),bg="light blue")
        disease.grid(row=4,column=0,pady=10,padx=20,sticky="w")
        self.disease_box=Entry(mangefrm,font=("Times New Roman",15,"bold"),bd=5,relief=GROOVE)
        self.disease_box.grid(row=4,column=1,pady=10,padx=20,sticky="w")

        medicine=Label(mangefrm,text="Medicines Advised",font=("Times New Roman",15,"bold"),bg="light blue")
        medicine.grid(row=5,column=0,pady=10,padx=20,sticky="w")
        self.medicine_box=Entry(mangefrm,font=("Times New Roman",15,"bold"),bd=5,relief=GROOVE)
        self.medicine_box.grid(row=5,column=1,pady=10,padx=20,sticky="w")

        btnfrm=Frame(mangefrm,bd=4,relief=RIDGE,bg="black")

        btnfrm.place(x=90,y=600,width=220,height=50)

        updatebt = Button(btnfrm, command=self.update, text="UPDATE", width=10).grid(row=0, column=0, padx=10, pady=10)

        clrt = Button(btnfrm, command=self.cleardata, text="CLEAR", width=10).grid(row=0, column=2, padx=10, pady=10)

        detfrm = Frame(self.rt, bd=4, relief=RIDGE, bg="light blue")

        detfrm.place(x=500, y=100, width=850, height=550)

        self.lsearch = Label(detfrm, text="Search By", font=("Times New Roman", 20, "bold"), bg="light blue")

        self.lsearch.grid(row=0, column=0, pady=10, padx=20, sticky="w")

        self.comboser = ttk.Combobox(detfrm, width=10, font=("Times New Roman", 20, "bold"), state='readonly')

        self.comboser['values'] = ("patient_name")

        self.comboser.grid(row=0, column=1, padx=20, pady=10)

        self.lsearch = Entry(detfrm, font=("Times New Roman", 15, "bold"), bd=5, relief=GROOVE)

        self.lsearch.grid(row=0, column=2, pady=10, padx=20, sticky="w")

        serbt = Button(detfrm, command=self.fectdata1, text="Search", font=("Times New Roman", 10, "bold"), width=10,pady=5).grid(row=0, column=3, padx=10, pady=10)

        showbt = Button(detfrm, command=self.fectdata, text="Show All", font=("Times New Roman", 10, "bold"), width=10,pady=5).grid(row=0, column=4, padx=10, pady=10)

        tabfrm = Frame(detfrm, bd=4, relief=RIDGE, bg="lightblue")

        tabfrm.place(x=10, y=70, width=800, height=450)

        scrollx = Scrollbar(tabfrm, orient=HORIZONTAL)

        scrolly = Scrollbar(tabfrm, orient=VERTICAL)

        self.medtab = ttk.Treeview(tabfrm, columns=("id", "pname", "docname", "disease", "medicine"),xscrollcommand=scrollx.set, yscrollcommand=scrolly.set)

        scrollx.pack(side=BOTTOM, fill=X)

        scrolly.pack(side=RIGHT, fill=Y)

        scrollx.config(command=self.medtab.xview)

        scrolly.config(command=self.medtab.yview)

        self.medtab.heading("id", text="ID")

        self. medtab.heading("pname", text="Patient_name")

        self.medtab.heading("docname", text="Doctor_name")

        self.medtab.heading("disease", text="Disease_caused")

        self.medtab.heading("medicine", text="Medicines_advised")

        self.medtab['show'] = "headings"

        self.medtab.column("id", width=150)

        self.medtab.column("pname", width=150)

        self.medtab.column("docname", width=150)

        self.medtab.column("disease", width=150)

        self.medtab.column("medicine", width=150)

        self.medtab.pack(fill=BOTH, expand=1)

        self.medtab.bind("<ButtonRelease-1>", self.getdata)

        self.fectdata()

        self.rt.mainloop()

    def fectdata(self):

        db = mysql.connector.connect(host="localhost", user="root", password="", database="hospital")

        mycursor = db.cursor()

        mycursor.execute(f"select * from patient_history where doctor_name='{self.doctor_name}'")

        rows=mycursor.fetchall()

        if len(rows)!=0:

            self.medtab.delete(*self.medtab.get_children())

        for row in rows:

           self.medtab.insert('',END,values=row)

        db.commit()

        db.close()

    def cleardata(self):

        self.id_box.delete(0, 'end')

        self.pname_box.delete(0, 'end')

        self.docname_box.delete(0, 'end')

        self.disease_box.delete(0 ,'end')

        self.medicine_box.delete(0, 'end')

        self.id_box.focus_set()

    def getdata(self,event):

        currow=self.medtab.focus()

        contents=self.medtab.item(currow)

        row=contents['values']

        self.id_box.delete(0, END)

        self.pname_box.delete(0, END)

        self.docname_box.delete(0, END)

        self.disease_box.delete(0, END)

        self.medicine_box.delete(0, END)

        self.id_box.insert(0,row[0])

        self.pname_box.insert(0,row[1])

        self.docname_box.insert(0,row[2])

        self.disease_box.insert(0,row[3])

        self.medicine_box.insert(0, row[4])


    def update(self):

        nm = self.id_box.get()

        ad = self.pname_box.get()

        co = self.docname_box.get()

        em = self.disease_box.get()

        pwd = self.medicine_box.get()

        db = mysql.connector.connect(host="localhost", user="root", password="", database="hospital")

        mycursor = db.cursor()

        try:

            sql = "update patient_history set patient_name=%s,doctor_name=%s,disease=%s,medicines_advised=%s where id=%s"

            val = (ad, co, em, pwd, nm)

            mycursor.execute(sql, val)

            db.commit()

            messagebox.showinfo("information", "Record Updated successfully")

            self.fectdata()

            self.cleardata()

            self.rt.destroy()

            import login

        except EXCEPTION as e:

            print(e)

            db.rollback()

            db.close()

    def fectdata1(self):

        ser1=self.comboser.get()

        lsearch1 = self.lsearch.get()

        db = mysql.connector.connect(host="localhost", user="root", password="", database="hospital")

        mycursor = db.cursor()

        mycursor.execute("select * from patient_history where "+str(ser1)+" LIKE '%"+str(lsearch1)+"%'")

        rows=mycursor.fetchall()

        if len(rows)!=0:

            self.medtab.delete(*self.medtab.get_children())

        for row in rows:

           self.medtab.insert('',END,values=row)

        db.commit()

        db.close()

def start_manage_patient_history(doctor_name):
    doctor_name = doctor_name
    Patient_history(doctor_name)


