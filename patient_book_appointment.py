import tkinter as tk
from tkinter import ttk,messagebox
import mysql.connector

connection = mysql.connector.connect(
    host='localhost',
    user='root',
    password='',
    db='hospital'
)

cursor = connection.cursor()

window = tk.Tk()
window.title("Book Appointment")
screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()

window_width = 400
window_height = 400

x = (screen_width // 2) - (window_width // 2)
y = (screen_height // 2) - (window_height // 2)

window.geometry(f"{window_width}x{window_height}+{x}+{y}")

frame = ttk.Frame(window)
frame.pack(pady=20)

tk.Label(frame, text="Patient Name:").grid(row=0, column=0, sticky="e")
name_entry = tk.Entry(frame,width=23)
name_entry.grid(row=0, column=1)

tk.Label(frame, text="Doctor Specialty:").grid(row=1, column=0, sticky="e",pady=6)
specialty_entry = ttk.Combobox(frame)
specialty_entry.grid(row=1, column=1,pady=6)

tk.Label(frame, text="Doctor name:").grid(row=2, column=0, sticky="e",pady=6)
doctor_entry = ttk.Combobox(frame)
doctor_entry.grid(row=2, column=1,pady=6)

tk.Label(frame, text="Doctor Availability:").grid(row=3, column=0, sticky="e",pady=6)
day_entry = ttk.Combobox(frame)
day_entry.grid(row=3, column=1,pady=6)

tk.Label(frame, text="Time Slot:").grid(row=4, column=0, sticky="e", pady=6)
time_entry = ttk.Combobox(frame)
time_entry["values"]=("SELECT","10:00 am","10:30 am","11:00 am","11:30 am","12:00 pm","12:30 pm","2:00 pm","2:30 pm","3:00 pm","3:30 pm","4:00 pm","4:30 pm","5:00 pm","5:30 pm")
time_entry.grid(row=4, column=1, pady=6)

tk.Label(frame, text="Doctor Fees (in Rs.) :").grid(row=5, column=0, sticky="e",pady=6)
fees_entry = ttk.Entry(frame,state="disabled")
fees_entry.grid(row=5, column=1,pady=6)

def populate_specialties():
    cursor.execute("SELECT DISTINCT speciality FROM doctor")
    specialties = cursor.fetchall()
    specialties = [item[0] for item in specialties]
    specialty_entry['values'] = specialties

def populate_doctors(*args):
    specialty = specialty_entry.get()
    cursor.execute(f"SELECT name FROM doctor WHERE speciality='{specialty}'")
    doctors = cursor.fetchall()
    doctors = [item[0] for item in doctors]
    doctor_entry['values'] = doctors

specialty_entry.bind("<<ComboboxSelected>>", populate_doctors)

def populate_days(*args):
    doctor = doctor_entry.get()
    cursor.execute(f"SELECT available_days, fees FROM doctor WHERE name='{doctor}'")
    result = cursor.fetchone()
    available_days = result[0]
    fees = result[1]
    days = available_days.split(',')
    day_entry['values'] = days
    fees_entry.config(state='normal')
    fees_entry.delete(0, tk.END)
    fees_entry.insert(0, fees)
    fees_entry.config(state='disabled')

doctor_entry.bind("<<ComboboxSelected>>", populate_days)

def book_appointment():
    name = name_entry.get()
    doctor = doctor_entry.get()
    day = day_entry.get()
    time_data=time_entry.get()

    if name=="" or doctor=="" or day=="" or time_data=="":
        messagebox.showerror("Error", "Please polulate relevant details")

    else:
        cursor.execute(f"SELECT slots FROM doctor WHERE name='{doctor}'")
        slots = cursor.fetchone()[0]

        cursor.execute(f"SELECT COUNT(*) FROM appointments WHERE doctor='{doctor}' AND day='{day}'")
        appointment_count = cursor.fetchone()[0]

        if appointment_count >= slots:
            tk.messagebox.showerror("Error", "All slots for this doctor on the given day are booked.")
            return

        cursor.execute(f"INSERT INTO appointments (name, doctor, day, time, status) VALUES ('{name}', '{doctor}', '{day}', '{time_data}', 'Upcoming')")
        connection.commit()

        cursor.execute(f"UPDATE doctor SET slots = slots - 1 WHERE name='{doctor}'")
        connection.commit()

        tk.messagebox.showinfo("Success", "Appointment booked successfully.")

        window.destroy()
        import patient_dash

book_button = tk.Button(window, text="Book Appointment", command=book_appointment)
book_button.pack()

populate_specialties()

window.mainloop()

connection.close()
