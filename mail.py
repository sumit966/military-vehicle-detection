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

import smtplib
from email.message import EmailMessage
import imghdr
import os

def mail():
   SENDER_EMAIL = "your_email@gmail.com"      # REPLACE WITH YOUR EMAIL
   RECEIVER_EMAIL = "your_email@gmail.com"    # REPLACE WITH YOUR EMAIL
   PASSWORD = "your_app_password"              # REPLACE WITH YOUR PASSWORD

    image_path = "unauth_user.jpg"
    if not os.path.exists(image_path):
        print("[ERROR] unauth_user.jpg not found.")
        return

    newMessage = EmailMessage()
    newMessage['Subject'] = "⚠️ Alert: Unauthenticated User Detected"
    newMessage['From'] = Sender_Email
    newMessage['To'] = Receiver_Email
    newMessage.set_content("An unauthenticated person has been detected by the system.")

    with open(image_path, 'rb') as f:
        image_data = f.read()
        image_type = imghdr.what(f.name)
        image_name = os.path.basename(f.name)
    newMessage.add_attachment(image_data, maintype='image', subtype=image_type, filename=image_name)

    try:
        with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
            smtp.login(Sender_Email, Password)
            smtp.send_message(newMessage)
        print("[INFO] Email alert sent successfully.")
    except Exception as e:
        print(f"[ERROR] Email failed: {e}")

if __name__ == "__main__":
    mail()
