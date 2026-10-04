# ============================================================
# COPYRIGHT (c) 2026 SUMIT RAJ (MT24AAI011)
# VNIT NAGPUR - ALL RIGHTS RESERVED
# 
# This code is for academic evaluation only.
# Unauthorized copying, modification, or distribution
# is strictly prohibited.
# 
# Project: Military Vehicle Detection and Face Authentication
# Author: Sumit Raj
# Guide: Prof. Meera Dhabu
# Date: May 2026
# ============================================================


from tkinter import *
import sqlite3
import tkinter as tk
from tkinter import messagebox as ms
from PIL import Image, ImageTk

root = Tk()
root.geometry('700x600')
root.title("Registration Form")

image2 = Image.open('6.jpg')
image2 = image2.resize((1530, 800), Image.LANCZOS)

background_image = ImageTk.PhotoImage(image2)

background_label = tk.Label(root, image=background_image)
background_label.image = background_image
background_label.place(x=0, y=0)

Name = StringVar()
LastName = StringVar()
Address = StringVar()
states1 = StringVar()
Mobile = StringVar()


# ================= FIXED DATABASE FUNCTION =================
def database():

    name = Name.get()
    lastname = LastName.get()
    address = Address.get()
    states = states1.get()
    mobileno = Mobile.get()

    conn = sqlite3.connect('face.db')
    cursor = conn.cursor()

    # 🔥 FIX 1: Ensure correct table structure (safe migration)
    cursor.execute('''CREATE TABLE IF NOT EXISTS User (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        Name TEXT,
        Lastname TEXT,
        Address TEXT,
        States TEXT,
        Mobileno TEXT
    )''')

    # 🔥 FIX 2: Auto-add missing column (important fix)
    try:
        cursor.execute("ALTER TABLE User ADD COLUMN States TEXT")
    except:
        pass

    try:
        cursor.execute("ALTER TABLE User ADD COLUMN Address TEXT")
    except:
        pass

    try:
        cursor.execute("ALTER TABLE User ADD COLUMN Mobileno TEXT")
    except:
        pass

    # ================= VALIDATION =================
    if (name.isdigit() or name == ""):
        ms.showinfo("Message", "please enter valid name")

    elif (lastname.isdigit() or lastname == ""):
        ms.showinfo("Message", "please enter valid lastname")

    elif (address == ""):
        ms.showinfo("Message", "Please Enter valid Address")

    elif (states == ""):
        ms.showinfo("Message", "Please Enter valid States")

    elif (len(str(mobileno)) != 10):
        ms.showinfo("Message", "Please Enter 10 digit mobile number")

    else:
        try:
            cursor.execute('''
                INSERT INTO User (Name, Lastname, Address, States, Mobileno)
                VALUES (?, ?, ?, ?, ?)
            ''', (name, lastname, address, states, mobileno))

            conn.commit()

            ms.showinfo('Success', 'User Registered Successfully.........')
            root.destroy()

        except Exception as e:
            ms.showerror("Database Error", str(e))

        finally:
            conn.close()


def display():
    from subprocess import call
    call(["python", "display.py"])


# ================= UI (UNCHANGED) =================
label_0 = Label(root, text="Registration Form", width=25,
                font=("bold", 22), fg="orange", bg="black")
label_0.place(x=1000, y=50)

label_1 = Label(root, text="Name", width=20,
                font=("bold", 15), bg='black', fg='white')
label_1.place(x=1000, y=130)

entry_1 = Entry(root, textvar=Name, width=25, font=("bold", 10))
entry_1.place(x=1250, y=130)

label_2 = Label(root, text="Last Name", width=20,
                font=("bold", 15), bg='black', fg='white')
label_2.place(x=1000, y=180)

entry_2 = Entry(root, textvar=LastName, width=25, font=("bold", 10))
entry_2.place(x=1250, y=180)

label_3 = Label(root, text="Address", width=20,
                font=("bold", 15), bg='black', fg='white')
label_3.place(x=1000, y=230)

entry_3 = Entry(root, textvar=Address, width=25, font=("bold", 10))
entry_3.place(x=1250, y=230)

label_4 = Label(root, text="States", width=20,
                font=("bold", 15), bg='black', fg='white')
label_4.place(x=1000, y=280)

entry_4 = Entry(root, textvar=states1, width=25, font=("bold", 10))
entry_4.place(x=1250, y=280)

label_5 = Label(root, text="Mobile No", width=20,
                font=("bold", 15), bg='black', fg='white')
label_5.place(x=1000, y=330)

entry_5 = Entry(root, textvar=Mobile, width=25, font=("bold", 10))
entry_5.place(x=1250, y=330)

Button(root, text='Submit', width=25,
       bg='red', fg='white', command=database).place(x=1000, y=380)

Button(root, text='Display', width=25,
       bg='red', fg='white', command=display).place(x=1250, y=380)

root.mainloop()