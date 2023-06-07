import tkinter as tk
from tkinter import *
from tkinter import ttk
import mysql.connector
from tkinter import messagebox

connection = mysql.connector.connect(
    host='localhost',
    user='root',
    password='',
    db='hospital'
)

cursor = connection.cursor()

window = tk.Tk()
window.title("Manage Appointments")
screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()

window_width = 1000
window_height = 800

x = (screen_width // 2) - (window_width // 2)
y = (screen_height // 2) - (window_height // 2)

window.geometry(f"{window_width}x{window_height}+{x}+{y}")


def populate_appointments():
    if name_entry.get() == "":
        messagebox.showerror("Error", "Please enter patient name")
    else:
        cursor.execute(f"SELECT doctor, day, time, status FROM appointments WHERE name='{name_entry.get()}'")
        appointments = cursor.fetchall()
        appointments_treeview.delete(*appointments_treeview.get_children())
        for appointment in appointments:
            appointments_treeview.insert("", "end", values=appointment)


def cancel_appointment():
    selected_item = appointments_treeview.selection()
    if not selected_item:
        messagebox.showwarning("Warning", "Please select an appointment to cancel.")
        return

    appointment_item = appointments_treeview.item(selected_item)
    appointment_status = appointment_item['values'][3]

    if appointment_status == 'Upcoming':
        appointment_id = name_entry.get()
        cursor.execute(f"SELECT doctor FROM appointments WHERE name='{name_entry.get()}'")
        doctor_name = cursor.fetchone()[0]
        cursor.execute(f"DELETE FROM appointments WHERE name='{appointment_id}'")
        connection.commit()
        cursor.execute(f"UPDATE doctor SET slots = slots + 1 WHERE name='{doctor_name}'")
        connection.commit()
        messagebox.showinfo("Success", "Appointment canceled successfully.")
        # populate_appointments()
        window.destroy()
        import patient_dash

    else:
        messagebox.showwarning("Warning", "Cannot cancel an completed appointment.")
        return


tk.Label(window, text="Patient Name:").pack()
name_entry = tk.Entry(window)
name_entry.pack()

populate_button = tk.Button(window, text="Show Appointments", command=populate_appointments)
populate_button.pack(pady=10)

scrollx = Scrollbar(window, orient=HORIZONTAL)
scrolly = Scrollbar(window, orient=VERTICAL)
appointments_treeview = ttk.Treeview(
    window,
    columns=("Doctor", "Day", "Time", "Status"),
    xscrollcommand=scrollx.set,
    yscrollcommand=scrolly.set,
    show="headings"
)
scrollx.pack(side=BOTTOM, fill=X)
scrolly.pack(side=RIGHT, fill=Y)
scrollx.config(command=appointments_treeview.xview)
scrolly.config(command=appointments_treeview.yview)
appointments_treeview.heading("#0", text="")
appointments_treeview.heading("Doctor", text="Doctor")
appointments_treeview.heading("Day", text="Appointment_Day")
appointments_treeview.heading("Time", text="Appointment_Time")
appointments_treeview.heading("Status", text="Status")

appointments_treeview.pack(pady=10)

cancel_button = tk.Button(window, text="Cancel Appointment", command=cancel_appointment)
cancel_button.pack()

window.mainloop()

connection.close()
