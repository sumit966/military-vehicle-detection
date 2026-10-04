# Military Vehicle Detection & Face Authentication System

AI-powered military surveillance system using **YOLOv8** for vehicle detection and **Haar Cascade + LBPH** for face authentication, with automated email alerts and GPS location tracking.

![Python](https://img.shields.io/badge/Python-3.10-blue?logo=python)
![YOLOv8](https://img.shields.io/badge/YOLOv8-Ultralytics-purple)
![OpenCV](https://img.shields.io/badge/OpenCV-4.8-green?logo=opencv)
![Tkinter](https://img.shields.io/badge/GUI-Tkinter-blue)

> **M.Tech Project** · VNIT Nagpur · Author: Sumit Raj (MT24AAI011) · Guide: Prof. Meera Dhabu

---

## 🎯 Overview

Real-time military surveillance system with two core capabilities:

1. **Military Vehicle Detection** — YOLOv8 detects military vehicles with distance estimation and automated email alerts
2. **Face Authentication** — Haar Cascade + LBPH authenticates personnel and alerts on unknown persons

---

## ✨ Features

### 🚗 Vehicle Detection
- YOLOv8 custom-trained on military vehicles
- Real-time detection with **91.3% mAP**
- Distance estimation using reference widths
- IoU-based overlap filtering
- Automated email alerts with image + GPS location
- Color-coded boxes (Red = danger, Green = normal)

### 🔐 Face Authentication
- User registration with SQLite
- Haar Cascade face detection
- LBPH recognition with **92% accuracy**
- Unknown person alerts with email + image
- Secure login system

### 🎨 GUI
- HUD-style command center with glowing animations
- Real-time clock + system status
- Full-screen dashboard

---

## 🛠️ Tech Stack

| Category | Technology |
|----------|-----------|
| Language | Python 3.10 |
| Object Detection | YOLOv8 (Ultralytics) |
| Face Recognition | Haar Cascade + LBPH |
| Computer Vision | OpenCV 4.8 |
| GUI | Tkinter |
| Database | SQLite |
| Email | SMTP (Gmail) |
| Location | ipstack API |

---

## 📁 Files

| File | Purpose |
|------|---------|
| `master_system.py` | Main launcher |
| `gui_main.py` | Initial HUD dashboard |
| `GUI_Master.py` | Command center GUI |
| `registration.py` | User registration |
| `login.py` | Login system |
| `face_registration.py` | Face DB registration |
| `Face_Authantication.py` | Face auth module |
| `testing.py` | Vehicle detection (YOLOv8) |
| `mail.py` | Email alerts |
| `model_CNN.py` | CNN preprocessing |

---

## 🚀 Installation

```bash
git clone https://github.com/sumit966/military-vehicle-detection.git
cd military-vehicle-detection
pip install ultralytics opencv-python opencv-contrib-python Pillow numpy pandas scikit-learn requests
