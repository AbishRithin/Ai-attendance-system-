# 🎓 AI Attendance System Using Face Recognition

An AI-powered attendance management system that uses **real-time face recognition** to identify registered students and automatically record their attendance.

The system captures student face images using a webcam, generates facial encodings, recognizes registered students in real time, stores attendance records in an SQLite database, and provides a Streamlit dashboard for viewing and exporting attendance information.

---

## 📌 Project Overview

Traditional attendance systems require manual calling of student names or manually entering attendance.

This project automates the process using:

```text
Webcam
   ↓
Face Detection
   ↓
Face Encoding
   ↓
Face Recognition
   ↓
Student Identification
   ↓
Attendance Verification
   ↓
SQLite Database
   ↓
Streamlit Dashboard
```

When a registered student appears in front of the camera, the system identifies the student and records their attendance.

---

# ✨ Features

### 👤 Student Registration
Capture multiple face images for each student using the webcam.

### 🤖 Face Recognition
Recognize registered students using facial encodings.

### 👥 Multiple Student Recognition
Multiple registered students can be detected and recognized in the same camera frame.

### 📷 Real-Time Webcam Detection
The system continuously processes webcam frames and searches for registered faces.

### ✅ Automatic Attendance
Once a student is recognized, the system records:

- Student name
- Date
- Time

### 🚫 Duplicate Prevention
The system checks whether the student has already been marked present on the current date.

If attendance already exists:

```text
Already Marked Today
```

A second attendance record is not created.

### 🗄️ SQLite Database
Attendance information is stored locally in:

```text
database/attendance.db
```

### 📊 Streamlit Dashboard
A web dashboard allows attendance records to be viewed and exported.

### 📥 CSV Export
Attendance records can be downloaded as a CSV file from the dashboard.

---

# 🧠 How the System Works

The system consists of several stages.

## Stage 1 — Face Registration

The webcam captures multiple images of a student.

```text
Student
   ↓
Webcam
   ↓
Face Images
   ↓
dataset/StudentName/
```

Example:

```text
dataset/
├── Matheesh/
│   ├── 1.jpg
│   ├── 2.jpg
│   ├── 3.jpg
│   └── ...
│
├── Santhosh/
│   ├── 1.jpg
│   ├── 2.jpg
│   └── ...
```

---

## Stage 2 — Model Training

The training script processes the images and generates face encodings.

```text
Student Images
      ↓
Face Detection
      ↓
Face Encoding
      ↓
Numerical Representation
      ↓
encodings.pkl
```

The generated model is stored locally as:

```text
models/encodings.pkl
```

---

## Stage 3 — Face Recognition

When the attendance system starts:

```text
Webcam
   ↓
Live Frame
   ↓
Detect Face
   ↓
Generate Encoding
   ↓
Compare With Registered Encodings
   ↓
Identify Student
```

If a matching face is found:

```text
Matheesh
```

If no matching face is found:

```text
Unknown
```

---

## Stage 4 — Attendance

After identifying the student:

```text
Recognized Student
       ↓
Check Database
       ↓
Has attendance been marked today?
       ↓
   ┌───┴────┐
   │        │
  NO       YES
   │        │
   ↓        ↓
 INSERT   Ignore
   │
   ↓
Attendance Marked
```

---

# 🏗️ System Architecture

```text
                         ┌───────────────────┐
                         │      Webcam       │
                         └─────────┬─────────┘
                                   │
                                   ▼
                         ┌───────────────────┐
                         │  Face Detection   │
                         │      OpenCV       │
                         └─────────┬─────────┘
                                   │
                                   ▼
                         ┌───────────────────┐
                         │  Face Encoding    │
                         │ face_recognition  │
                         └─────────┬─────────┘
                                   │
                                   ▼
                         ┌───────────────────┐
                         │ Face Comparison   │
                         │ With Trained Data │
                         └─────────┬─────────┘
                                   │
                         ┌─────────┴─────────┐
                         │                   │
                         ▼                   ▼
                  ┌─────────────┐     ┌─────────────┐
                  │ Recognized  │     │   Unknown   │
                  │   Student   │     │    Face     │
                  └──────┬──────┘     └─────────────┘
                         │
                         ▼
                ┌─────────────────┐
                │ Check Attendance │
                └────────┬────────┘
                         │
                         ▼
                ┌─────────────────┐
                │ SQLite Database │
                └────────┬────────┘
                         │
                         ▼
                ┌─────────────────┐
                │    Streamlit    │
                │    Dashboard    │
                └─────────────────┘
```

---

# 🛠️ Technology Stack

| Technology | Purpose |
|---|---|
| Python 3.12 | Core programming language |
| OpenCV | Webcam and computer vision |
| face_recognition | Face detection and recognition |
| face_recognition_models | Face recognition model data |
| NumPy | Numerical computation |
| Pandas | Data processing |
| SQLite | Attendance database |
| Streamlit | Web dashboard |
| Plotly | Data visualization |
| Git | Version control |
| GitHub | Source code hosting |

---

# 📂 Project Structure

```text
ai-attendance-system/
│
├── assets/
│
├── captured/
│
├── database/
│   └── attendance.db
│
├── dataset/
│   └── StudentName/
│
├── docs/
│
├── logs/
│
├── models/
│   └── encodings.pkl
│
├── src/
│   ├── attendance.py
│   ├── capture_faces.py
│   ├── config.py
│   ├── database.py
│   ├── database_utils.py
│   ├── train_model.py
│   └── utils.py
│
├── dashboard.py
├── requirements.txt
├── README.md
└── .gitignore
```

### Important

The following files/directories are generated locally and should normally **not** be committed to a public repository:

```text
venv/
dataset/<student-face-images>/
models/encodings.pkl
database/attendance.db
```

This is especially important because student face images are biometric information.

---

# 💻 Requirements

Before installing the project, make sure you have:

- Python 3.12
- Git
- A working webcam
- Internet connection for installing Python dependencies

Python 3.12 is recommended for this project because the face-recognition dependency stack may have compatibility issues with newer Python versions.

---

# 🐧 Linux / Ubuntu Installation

## Step 1 — Install Git

Check whether Git is installed:

```bash
git --version
```

If Git is not installed:

```bash
sudo apt update
sudo apt install git
```

Verify:

```bash
git --version
```

---

## Step 2 — Check Python

```bash
python3 --version
```

You should preferably have:

```text
Python 3.12.x
```

If `python3.12` is available:

```bash
python3.12 --version
```

---

## Step 3 — Clone the Repository

Clone the project:

```bash
git clone https://github.com/Matheesh777/ai-attendance-system.git
```

Go inside the project:

```bash
cd ai-attendance-system
```

Check the files:

```bash
ls
```

You should see files such as:

```text
README.md
dashboard.py
requirements.txt
src
models
database
dataset
```

---

# 🪟 Windows Installation

## Step 1 — Install Git

Check:

```powershell
git --version
```

If Git is not installed, install Git for Windows.

After installation, reopen PowerShell.

---

## Step 2 — Check Python

```powershell
python --version
```

or:

```powershell
py --version
```

Recommended:

```text
Python 3.12.x
```

---

## Step 3 — Clone the Repository

Open PowerShell:

```powershell
git clone https://github.com/Matheesh777/ai-attendance-system.git
```

Enter the project:

```powershell
cd ai-attendance-system
```

Check the files:

```powershell
dir
```

---

# 🐍 Virtual Environment

A virtual environment keeps the project's Python packages separate from your system Python installation.

---

## 🐧 Linux / Ubuntu

Create the environment:

```bash
python3.12 -m venv venv
```

Activate it:

```bash
source venv/bin/activate
```

After activation, your terminal should look similar to:

```text
(venv) user@computer:~/ai-attendance-system$
```

Verify:

```bash
python --version
```

Verify Python location:

```bash
which python
```

It should point to something similar to:

```text
.../ai-attendance-system/venv/bin/python
```

---

## 🪟 Windows

Create the environment:

```powershell
py -3.12 -m venv venv
```

Activate:

```powershell
venv\Scripts\activate
```

Verify:

```powershell
python --version
```

Check Python location:

```powershell
where python
```

The path should point to:

```text
ai-attendance-system\venv\Scripts\python.exe
```

---

# 📦 Install Dependencies

Make sure the virtual environment is activated.

Upgrade pip:

```bash
python -m pip install --upgrade pip
```

Install all project dependencies:

```bash
pip install -r requirements.txt
```

Verify installed packages:

```bash
pip list
```

---

# 📋 requirements.txt

The project dependencies include:

```text
opencv-python
face-recognition
face-recognition-models
numpy
pandas
streamlit
plotly
Pillow
```

---

# 📷 Step 1 — Register a Student

The first stage is collecting face images.

Run:

```bash
python src/capture_faces.py
```

The program will ask:

```text
Enter Student Name:
```

Enter the student's name:

```text
Matheesh
```

The webcam will open.

Position the student's face in front of the camera and allow the program to capture the required images.

---

# 📁 Dataset Structure

After registration:

```text
dataset/
└── Matheesh/
    ├── 1.jpg
    ├── 2.jpg
    ├── 3.jpg
    ├── ...
```

For multiple students:

```text
dataset/
├── Matheesh/
│   ├── 1.jpg
│   ├── 2.jpg
│   └── ...
│
├── Santhosh/
│   ├── 1.jpg
│   ├── 2.jpg
│   └── ...
│
├── Rahul/
│   ├── 1.jpg
│   ├── 2.jpg
│   └── ...
│
└── Arun/
    ├── 1.jpg
    ├── 2.jpg
    └── ...
```

Each student must have a separate folder.

---

# 👥 Adding Multiple Students

Run the capture program again:

```bash
python src/capture_faces.py
```

Enter:

```text
Santhosh
```

Then repeat:

```bash
python src/capture_faces.py
```

Enter:

```text
Rahul
```

Repeat again for additional students.

For example:

```text
dataset/
├── Matheesh/
├── Santhosh/
├── Rahul/
└── Arun/
```

---

# 🧠 Step 2 — Train the Face Recognition Model

After registering students, train the model:

```bash
python src/train_model.py
```

The training process reads the entire dataset.

Conceptually:

```text
dataset/
   │
   ├── Matheesh
   ├── Santhosh
   ├── Rahul
   └── Arun
          ↓
   Face Detection
          ↓
   Face Encodings
          ↓
   Trained Encoding Data
          ↓
models/encodings.pkl
```

You should see a message indicating that the model/encodings were generated.

---

# 🔄 When Should You Retrain?

You should retrain whenever you add a new student.

Example:

You already have:

```text
Matheesh
Santhosh
Rahul
```

Then you register:

```text
Arun
```

Run:

```bash
python src/train_model.py
```

again.

The training script rebuilds the encoding data from the complete dataset.

---

# 🎥 Step 3 — Start the Attendance System

Run:

```bash
python src/attendance.py
```

The webcam will open.

The system continuously performs:

```text
Capture Frame
     ↓
Resize Frame
     ↓
Detect Faces
     ↓
Generate Face Encodings
     ↓
Compare Against Known Faces
     ↓
Identify Student
     ↓
Check Today's Attendance
     ↓
Mark Attendance
```

---

# 🟢 Recognized Student

If the face matches a registered student:

```text
Matheesh
Attendance Marked
```

The attendance is stored in SQLite.

---

# 🟡 Already Marked

If the same student is recognized again on the same day:

```text
Matheesh
Already Marked Today
```

The system does not create another attendance record.

This prevents a student from receiving hundreds of attendance records while standing in front of the camera.

---

# 🔴 Unknown Student

If the face does not match a registered student:

```text
Unknown
```

The system should not mark attendance for that person.

---

# 👥 Multiple Faces

The system can process multiple faces detected in a camera frame.

Example:

```text
          WEBCAM

┌──────────────────────────────────┐
│                                  │
│   ┌─────────┐      ┌─────────┐  │
│   │Matheesh │      │Santhosh │  │
│   └─────────┘      └─────────┘  │
│                                  │
│      ┌─────────┐                 │
│      │  Rahul  │                 │
│      └─────────┘                 │
│                                  │
└──────────────────────────────────┘
```

Each recognized student is checked independently.

The database may contain:

```text
Matheesh | 2026-08-08 | 09:01:12
Santhosh | 2026-08-08 | 09:01:13
Rahul    | 2026-08-08 | 09:01:14
```

---

# 🗄️ Step 4 — Attendance Database

Attendance is stored locally using SQLite.

Database location:

```text
database/attendance.db
```

The database contains attendance information such as:

```text
Student Name
Date
Time
```

---

# 🔍 Inspect the Database

If SQLite CLI is available:

```bash
sqlite3 database/attendance.db
```

Then:

```sql
SELECT * FROM attendance;
```

Example:

```text
1|Matheesh|2026-08-08|09:01:12
2|Santhosh|2026-08-08|09:01:13
3|Rahul|2026-08-08|09:01:14
```

Exit SQLite:

```sql
.quit
```

---

# 📊 Step 5 — Start the Streamlit Dashboard

Open another terminal.

Go to the project:

```bash
cd ai-attendance-system
```

Activate the virtual environment.

### Linux

```bash
source venv/bin/activate
```

### Windows

```powershell
venv\Scripts\activate
```

Start Streamlit:

```bash
streamlit run dashboard.py
```

The terminal will provide a local URL similar to:

```text
http://localhost:8501
```

Open that URL in your browser.

---

# 📊 Dashboard

The dashboard provides a graphical interface for attendance information.

Typical functionality includes:

- Attendance records
- Student search
- Date filtering
- Attendance statistics
- Attendance visualization
- CSV download

---

# 📥 Export Attendance

The dashboard provides an option to download attendance information as a CSV file.

The exported data can be opened using:

- Microsoft Excel
- LibreOffice Calc
- Google Sheets
- Python Pandas
- Other spreadsheet applications

---

# 🔄 Complete End-to-End Workflow

For a completely fresh installation:

```bash
git clone https://github.com/Matheesh777/ai-attendance-system.git

cd ai-attendance-system
```

Create environment.

### Linux

```bash
python3.12 -m venv venv
source venv/bin/activate
```

### Windows

```powershell
py -3.12 -m venv venv
venv\Scripts\activate
```

Install dependencies:

```bash
python -m pip install --upgrade pip
pip install -r requirements.txt
```

Register students:

```bash
python src/capture_faces.py
```

Train the model:

```bash
python src/train_model.py
```

Start attendance:

```bash
python src/attendance.py
```

Start dashboard in another terminal:

### Linux

```bash
source venv/bin/activate
streamlit run dashboard.py
```

### Windows

```powershell
venv\Scripts\activate
streamlit run dashboard.py
```

---

# 🧪 Recommended Testing Procedure

For the first test, use only one student.

## Test 1 — Registration

```bash
python src/capture_faces.py
```

Register:

```text
Matheesh
```

---

## Test 2 — Training

```bash
python src/train_model.py
```

---

## Test 3 — Recognition

```bash
python src/attendance.py
```

Look at the camera.

Expected:

```text
Matheesh
Attendance Marked
```

---

## Test 4 — Duplicate Prevention

Continue looking at the camera.

Expected:

```text
Matheesh
Already Marked Today
```

There should still be only one attendance record for the day.

---

## Test 5 — Multiple Students

Register another student:

```bash
python src/capture_faces.py
```

Train again:

```bash
python src/train_model.py
```

Start:

```bash
python src/attendance.py
```

Have both registered students appear in front of the camera.

Verify that both are recognized separately.

---

# ⚡ Performance Optimization

The attendance system processes webcam frames continuously.

To improve performance, the recognition implementation can:

- Process smaller frames
- Skip unnecessary frames
- Use efficient face detection
- Avoid repeatedly inserting the same attendance record

This is particularly useful when running the system on laptops with limited CPU resources.

---

# 🛑 Stopping the Applications

## Stop Attendance

Inside the webcam window:

```text
Q
```

or stop the terminal process using:

```text
Ctrl + C
```

---

## Stop Streamlit

In the Streamlit terminal:

```text
Ctrl + C
```

---

# 🐧 Linux Troubleshooting

## Webcam Not Opening

Check available video devices:

```bash
ls /dev/video*
```

You can also check whether another application is currently using the webcam.

Close applications such as:

- Camera
- Zoom
- Google Meet
- Microsoft Teams
- OBS
- Other webcam applications

Then run:

```bash
python src/attendance.py
```

---

## Check Python

```bash
python --version
```

---

## Check Pip

```bash
pip --version
```

---

## Check Installed Packages

```bash
pip list
```

---

## Reinstall Dependencies

If the environment becomes corrupted:

```bash
pip install --upgrade pip
pip install -r requirements.txt
```

---

# 🪟 Windows Troubleshooting

## Webcam Permission

Make sure Windows allows desktop applications to access the camera.

Check:

```text
Settings
→ Privacy & security
→ Camera
```

Enable camera access.

---

## Check Python

```powershell
python --version
```

---

## Check Pip

```powershell
pip --version
```

---

## Check Virtual Environment

```powershell
where python
```

The result should point to:

```text
ai-attendance-system\venv\Scripts\python.exe
```

---

# ⚠️ Common Errors

## `ModuleNotFoundError`

Example:

```text
ModuleNotFoundError: No module named ...
```

Make sure the virtual environment is activated.

Linux:

```bash
source venv/bin/activate
```

Windows:

```powershell
venv\Scripts\activate
```

Then:

```bash
pip install -r requirements.txt
```

---

## `face_recognition_models` Error

If the face-recognition package reports that its model package is missing:

```bash
pip install face-recognition-models
```

Then test:

```bash
python -c "import face_recognition_models; print('Models OK')"
```

---

## Python Compatibility Problems

If you encounter dependency/build problems with a newer Python version, use Python 3.12.

Check:

```bash
python --version
```

Create a fresh Python 3.12 environment.

Linux:

```bash
python3.12 -m venv venv
```

Windows:

```powershell
py -3.12 -m venv venv
```

Then activate and reinstall:

```bash
pip install -r requirements.txt
```

---

# 🧹 Recreating the Virtual Environment

If the virtual environment becomes corrupted:

## Linux

Deactivate:

```bash
deactivate
```

Remove:

```bash
rm -rf venv
```

Create again:

```bash
python3.12 -m venv venv
```

Activate:

```bash
source venv/bin/activate
```

Install:

```bash
pip install -r requirements.txt
```

---

## Windows

Deactivate:

```powershell
deactivate
```

Remove:

```powershell
Remove-Item -Recurse -Force venv
```

Create again:

```powershell
py -3.12 -m venv venv
```

Activate:

```powershell
venv\Scripts\activate
```

Install:

```powershell
pip install -r requirements.txt
```

---

# 🔐 Privacy and Ethical Use

This system processes facial information.

Face images and face encodings should be treated as sensitive biometric information.

For responsible use:

- Obtain appropriate permission from students before collecting face images.
- Do not publish real student face datasets on GitHub.
- Do not share generated face encodings publicly.
- Do not upload private attendance databases to public repositories.
- Store biometric information securely.
- Use the system only for authorized purposes.
- Follow applicable privacy and institutional policies.

The repository intentionally excludes local datasets, generated encodings, and attendance databases.

---

# 🚀 Future Improvements

The current system provides the core face-recognition attendance workflow.

Possible future improvements include:

### 👤 Student Management

- Student ID
- Department
- Year
- Section
- Email
- Profile information

### 📊 Advanced Analytics

- Daily attendance
- Weekly attendance
- Monthly attendance
- Attendance percentage
- Present/Absent statistics
- Student-wise reports

### 🔐 Security

- Liveness detection
- Anti-spoofing
- User authentication
- Admin login
- Role-based access

### ☁️ Cloud

- Cloud database
- Cloud deployment
- Remote dashboard
- Backup and synchronization

### 📧 Notifications

- Email attendance reports
- Parent notifications
- Low attendance alerts

### 🎥 User Interface

- Student registration through Streamlit
- Live camera inside the dashboard
- One-click model training
- Student management panel

### 📱 Accessibility

- Responsive dashboard
- Mobile-friendly interface

---

# 📌 Important Notes

## Do not upload these files

```text
venv/
dataset/<real-student-images>/
models/encodings.pkl
database/attendance.db
```

These files are local/generated data and may contain sensitive information.

---

# 🔗 Repository

GitHub:

https://github.com/Matheesh777/ai-attendance-system

Clone:

```bash
git clone https://github.com/Matheesh777/ai-attendance-system.git
```

---

# 👨‍💻 Author

## Matheesh Joshco

GitHub:

https://github.com/Matheesh777

---

# ⭐ Support

If you find this project useful, consider giving the repository a ⭐ on GitHub.

---

# 📜 License

This project is intended for educational, academic, and authorized demonstration purposes.