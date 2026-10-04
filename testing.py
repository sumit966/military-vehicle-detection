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

from ultralytics import YOLO
import cv2
import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageTk
import threading
import smtplib
from email.message import EmailMessage
import requests
import json
from datetime import datetime
import os
import time

# ================= MODEL =================
model = YOLO("best.pt")

# ================= EMAIL CONFIG =================
SENDER_EMAIL = "your_email@gmail.com"      # REPLACE WITH YOUR EMAIL
RECEIVER_EMAIL = "your_email@gmail.com"    # REPLACE WITH YOUR EMAIL
PASSWORD = "your_app_password"              # REPLACE WITH YOUR PASSWORD

# ================= DISTANCE SETTINGS =================
KNOWN_WIDTHS = {
    "Aircraft": 10.0,
    "Armoured Fighting Vehicle-AFV-": 3.5,
    "Armoured Personal Carrier-APC-": 2.9,
    "Army-vehicle": 2.5,
    "Light Armoured Vehicle-LAV-": 2.8,
    "Military engineering vehicle-MEV-": 3.2
}
FOCAL_LENGTH = 650

# ================= GLOBALS =================
cap = None
running = False
last_sent_time = 0

if not os.path.exists("captures"):
    os.makedirs("captures")

# ================= LOCATION =================
def get_location():
    try:
        url = "http://api.ipstack.com/check?access_key=a7003977af457525708100fca423928d"
        data = json.loads(requests.get(url).text)
        return data.get("city","NA"), data.get("country_name","NA")
    except:
        return "NA","NA"

# ================= EMAIL FUNCTION =================
def send_email(vehicle, image_path):
    city, country = get_location()
    time_now = datetime.now().strftime("%d-%m-%Y %H:%M:%S")

    msg = EmailMessage()
    msg["Subject"] = f"🚨 Vehicle Detected: {vehicle}"
    msg["From"] = SENDER_EMAIL
    msg["To"] = RECEIVER_EMAIL
    msg.set_content(f"Vehicle: {vehicle}\nTime: {time_now}\nLocation: {city}, {country}")

    with open(image_path, "rb") as f:
        msg.add_attachment(f.read(), maintype="image", subtype="jpeg", filename=os.path.basename(image_path))

    with smtplib.SMTP_SSL("smtp.gmail.com", 465) as smtp:
        smtp.login(SENDER_EMAIL, PASSWORD)
        smtp.send_message(msg)

# ================= DISTANCE FUNCTION =================
def estimate_distance(label, box_width):
    if label in KNOWN_WIDTHS and box_width > 0:
        real_width = KNOWN_WIDTHS[label]
        distance = (real_width * FOCAL_LENGTH) / box_width
        return round(distance, 2)
    return None

# ================= IOU FUNCTION =================
def iou(boxA, boxB):
    xA = max(boxA[0], boxB[0])
    yA = max(boxA[1], boxB[1])
    xB = min(boxA[2], boxB[2])
    yB = min(boxA[3], boxB[3])

    interArea = max(0, xB - xA) * max(0, yB - yA)
    boxAArea = (boxA[2]-boxA[0]) * (boxA[3]-boxA[1])
    boxBArea = (boxB[2]-boxB[0]) * (boxB[3]-boxB[1])
    return interArea / float(boxAArea + boxBArea - interArea + 1e-6)

# ================= UPDATE FRAME =================
def update_frame(frame):
    frame = cv2.resize(frame, (1100, 700))  # HD resolution for clear text
    frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    img = Image.fromarray(frame_rgb)
    imgtk = ImageTk.PhotoImage(img)
    video_label.imgtk = imgtk
    video_label.configure(image=imgtk)

# ================= DETECTION =================
def detect(source):
    global cap, running, last_sent_time
    running = True
    cap = cv2.VideoCapture(source)

    while running:
        ret, frame = cap.read()
        if not ret:
            break

        results = model(frame, conf=0.5)
        detections = []

        for r in results:
            if r.boxes is not None:
                for box in r.boxes:
                    x1, y1, x2, y2 = map(int, box.xyxy[0])
                    conf = float(box.conf[0])
                    cls = int(box.cls[0])
                    detections.append([x1,y1,x2,y2,conf,cls])

        detections.sort(key=lambda x: x[4], reverse=True)
        final_boxes = []

        while detections:
            best = detections.pop(0)
            final_boxes.append(best)
            detections = [d for d in detections if iou(best[:4], d[:4]) < 0.5]

        for x1,y1,x2,y2,conf,cls in final_boxes:
            label = model.names[cls]
            box_width = x2 - x1
            distance = estimate_distance(label, box_width)

            # ================= TEXT =================
            if distance:
                text = f"{label} | {conf:.2f} | {distance} m"
            else:
                text = f"{label} | {conf:.2f}"

            # Color based on distance
            if distance and distance < 20:
                color = (0, 0, 255)   # RED = danger
            else:
                color = (0, 255, 0)   # GREEN = normal

            # Bounding box
            cv2.rectangle(frame, (x1, y1), (x2, y2), color, 3)

            # Big & bold font
            font = cv2.FONT_HERSHEY_SIMPLEX
            font_scale = 1.0
            thickness = 3

            (text_w, text_h), _ = cv2.getTextSize(text, font, font_scale, thickness)

            # Text position fix
            text_x = x1
            text_y = y1 - 10
            if text_y < 20:
                text_y = y1 + text_h + 15

            # Background rectangle
            cv2.rectangle(frame,
                          (text_x, text_y - text_h - 12),
                          (text_x + text_w + 8, text_y),
                          (0, 0, 0), -1)

            # Draw text
            cv2.putText(frame, text,
                        (text_x + 4, text_y - 4),
                        font, font_scale, color, thickness)

            # ================= EMAIL ALERT =================
            current_time = time.time()
            if current_time - last_sent_time > 15:
                img_path = f"captures/{label}_{int(current_time)}.jpg"
                cv2.imwrite(img_path, frame)
                threading.Thread(target=send_email, args=(label, img_path), daemon=True).start()
                last_sent_time = current_time

        update_frame(frame)

    cap.release()

# ================= UI FUNCTIONS =================
def open_camera():
    stop_detection()
    threading.Thread(target=detect, args=(0,), daemon=True).start()

def upload_video():
    stop_detection()
    path = filedialog.askopenfilename(filetypes=[("Video Files", "*.mp4 *.avi *.mov")])
    if path:
        threading.Thread(target=detect, args=(path,), daemon=True).start()

def stop_detection():
    global running
    running = False

# ================= TKINTER UI =================
root = tk.Tk()
root.title("Vehicle Detection & Distance Estimation")
root.geometry("1100x750")
root.configure(bg="#121212")

tk.Label(root, text="Vehicle Detection & Distance Alert System",
         font=("Arial", 20, "bold"), fg="white", bg="#121212").pack(pady=10)

video_label = tk.Label(root, bg="black")
video_label.pack(pady=10)

btn_frame = tk.Frame(root, bg="#121212")
btn_frame.pack(pady=20)

tk.Button(btn_frame, text="Open Camera", width=18, height=2,
          bg="#4CAF50", fg="white", font=("Arial", 12, "bold"),
          command=open_camera).grid(row=0, column=0, padx=20)

tk.Button(btn_frame, text="Upload Video", width=18, height=2,
          bg="#2196F3", fg="white", font=("Arial", 12, "bold"),
          command=upload_video).grid(row=0, column=1, padx=20)

tk.Button(btn_frame, text="Stop", width=18, height=2,
          bg="#f44336", fg="white", font=("Arial", 12, "bold"),
          command=stop_detection).grid(row=0, column=2, padx=20)

root.mainloop()
