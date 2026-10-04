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
from PIL import Image, ImageTk
from subprocess import call
import os
import time

# ================= Root Window ================= 
root = tk.Tk()
root.title("MILITARY FACE & VEHICLE DETECTION")
root.configure(bg="black")

w, h = root.winfo_screenwidth(), root.winfo_screenheight()
root.geometry(f"{w}x{h}+0+0")

# ================= Background Image =================
bg_path = "1.jpeg"

if not os.path.exists(bg_path):
    raise FileNotFoundError(f"Background image '{bg_path}' not found!")

bg = Image.open(bg_path).resize((w, h), Image.LANCZOS)
bg_img = ImageTk.PhotoImage(bg)

tk.Label(root, image=bg_img).place(x=0, y=0, relwidth=1, relheight=1)

# ================= Header =================
header = tk.Frame(root, bg="#000814", height=65)
header.pack(fill="x")

tk.Label(
    header,
    text=" MILITARY FACE & VEHICLE DETECTION SYSTEM",
    font=("Segoe UI", 26, "bold"),
    fg="white",
    bg="#000814"
).pack(side="left", padx=30)

time_lbl = tk.Label(
    header,
    font=("Segoe UI", 12, "bold"),
    fg="#00FFCC",
    bg="#000814"
)
time_lbl.pack(side="right", padx=30)

def update_time():
    time_lbl.config(text=time.strftime("%d %b %Y  |  %H:%M:%S"))
    root.after(1000, update_time)

update_time()

# ================= Compact Left HUD Panel =================
panel_x, panel_y = 40, 200   # moved downward from 120 → 200
panel_w, panel_h = 300, 360

canvas = tk.Canvas(
    root,
    width=panel_w,
    height=panel_h,
    bg="#020617",
    highlightthickness=0
)
canvas.place(x=panel_x, y=panel_y)

border = canvas.create_rectangle(
    3, 3, panel_w-3, panel_h-3,
    outline="#00FFD5", width=3
)

glow = 120
direction = 1

def animate_border():
    global glow, direction
    glow += direction * 4
    if glow > 230:
        direction = -1
    elif glow < 90:
        direction = 1
    canvas.itemconfig(border, outline=f"#00{glow:02x}CC")
    root.after(40, animate_border)

animate_border()

content = tk.Frame(root, bg="#020617")
content.place(x=panel_x+15, y=panel_y+15, width=panel_w-30, height=panel_h-30)

# ================= Status =================
status_frame = tk.Frame(content, bg="#020617")
status_frame.pack(pady=15)

dot = tk.Label(
    status_frame, text="●",
    font=("Segoe UI", 16, "bold"),
    fg="#00FF00", bg="#020617"
)
dot.pack(side="left", padx=(0, 6))

tk.Label(
    status_frame,
    text="SYSTEM ONLINE",
    font=("Segoe UI", 13, "bold"),
    fg="#00FF00",
    bg="#020617"
).pack(side="left")

dot_on = True
def blink():
    global dot_on
    dot.config(fg="#020617" if dot_on else "#00FF00")
    dot_on = not dot_on
    root.after(500, blink)

blink()

# ================= Button Functions =================
def reg():
    if os.path.exists("registration.py"):
        call(["python", "registration.py"])

def login():
    if os.path.exists("login.py"):
        call(["python", "login.py"])

def exit_app():
    root.destroy()

# ================= Buttons =================
def hud_button(text, cmd, is_exit=False):
    btn = tk.Button(
        content,
        text=text,
        command=cmd,
        font=("Segoe UI", 14, "bold"),
        bg="#0A1A2F",
        fg="#00FFD5",
        activeforeground="black",
        width=18,
        bd=0,
        cursor="hand2"
    )
    btn.pack(pady=12)

    if is_exit:
        # 🔴 EXIT BUTTON HOVER → RED
        btn.bind("<Enter>", lambda e: btn.config(bg="#B22222", fg="white"))
        btn.bind("<Leave>", lambda e: btn.config(bg="#0A1A2F", fg="#00FFD5"))
    else:
        btn.bind("<Enter>", lambda e: btn.config(bg="#00FFD5", fg="black"))
        btn.bind("<Leave>", lambda e: btn.config(bg="#0A1A2F", fg="#00FFD5"))

    return btn

hud_button("REGISTRATION", reg)
hud_button("LOGIN", login)
hud_button("EXIT SYSTEM", exit_app, is_exit=True)

# ================= Footer =================
tk.Label(
    root,
    text="© 2026 Military AI Surveillance | Secure Mode Enabled",
    font=("Segoe UI", 10),
    bg="#000814",
    fg="gray"
).place(relx=0.5, rely=0.97, anchor="center")

# ================= Run =================
root.mainloop()
