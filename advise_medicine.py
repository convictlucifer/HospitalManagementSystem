import tkinter as tk
from tkinter import ttk
from tkinter import *
import mysql.connector
from tkinter import messagebox

class ManagePatient:
    def __init__(self, doctor_name):
        self.connection = mysql.connector.connect(
            host='localhost',
            user='root',
            password='',
            db='hospital'
        )
        self.cursor = self.connection.cursor()
        self.doctor_name = doctor_name

        self.window = tk.Tk()
        self.window.title("Manage Patient")
        screen_width = self.window.winfo_screenwidth()
        screen_height = self.window.winfo_screenheight()

        window_width = 800
        window_height = 350

        x = (screen_width // 2) - (window_width // 2)
        y = (screen_height // 2) - (window_height // 2)

        self.window.geometry(f"{window_width}x{window_height}+{x}+{y}")

        scrollx = Scrollbar(self.window, orient=HORIZONTAL)
        scrolly = Scrollbar(self.window, orient=VERTICAL)
        self.patient_treeview = ttk.Treeview(
            self.window, columns=("Name"), show="headings", xscrollcommand=scrollx.set, yscrollcommand=scrolly.set
        )
        scrollx.pack(side=BOTTOM, fill=X)
        scrolly.pack(side=RIGHT, fill=Y)
        scrollx.config(command=self.patient_treeview.xview)
        scrolly.config(command=self.patient_treeview.yview)
        self.patient_treeview.heading("#0", text="")
        self.patient_treeview.heading("Name", text="Patient Name")
        self.patient_treeview.pack(pady=10)

        manage_button = tk.Button(
            self.window, text="Manage", command=self.manage_patient
        )
        manage_button.pack(pady=10)

        self.populate_patients()

        self.window.mainloop()

        self.connection.close()

    def populate_patients(self):
        self.cursor.execute(
            f"SELECT name FROM appointments WHERE doctor='{self.doctor_name}' and status='Upcoming'"
        )
        patients = self.cursor.fetchall()
        self.patient_treeview.delete(*self.patient_treeview.get_children())
        for patient in patients:
            self.patient_treeview.insert("", "end", values=patient)

    def manage_patient(self):
        selected_item = self.patient_treeview.selection()
        if not selected_item:
            messagebox.showwarning("Warning", "Please select a patient.")
            return

        patient_name = self.patient_treeview.item(selected_item)["values"][0]

        self.window.destroy()
        ManageAppointment(patient_name, self.doctor_name)


class ManageAppointment:
    def __init__(self, patient_name, doctor_name):
        self.connection = mysql.connector.connect(
            host='localhost',
            user='root',
            password='',
            db='hospital'
        )
        self.cursor = self.connection.cursor()
        self.patient_name = patient_name
        self.doctor_name = doctor_name

        self.window = tk.Tk()
        self.window.title("Manage Appointment")
        screen_width = self.window.winfo_screenwidth()
        screen_height = self.window.winfo_screenheight()

        window_width = 300
        window_height = 200

        x = (screen_width // 2) - (window_width // 2)
        y = (screen_height // 2) - (window_height // 2)

        self.window.geometry(f"{window_width}x{window_height}+{x}+{y}")

        tk.Label(self.window, text="Patient Name:").grid(row=0, column=0, sticky="e")
        tk.Label(self.window, text=patient_name).grid(row=0, column=1)

        tk.Label(self.window, text="Disease:").grid(row=1, column=0, sticky="e", pady=6)
        self.disease_entry = tk.Entry(self.window)
        self.disease_entry.grid(row=1, column=1, pady=6)

        tk.Label(self.window, text="Medicines:").grid(row=2, column=0, sticky="e", pady=6)
        self.medicines_entry = tk.Entry(self.window)
        self.medicines_entry.grid(row=2, column=1, pady=6)

        save_button = tk.Button(self.window, text="Save", command=self.save_appointment)
        save_button.grid(row=3, columnspan=2, pady=10)

        self.window.mainloop()

        self.connection.close()

    def save_appointment(self):
        disease = self.disease_entry.get()
        medicines = self.medicines_entry.get()

        if disease == "" or medicines == "":
            messagebox.showerror("Error", "Please enter disease and medicines.")
        else:
            self.cursor.execute(
                f"INSERT INTO patient_history (patient_name, doctor_name, disease, medicines_advised) VALUES ('{self.patient_name}', '{self.doctor_name}', '{disease}', '{medicines}')"
            )
            self.connection.commit()

            self.update_appointment_status(self.patient_name)

            self.window.destroy()
            import login

    def update_appointment_status(self, patient_name):
        self.cursor.execute(
            f"UPDATE appointments SET status='Completed' WHERE name='{patient_name}'"
        )
        self.connection.commit()

        messagebox.showinfo(
            "Success", "Diagnosis Completed for patient"
        )


def start_manage_appointment(doctor_name):
    doctor_name = doctor_name
    ManagePatient(doctor_name)
