from tkinter import*
import mysql.connector
from tkinter import ttk
from tkinter import ttk,messagebox
from tkcalendar import DateEntry
from PIL import Image,ImageTk

class DoctorDash:
    def __init__(self, window, email):
        self.connection = mysql.connector.connect(
            host='localhost',
            user='root',
            password='',
            db='hospital'
        )

        self.cursor = self.connection.cursor()
        self.email = email
        print(self.email)
        self.cursor.execute(f"SELECT name FROM doctor WHERE email='{self.email}'")
        self.doctor_name = self.cursor.fetchone()[0]
        print(self.doctor_name)
        self.connection.close()
        self.top = Tk()
        self.top.title("Doctor Dash")
        self.top.geometry("400x300")
        self.top.iconbitmap(r'medkit.ico')
        img = Image.open('home_bg.jpg')
        bg = ImageTk.PhotoImage(img)
        label = Label(self.top, image=bg)
        label.place(x=0, y=0, relwidth=1, relheight=1)
        btn1 = Button(self.top, text="Manage Patient", command=self.advise_medicine, width=17, bg='lightblue').grid(row=1, column=0, padx=150, pady=90)
        btn2 = Button(self.top, text="Patient History", command=self.manage_patient_history, width=17, bg='lightblue').grid(row=2,column=0,padx=150,pady=0)
        self.top.mainloop()

    def manage_patient_history(self):
        self.top.destroy()
        import patient_history
        patient_history.start_manage_patient_history(self.doctor_name)

    def advise_medicine(self):
        self.top.destroy()
        import advise_medicine
        advise_medicine.start_manage_appointment(self.doctor_name)


def start_doctor_dash(window, variable):
    doctor_dash = DoctorDash(window, variable)

