# ============================================================
# MASTER MILITARY SURVEILLANCE SYSTEM - SINGLE APPLICATION
# Copyright (c) 2026 Sumit Raj (MT24AAI011) - VNIT Nagpur
# ============================================================

import tkinter as tk
from tkinter import ttk, messagebox
import subprocess
import sys
import os
from datetime import datetime

class MilitarySurveillanceSystem:
    def __init__(self, root):
        self.root = root
        self.root.title("MILITARY SURVEILLANCE SYSTEM")
        self.root.geometry("900x650")
        self.root.configure(bg="#0a0a2a")
        
        # Center the window on screen
        self.center_window()
        
        # Create UI
        self.create_header()
        self.create_main_menu()
        self.create_status_bar()
        
    def center_window(self):
        """Center the window on screen"""
        self.root.update_idletasks()
        width = 900
        height = 650
        x = (self.root.winfo_screenwidth() // 2) - (width // 2)
        y = (self.root.winfo_screenheight() // 2) - (height // 2)
        self.root.geometry(f'{width}x{height}+{x}+{y}')
    
    def create_header(self):
        """Create header with title and time"""
        # Title Frame
        title_frame = tk.Frame(self.root, bg="#0a0a2a", height=120)
        title_frame.pack(fill="x", pady=20)
        
        # Main Title
        title = tk.Label(title_frame, text="⚔️ MILITARY SURVEILLANCE SYSTEM ⚔️", 
                        font=("Arial", 28, "bold"), bg="#0a0a2a", fg="#FFD700")
        title.pack(pady=10)
        
        # Subtitle
        subtitle = tk.Label(title_frame, text="AI Powered Border Security & Surveillance", 
                           font=("Arial", 14), bg="#0a0a2a", fg="#00FF00")
        subtitle.pack()
        
        # Author Info
        author = tk.Label(title_frame, text="Sumit Raj (MT24AAI011) | Guide: Prof. Meera Dhabu", 
                         font=("Arial", 10), bg="#0a0a2a", fg="#888888")
        author.pack(pady=5)
        
        # Separator Line
        separator = tk.Frame(self.root, bg="#FFD700", height=2)
        separator.pack(fill="x", padx=50, pady=10)
    
    def create_main_menu(self):
        """Create main menu buttons"""
        # Main Frame for buttons
        main_frame = tk.Frame(self.root, bg="#0a0a2a")
        main_frame.pack(expand=True, fill="both", pady=30)
        
        # Button Style
        btn_style = {
            "font": ("Arial", 16, "bold"),
            "width": 28,
            "height": 2,
            "bg": "#1a1a4a",
            "fg": "white",
            "relief": "raised",
            "bd": 4,
            "cursor": "hand2"
        }
        
        # Button 1: Face Authentication
        btn1 = tk.Button(main_frame, text="🔐 FACE AUTHENTICATION SYSTEM", 
                        command=self.run_face_authentication, **btn_style)
        btn1.pack(pady=15)
        self.add_hover_effect(btn1, "#2a2a6a", "#1a1a4a")
        
        # Button 2: Vehicle Detection
        btn2 = tk.Button(main_frame, text="🚗 MILITARY VEHICLE DETECTION", 
                        command=self.run_vehicle_detection, **btn_style)
        btn2.pack(pady=15)
        self.add_hover_effect(btn2, "#2a2a6a", "#1a1a4a")
        
        # Button 3: Full Surveillance Dashboard
        btn3 = tk.Button(main_frame, text="🎮 FULL SURVEILLANCE DASHBOARD", 
                        command=self.run_full_dashboard, **btn_style)
        btn3.pack(pady=15)
        self.add_hover_effect(btn3, "#2a2a6a", "#1a1a4a")
        
        # Button 4: System Info
        btn4 = tk.Button(main_frame, text="ℹ️ SYSTEM INFORMATION", 
                        command=self.show_system_info, **btn_style)
        btn4.pack(pady=15)
        self.add_hover_effect(btn4, "#2a2a6a", "#1a1a4a")
        
        # Button 5: Exit
        btn5 = tk.Button(main_frame, text="❌ EXIT SYSTEM", 
                        command=self.exit_system, **btn_style, bg="#8b0000")
        btn5.pack(pady=15)
        self.add_hover_effect(btn5, "#aa0000", "#8b0000")
    
    def add_hover_effect(self, button, hover_color, normal_color):
        """Add hover effect to buttons"""
        button.bind("<Enter>", lambda e: button.config(bg=hover_color))
        button.bind("<Leave>", lambda e: button.config(bg=normal_color))
    
    def create_status_bar(self):
        """Create status bar at bottom"""
        status_frame = tk.Frame(self.root, bg="#1a1a2a", height=30)
        status_frame.pack(side="bottom", fill="x")
        
        # Status text
        self.status_label = tk.Label(status_frame, text="✅ SYSTEM READY | Status: Online", 
                                     font=("Arial", 10), bg="#1a1a2a", fg="#00FF00")
        self.status_label.pack(side="left", padx=20, pady=5)
        
        # Time
        self.time_label = tk.Label(status_frame, font=("Arial", 10), bg="#1a1a2a", fg="#888888")
        self.time_label.pack(side="right", padx=20, pady=5)
        self.update_time()
    
    def update_time(self):
        """Update time in status bar"""
        current_time = datetime.now().strftime("%d-%m-%Y | %H:%M:%S")
        self.time_label.config(text=current_time)
        self.root.after(1000, self.update_time)
    
    def run_face_authentication(self):
        """Run Face Authentication module"""
        try:
            self.status_label.config(text="🔄 Loading Face Authentication System...", fg="#FFA500")
            self.root.update()
            
            # Check if running as EXE or script
            if getattr(sys, 'frozen', False):
                # Running as compiled EXE
                subprocess.Popen([sys.executable, "Face_Authantication.py"])
            else:
                # Running as Python script
                subprocess.Popen(["python", "Face_Authantication.py"])
            
            self.status_label.config(text="✅ Face Authentication System Launched", fg="#00FF00")
            
        except Exception as e:
            messagebox.showerror("Error", f"Failed to launch Face Authentication:\n{str(e)}")
            self.status_label.config(text="❌ Error launching Face Authentication", fg="#FF0000")
    
    def run_vehicle_detection(self):
        """Run Vehicle Detection module"""
        try:
            self.status_label.config(text="🔄 Loading Vehicle Detection System...", fg="#FFA500")
            self.root.update()
            
            if getattr(sys, 'frozen', False):
                subprocess.Popen([sys.executable, "testing.py"])
            else:
                subprocess.Popen(["python", "testing.py"])
            
            self.status_label.config(text="✅ Vehicle Detection System Launched", fg="#00FF00")
            
        except Exception as e:
            messagebox.showerror("Error", f"Failed to launch Vehicle Detection:\n{str(e)}")
            self.status_label.config(text="❌ Error launching Vehicle Detection", fg="#FF0000")
    
    def run_full_dashboard(self):
        """Run Full GUI Dashboard"""
        try:
            self.status_label.config(text="🔄 Loading Full Surveillance Dashboard...", fg="#FFA500")
            self.root.update()
            
            if getattr(sys, 'frozen', False):
                subprocess.Popen([sys.executable, "GUI_Master.py"])
            else:
                subprocess.Popen(["python", "GUI_Master.py"])
            
            self.status_label.config(text="✅ Full Dashboard Launched", fg="#00FF00")
            
        except Exception as e:
            messagebox.showerror("Error", f"Failed to launch Dashboard:\n{str(e)}")
            self.status_label.config(text="❌ Error launching Dashboard", fg="#FF0000")
    
    def show_system_info(self):
        """Show system information"""
        info_text = """
╔══════════════════════════════════════════════════════════════╗
║              MILITARY SURVEILLANCE SYSTEM                    ║
╠══════════════════════════════════════════════════════════════╣
║                                                              ║
║  Project: AI Powered Military Vehicle Detection             ║
║           and Face Authentication System                    ║
║                                                              ║
║  Author: Sumit Raj (MT24AAI011)                             ║
║  Guide: Prof. Meera Dhabu                                   ║
║  Institute: VNIT Nagpur                                     ║
║  Year: 2026                                                 ║
║                                                              ║
║  Technologies Used:                                         ║
║  • YOLOv8 for Vehicle Detection                             ║
║  • Haar Cascade + LBPH for Face Recognition                 ║
║  • OpenCV for Image Processing                              ║
║  • Python Tkinter for GUI                                   ║
║                                                              ║
║  Results:                                                   ║
║  • Vehicle Detection mAP: 91.3%                             ║
║  • Face Recognition: 92% accuracy                          ║
║  • Processing Speed: 25.9 FPS                               ║
║                                                              ║
╚══════════════════════════════════════════════════════════════╝
        """
        messagebox.showinfo("System Information", info_text)
    
    def exit_system(self):
        """Exit the application"""
        if messagebox.askyesno("Exit", "Are you sure you want to exit the system?"):
            self.root.destroy()

# ============================================================
# MAIN APPLICATION ENTRY POINT
# ============================================================

if __name__ == "__main__":
    root = tk.Tk()
    app = MilitarySurveillanceSystem(root)
    root.mainloop()