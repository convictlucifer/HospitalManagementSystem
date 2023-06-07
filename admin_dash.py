from tkinter import*
import mysql.connector
from tkinter import ttk
from tkinter import ttk,messagebox
from tkcalendar import DateEntry
from PIL import Image,ImageTk

def update_med():
    top.destroy()
    import update_medicine

def update_doctor():
    top.destroy()
    import update_doctor

def update_user():
    top.destroy()
    import update_user

def reset_slots():
    db = mysql.connector.connect(host="localhost", user="root", password="", database="hospital")
    mycursor = db.cursor()
    try:
        sql = "update doctor set slots=50"
        mycursor.execute(sql)
        db.commit()
        messagebox.showinfo("information", "Doctor slots resetted successfully")

    except EXCEPTION as e:
        print(e)
        db.rollback()
        db.close()

top=Tk()
top.title("Admin Dash")
top.geometry("400x300")
top.iconbitmap(r'medkit.ico')
img =Image.open('home_bg.jpg')
bg = ImageTk.PhotoImage(img)
label = Label(top, image=bg)
label.place(x =0,y = 0,relwidth=1,relheight=1)
btn1=Button(top,text="Update Patient",command=update_user,width=12,bg='lightblue').grid(row=1,column=0,padx=150,pady=40)
btn2=Button(top,text="Update Doctor",command=update_doctor,width=12,bg='lightblue').grid(row=2,column=0,padx=150,pady=0)
btn3=Button(top,text="Update Medicine",command=update_med,width=12,bg='lightblue').grid(row=3,column=0,padx=150,pady=40)
btn4=Button(top,text="Reset Slots",command=reset_slots,width=12,bg='lightblue').grid(row=4,column=0,padx=150,pady=0)
top.mainloop()