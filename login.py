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


import tkinter as tk
from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk
import sqlite3
import os

# ================= Root Window =================
login_win = tk.Tk()
login_win.title("User Login")

w, h = login_win.winfo_screenwidth(), login_win.winfo_screenheight()
login_win.geometry(f"{w}x{h}+0+0")

# ================= Background Image =================
bg = Image.open("4.png")
bg = bg.resize((w, h), Image.LANCZOS)
bg_img = ImageTk.PhotoImage(bg)

bg_label = Label(login_win, image=bg_img)
bg_label.place(x=0, y=0, relwidth=1, relheight=1)

label = Label(login_win, text="Military Face Authentication & Vehicle Detection",
              font=('Arial', 30), bg="black", fg="white", width=70, height=1)
label.place(x=0, y=0)

# ================= Database =================
conn = sqlite3.connect("users.db")
cursor = conn.cursor()

# ================= OPEN NEXT PAGE =================
def open_gui_master():
    login_win.destroy()
    os.system("python GUI_Master.py")

# ================= Login Function =================
def login_user():
    username = entry_username.get()
    password = entry_password.get()

    if not username or not password:
        messagebox.showerror("Error", "All fields required")
        return

    cursor.execute("SELECT * FROM users WHERE username=? AND password=?", (username, password))
    row = cursor.fetchone()

    if row:
        messagebox.showinfo("Success", "Login Successful ✅")
        open_gui_master()
    else:
        messagebox.showerror("Error", "Invalid username or password")

# ================= UI =================
frame = Frame(login_win, bg="gray20", bd=10, relief="ridge")
frame.place(relx=0.5, rely=0.55, anchor="center", width=500, height=300)

Label(frame, text="LOGIN", font=("Arial",22,"bold"), bg="gray20", fg="white").grid(row=0,column=0,columnspan=2,pady=20)
Label(frame, text="Username:", font=("Arial",14), bg="gray20", fg="white").grid(row=1,column=0,padx=15,pady=10)
entry_username = Entry(frame, font=("Arial",14), width=25)
entry_username.grid(row=1,column=1)

Label(frame, text="Password:", font=("Arial",14), bg="gray20", fg="white").grid(row=2,column=0,padx=15,pady=10)
entry_password = Entry(frame, show="*", font=("Arial",14), width=25)
entry_password.grid(row=2,column=1)

Button(frame,text="Login", font=("Arial",14,"bold"), bg="#228B22", fg="white", width=15, command=login_user).grid(row=3,column=0,pady=25)
Button(frame,text="Exit", font=("Arial",14,"bold"), bg="#B22222", fg="white", width=15, command=login_win.destroy).grid(row=3,column=1,pady=25)

login_win.mainloop()
