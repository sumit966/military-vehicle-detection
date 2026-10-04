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
reg_win = tk.Tk()
reg_win.title("User Registration")

w, h = reg_win.winfo_screenwidth(), reg_win.winfo_screenheight()
reg_win.geometry(f"{w}x{h}+0+0")
reg_win.configure(bg="black")

# ================= Background Image =================
bg = Image.open("2.png")
bg = bg.resize((w, h), Image.LANCZOS)
bg_img = ImageTk.PhotoImage(bg)

bg_label = Label(reg_win, image=bg_img)
bg_label.place(x=0, y=0, relwidth=1, relheight=1)

# ================= Header =================
header = Label(
    reg_win,
    text="Military Face Authentication & Vehicle Detection",
    font=("Segoe UI", 26, "bold"),
    bg="black",
    fg="white",
    pady=8
)
header.place(x=0, y=0, width=w)

# ================= Database Setup =================
conn = sqlite3.connect("users.db")
cursor = conn.cursor()
cursor.execute("""
CREATE TABLE IF NOT EXISTS users(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT,
    address TEXT,
    dob TEXT,
    age INTEGER,
    username TEXT UNIQUE,
    password TEXT
)
""")
conn.commit()

# ================= Register Function (GO TO LOGIN PAGE) =================
def register_user():
    if entry_password.get() != entry_confirm.get():
        messagebox.showerror("Error", "Passwords do not match")
        return

    try:
        cursor.execute(
            "INSERT INTO users (name,address,dob,age,username,password) VALUES (?,?,?,?,?,?)",
            (
                entry_name.get(),
                entry_address.get(),
                entry_dob.get(),
                entry_age.get(),
                entry_username.get(),
                entry_password.get()
            )
        )
        conn.commit()
        messagebox.showinfo("Success", "Registered Successfully! Please Login.")

        # Close registration window
        reg_win.destroy()

        # Open login page
        os.system("python login.py")

    except sqlite3.IntegrityError:
        messagebox.showerror("Error", "Username already exists")

# ================= RIGHT SIDE GLASS FRAME =================
outer = Frame(reg_win, bg="#00bcd4")
outer.place(relx=0.78, rely=0.55, anchor="center", width=560, height=500)

frame = Frame(outer, bg="#121212")
frame.place(x=4, y=4, width=552, height=492)

title = Label(
    frame,
    text="REGISTRATION FORM",
    font=("Segoe UI", 20, "bold"),
    bg="#121212",
    fg="#00e5ff"
)
title.pack(pady=15)

# ================= Form =================
form = Frame(frame, bg="#121212")
form.pack(pady=5)

def field(lbl, row, show=None):
    Label(
        form,
        text=lbl,
        font=("Segoe UI", 12),
        bg="#121212",
        fg="white"
    ).grid(row=row, column=0, sticky="e", padx=15, pady=8)

    e = Entry(form, font=("Segoe UI", 12), width=24, show=show)
    e.grid(row=row, column=1, pady=8)
    return e

entry_name = field("Full Name:", 0)
entry_address = field("Address:", 1)
entry_dob = field("DOB:", 2)
entry_age = field("Age:", 3)
entry_username = field("Username:", 4)

entry_password = field("Password:", 5, show="*")
entry_confirm = field("Confirm Password:", 6, show="*")

# ================= Eye Toggle =================
def toggle_password(entry, label):
    if entry.cget("show") == "":
        entry.config(show="*")
        label.config(text="👁")
    else:
        entry.config(show="")
        label.config(text="👁‍🗨")

eye_label_pass = Label(form, text="👁", bg="#121212", fg="white", cursor="hand2", font=("Arial", 12))
eye_label_pass.grid(row=5, column=2, padx=5)
eye_label_pass.bind("<Button-1>", lambda e: toggle_password(entry_password, eye_label_pass))

eye_label_confirm = Label(form, text="👁", bg="#121212", fg="white", cursor="hand2", font=("Arial", 12))
eye_label_confirm.grid(row=6, column=2, padx=5)
eye_label_confirm.bind("<Button-1>", lambda e: toggle_password(entry_confirm, eye_label_confirm))

# ================= Buttons =================
btn_frame = Frame(frame, bg="#121212")
btn_frame.pack(pady=20)

def hover(btn, c1, c2):
    btn.bind("<Enter>", lambda e: btn.config(bg=c2))
    btn.bind("<Leave>", lambda e: btn.config(bg=c1))

btn_register = Button(
    btn_frame,
    text="REGISTER",
    font=("Segoe UI", 13, "bold"),
    bg="#00c853",
    fg="white",
    width=13,
    bd=0,
    command=register_user
)
btn_register.grid(row=0, column=0, padx=15)
hover(btn_register, "#00c853", "#00e676")

btn_exit = Button(
    btn_frame,
    text="EXIT",
    font=("Segoe UI", 13, "bold"),
    bg="#d50000",
    fg="white",
    width=13,
    bd=0,
    command=reg_win.destroy
)
btn_exit.grid(row=0, column=1, padx=15)
hover(btn_exit, "#d50000", "#ff1744")

# ================= Run =================
reg_win.mainloop()
