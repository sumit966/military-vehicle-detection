<!-- ═══════════════════════════════════════════════════════════════ -->
<!-- 🎖️ Military Vehicle Detection & Face Auth — Animated README -->
<!-- ═══════════════════════════════════════════════════════════════ -->

<div align="center">
  <img src="https://capsule-render.vercel.app/api?type=waving&color=gradient&customColorList=12,20,24,30&height=220&section=header&text=🎖️%20Military%20Vehicle%20Detection&fontSize=42&fontColor=ffffff&animation=fadeIn&fontAlignY=38&desc=YOLOv8%20%2B%20Haar%20Cascade%20%2B%20LBPH%20%7C%20Real-time%20Surveillance&descAlignY=58&descSize=17" />
</div>

<div align="center">
  <a href="https://git.io/typing-svg">
    <img src="https://readme-typing-svg.herokuapp.com?font=JetBrains+Mono&weight=600&size=22&duration=3000&pause=800&color=10B981&center=true&vCenter=true&multiline=true&width=750&height=100&lines=🎯+YOLOv8+Vehicle+Detection+(91.3%25+mAP);🔐+Face+Auth+(92%25+Accuracy);📧+Automated+Email+Alerts;📍+GPS+Location+Tracking" alt="Typing SVG" />
  </a>
</div>

<br/>

<div align="center">
  <a href="https://github.com/sumit966/military-vehicle-detection/stargazers">
    <img src="https://img.shields.io/github/stars/sumit966/military-vehicle-detection?style=for-the-badge&color=10b981&labelColor=0d1117&logo=github&logoColor=white" />
  </a>
  <a href="https://github.com/sumit966/military-vehicle-detection/network/members">
    <img src="https://img.shields.io/github/forks/sumit966/military-vehicle-detection?style=for-the-badge&color=3b82f6&labelColor=0d1117&logo=git&logoColor=white" />
  </a>
  <a href="https://github.com/sumit966/military-vehicle-detection/issues">
    <img src="https://img.shields.io/github/issues/sumit966/military-vehicle-detection?style=for-the-badge&color=ec4899&labelColor=0d1117&logo=github&logoColor=white" />
  </a>
  <a href="https://github.com/sumit966/military-vehicle-detection/commits/main">
    <img src="https://img.shields.io/github/last-commit/sumit966/military-vehicle-detection?style=for-the-badge&color=f59e0b&labelColor=0d1117&logo=git&logoColor=white" />
  </a>
</div>

<br/>

<div align="center">
  <img src="https://img.shields.io/badge/Python-3.10-3776AB?style=for-the-badge&logo=python&logoColor=white" />
  <img src="https://img.shields.io/badge/YOLOv8-Ultralytics-purple?style=for-the-badge&logo=yolo&logoColor=white" />
  <img src="https://img.shields.io/badge/OpenCV-4.8-5C3EE8?style=for-the-badge&logo=opencv&logoColor=white" />
  <img src="https://img.shields.io/badge/Tkinter-GUI-3776AB?style=for-the-badge&logo=python&logoColor=white" />
  <img src="https://img.shields.io/badge/SQLite-Database-003B57?style=for-the-badge&logo=sqlite&logoColor=white" />
  <img src="https://img.shields.io/badge/SMTP-Email-D14836?style=for-the-badge&logo=gmail&logoColor=white" />
</div>

<br/>

<div align="center">
  <img src="https://img.shields.io/badge/Vehicle_mAP-91.3%25-10b981?style=for-the-badge&logo=target&logoColor=white" />
  <img src="https://img.shields.io/badge/Face_Auth-92%25-3b82f6?style=for-the-badge&logo=faces&logoColor=white" />
  <img src="https://img.shields.io/badge/Speed-25.9_FPS-8b5cf6?style=for-the-badge&logo=speedtest&logoColor=white" />
  <img src="https://img.shields.io/badge/Alert_Latency-<2s-f59e0b?style=for-the-badge&logo=clock&logoColor=white" />
</div>

<br/>

<div align="center">
  <i>🎓 M.Tech Project · VNIT Nagpur · <b>Sumit Raj</b> (MT24AAI011) · Guide: <b>Prof. Meera Dhabu</b></i>
</div>

<br/>

<img src="https://raw.githubusercontent.com/andreasbm/readme/master/assets/lines/rainbow.png" width="100%" />

---

## 📑 Table of Contents

<div align="center">

| 🎯 | 🎯 | 🎯 |
|:---:|:---:|:---:|
| [Overview](#-overview) | [Features](#-features) | [Tech Stack](#️-tech-stack) |
| [Project Structure](#-project-structure) | [Installation](#-installation) | [Requirements](#-requirements) |
| [Configuration](#️-configuration) | [Usage](#-usage) | [Results](#-results) |
| [Dataset](#-dataset) | [Author](#-author) | [License](#-license) |

</div>

---

## 🎯 Overview

<div align="center">
  <img src="https://user-images.githubusercontent.com/74038190/212257472-08e52665-c503-4bd9-aa20-f5a4dae769b5.gif" width="400" alt="Surveillance animation"/>
</div>

<br/>

Real-time military surveillance system with **two core capabilities**:

<table align="center">
<tr>
<td width="50%" valign="top" align="center">

### 🚗 Military Vehicle Detection

<img src="https://img.shields.io/badge/🎯-YOLOv8-10b981?style=for-the-badge" />

Real-time vehicle detection with **distance estimation** and **automated email alerts**.

</td>
<td width="50%" valign="top" align="center">

### 🔐 Face Authentication

<img src="https://img.shields.io/badge/🔐-Haar+LBPH-3b82f6?style=for-the-badge" />

Authenticates personnel and alerts on **unknown persons** via email.

</td>
</tr>
</table>

---

## ✨ Features

<table align="center">
<tr>
<td width="33%" valign="top">

### 🚗 Vehicle Detection

- 🎯 YOLOv8 custom-trained
- 📊 **91.3% mAP** accuracy
- 📏 Distance estimation
- 🔀 IoU overlap filtering
- 📧 Email + GPS alerts
- 🎨 Color-coded boxes

</td>
<td width="33%" valign="top">

### 🔐 Face Authentication

- 📝 User registration (SQLite)
- 👤 Haar Cascade detection
- 🧠 **LBPH 92% accuracy**
- ⚠️ Unknown person alerts
- 🔐 Secure login system
- 📸 Image capture on alert

</td>
<td width="33%" valign="top">

### 🎨 HUD Interface

- 🖥️ Command center GUI
- ✨ Glowing animations
- ⏰ Real-time clock
- 📊 System status
- 🖥️ Full-screen dashboard
- 🎮 Tkinter-based

</td>
</tr>
</table>

---

## 🛠️ Tech Stack

<table align="center">
<tr>
<td><b>Category</b></td>
<td><b>Technology</b></td>
</tr>
<tr>
<td>🐍 Language</td>
<td><img src="https://img.shields.io/badge/Python_3.10-3776AB?style=flat-square&logo=python&logoColor=white" /></td>
</tr>
<tr>
<td>🎯 Object Detection</td>
<td><img src="https://img.shields.io/badge/YOLOv8-Ultralytics-purple?style=flat-square" /></td>
</tr>
<tr>
<td>🔐 Face Recognition</td>
<td><img src="https://img.shields.io/badge/Haar_Cascade_+_LBPH-3b82f6?style=flat-square" /></td>
</tr>
<tr>
<td>👁️ Computer Vision</td>
<td><img src="https://img.shields.io/badge/OpenCV_4.8-5C3EE8?style=flat-square&logo=opencv&logoColor=white" /></td>
</tr>
<tr>
<td>🖥️ GUI</td>
<td><img src="https://img.shields.io/badge/Tkinter-3776AB?style=flat-square&logo=python&logoColor=white" /></td>
</tr>
<tr>
<td>🗄️ Database</td>
<td><img src="https://img.shields.io/badge/SQLite-003B57?style=flat-square&logo=sqlite&logoColor=white" /></td>
</tr>
<tr>
<td>📧 Email</td>
<td><img src="https://img.shields.io/badge/SMTP_Gmail-D14836?style=flat-square&logo=gmail&logoColor=white" /></td>
</tr>
<tr>
<td>📍 Location</td>
<td><img src="https://img.shields.io/badge/ipstack_API-10b981?style=flat-square" /></td>
</tr>
</table>

---

## 🏗️ Architecture

```mermaid
flowchart LR
    A[📹 Webcam Feed] --> B{🧠 AI Processing}
    B --> C[🚗 YOLOv8 Detection]
    B --> D[👤 Haar + LBPH Auth]
    C --> E[📏 Distance Calc]
    C --> F[🎨 Color Boxes]
    D --> G[✅ Known Person]
    D --> H[⚠️ Unknown Alert]
    E --> I[📧 Email Alert]
    H --> I
    F --> J[🖥️ HUD Display]
    G --> J
    I --> K[📍 GPS Location]
    
    style A fill:#8b5cf6,stroke:#fff,color:#fff
    style I fill:#ec4899,stroke:#fff,color:#fff
    style J fill:#10b981,stroke:#fff,color:#fff
```

---

## 📁 Project Structure

```
military-vehicle-detection/
├── 🚀 master_system.py              # Main launcher
├── 🖥️ gui_main.py                   # Initial HUD dashboard
├── 🎮 GUI_Master.py                 # Command center GUI
├── 📝 registration.py               # User registration
├── 🔐 login.py                      # Login system
├── 👤 face_registration.py          # Face DB registration
├── 🔒 Face_Authantication.py        # Face auth module
├── 🎯 testing.py                    # Vehicle detection (YOLOv8)
├── 📧 mail.py                       # Email alerts
├── 🧠 model_CNN.py                  # CNN preprocessing
├── 📋 requirements.txt              # Dependencies
└── 📖 README.md                     # This file
```

---

## 🚀 Installation

<div align="center">
  <img src="https://img.shields.io/badge/⏱️_5_min_setup-3776AB?style=for-the-badge" />
  <img src="https://img.shields.io/badge/🎯_YOLOv8_required-purple?style=for-the-badge" />
</div>

<br/>

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/sumit966/military-vehicle-detection.git
cd military-vehicle-detection
```

### 2️⃣ Create Virtual Environment (Recommended)

```bash
python -m venv venv
venv\Scripts\activate        # Windows
source venv/bin/activate     # Mac/Linux
```

### 3️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

**Or install manually:**

```bash
pip install ultralytics opencv-python opencv-contrib-python Pillow numpy pandas scikit-learn requests
```

---

## 📋 Requirements

Create a `requirements.txt` file with:

```txt
ultralytics>=8.0.0
opencv-python>=4.8.0
opencv-contrib-python>=4.8.0
Pillow>=10.0.0
numpy>=1.24.0
pandas>=2.0.0
scikit-learn>=1.3.0
requests>=2.31.0
tkinter
smtplib
sqlite3
```

### Pre-trained Files Needed

<table align="center">
<tr>
<td><b>File</b></td>
<td><b>Purpose</b></td>
<td><b>Where to Get</b></td>
</tr>
<tr>
<td><code>best.pt</code></td>
<td>YOLOv8 trained model</td>
<td>Train with custom dataset</td>
</tr>
<tr>
<td><code>haarcascade_frontalface_default.xml</code></td>
<td>Face detector</td>
<td>OpenCV GitHub</td>
</tr>
<tr>
<td><code>trainingData.yml</code></td>
<td>LBPH face trainer</td>
<td>Generated by <code>face_registration.py</code></td>
</tr>
</table>

---

## ⚙️ Configuration

### 📧 Email Settings (`testing.py`)

Open `testing.py` and update:

```python
SENDER_EMAIL = "your_email@gmail.com"
RECEIVER_EMAIL = "your_email@gmail.com"
PASSWORD = "your_app_password"        # Use Gmail App Password, NOT login password
SMTP_SERVER = "smtp.gmail.com"
SMTP_PORT = 587
```

**🔑 How to get Gmail App Password:**

1. Go to Google Account → Security
2. Enable 2-Step Verification
3. Go to App Passwords
4. Generate password for "Mail"
5. Copy 16-character password into `PASSWORD`

### 📍 GPS Location Settings

```python
IPSTACK_API_KEY = "your_ipstack_api_key"   # Get free key from ipstack.com
```

### 🔐 Face Recognition Threshold (`Face_Authantication.py`)

```python
CONFIDENCE_THRESHOLD = 70    # Lower = stricter matching
```

---

## 🎮 Usage

### 🚀 Run the Main System

```bash
python master_system.py
```

### 📋 Step-by-Step Workflow

<table align="center">
<tr>
<td width="50%" valign="top">

**1️⃣ Register a User**
- Open the app → Click "Register"
- Enter username + password
- Credentials saved to SQLite

**2️⃣ Login**
- Enter credentials
- Access main dashboard

**3️⃣ Face Registration (First Time)**
- Go to "Face Registration"
- Capture 30+ images per person
- LBPH model auto-trains → `trainingData.yml`

</td>
<td width="50%" valign="top">

**4️⃣ Vehicle Detection**
- Click "Vehicle Detection"
- Real-time YOLOv8 detection on webcam
- Alerts auto-sent on detection

**5️⃣ Face Authentication**
- Click "Face Authentication"
- Live webcam feed
- Unknown faces → email alert with image

</td>
</tr>
</table>

---

## 📊 Results

<div align="center">
  <img src="https://img.shields.io/badge/Vehicle_mAP-91.3%25-10b981?style=for-the-badge&logo=target&logoColor=white" />
  <img src="https://img.shields.io/badge/Face_Accuracy-92%25-3b82f6?style=for-the-badge&logo=faces&logoColor=white" />
  <img src="https://img.shields.io/badge/Speed-25.9_FPS-8b5cf6?style=for-the-badge&logo=speedtest&logoColor=white" />
  <img src="https://img.shields.io/badge/Alert_Latency-<2s-f59e0b?style=for-the-badge&logo=clock&logoColor=white" />
  <img src="https://img.shields.io/badge/False_Positive-4.2%25-ec4899?style=for-the-badge" />
</div>

<br/>

### 📈 Benchmark Metrics

| Metric | Value |
|--------|-------|
| 🎯 Vehicle Detection mAP | **91.3%** |
| 🔐 Face Recognition Accuracy | **92%** |
| ⚡ Processing Speed | **25.9 FPS** |
| 📧 Alert Latency | **< 2 seconds** |
| ⚠️ False Positive Rate | **4.2%** |

### 🖥️ Sample Output

```bash
[INFO] Loading YOLOv8 model... ✓
[INFO] Loading Haar Cascade... ✓
[INFO] Starting camera feed...
[DETECT] Military tank detected - Confidence: 0.94
[ALERT] Email sent to admin with GPS: 18.5204°N, 73.8567°E
[FACE] Unknown person detected - Confidence: 45.2 (threshold: 70)
```

---

## 📊 Dataset

<table align="center">
<tr>
<td width="50%" valign="top">

### 🚗 Vehicle Detection Dataset

- 📚 **Source:** Custom annotated military vehicle images
- 🎯 **Classes:** Tank, Military Truck, Armored Vehicle, Soldier
- 📸 **Images:** 2,000+ annotated images
- 📝 **Format:** YOLO format (`.txt` labels)
- 🔀 **Split:** 80% train / 10% val / 10% test

</td>
<td width="50%" valign="top">

### 👤 Face Dataset

- 📚 **Source:** Custom webcam captures
- 📸 **Images per person:** 30-50
- 🎨 **Format:** Grayscale 200x200 px
- 📁 **Storage:** `facesData/` folder

</td>
</tr>
</table>

---

## 🧪 Testing

```bash
# 🚗 Test vehicle detection only
python testing.py

# 🔐 Test face auth only
python Face_Authantication.py

# 🚀 Run full system
python master_system.py
```

---

## 🐛 Troubleshooting

| Issue | Solution |
|-------|----------|
| 📷 Camera not opening | Check if other apps are using webcam |
| 📧 Email not sending | Use Gmail App Password, not login password |
| 🎯 Model not loading | Ensure `best.pt` is in root folder |
| 👤 Face not recognized | Re-register with more images (50+) |
| ⚠️ OpenCV error | Reinstall: `pip install --force-reinstall opencv-python` |

---

## 👤 Author

<div align="center">

<img src="https://img.shields.io/badge/Sumit_Raj-MT24AAI011-10b981?style=for-the-badge&labelColor=0d1117" />

<br/><br/>

<b>M.Tech Applied AI & ML · VNIT Nagpur</b>

<br/><br/>

<a href="https://sumit966-github-io.vercel.app">
  <img src="https://img.shields.io/badge/Portfolio-Visit-3b82f6?style=for-the-badge&logo=googlechrome&logoColor=white" />
</a>
<a href="https://www.linkedin.com/in/er-sumit-raj-/">
  <img src="https://img.shields.io/badge/LinkedIn-Connect-0A66C2?style=for-the-badge&logo=linkedin&logoColor=white" />
</a>
<a href="https://github.com/sumit966">
  <img src="https://img.shields.io/badge/GitHub-Follow-181717?style=for-the-badge&logo=github&logoColor=white" />
</a>
<a href="mailto:info.sr0909@gmail.com">
  <img src="https://img.shields.io/badge/Email-Contact-D14836?style=for-the-badge&logo=gmail&logoColor=white" />
</a>

<br/><br/>

<i>🎓 Guide: <b>Prof. Meera Dhabu</b>, VNIT Nagpur</i>

</div>

---

## 🙏 Acknowledgements

<div align="center">

<a href="https://github.com/ultralytics/ultralytics">
  <img src="https://img.shields.io/badge/Ultralytics_YOLOv8-111F68?style=for-the-badge&logo=yolo&logoColor=white" />
</a>
<a href="https://opencv.org/">
  <img src="https://img.shields.io/badge/OpenCV-5C3EE8?style=for-the-badge&logo=opencv&logoColor=white" />
</a>
<a href="https://vnit.ac.in/">
  <img src="https://img.shields.io/badge/VNIT_Nagpur-8b5cf6?style=for-the-badge" />
</a>

</div>

---

## 📄 License

<div align="center">

<img src="https://capsule-render.vercel.app/api?type=rect&color=gradient&customColorList=12,20,24,30&height=2&width=60%" />

<br/>

<img src="https://img.shields.io/badge/⚖️_ACADEMIC_USE_ONLY-f59e0b?style=for-the-badge&labelColor=0d1117" />

<br/><br/>

<samp>
This project is for <b>academic evaluation purposes only</b>.<br/>
Not for commercial or military use without proper authorization.
</samp>

<br/><br/>

<sub><samp>© 2024 &nbsp;·&nbsp; SUMIT RAJ &nbsp;·&nbsp; VNIT NAGPUR</samp></sub>

<br/>

<img src="https://capsule-render.vercel.app/api?type=rect&color=gradient&customColorList=12,20,24,30&height=2&width=60%" />

</div>

<br/>

<img src="https://capsule-render.vercel.app/api?type=waving&color=gradient&customColorList=12,20,24,30&height=120&section=footer&text=🎖️%20Stay%20Vigilant%20·%20Stay%20Secure&fontSize=20&fontColor=ffffff&animation=twinkling" width="100%" />
