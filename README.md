# Students CRUD Application

## Project Overview
The Students CRUD Application is a Python-based backend project developed using FastAPI and SQLite. It allows users to add, view, update, and delete student records.

## Technologies Used
- Python
- FastAPI
- SQLite
- SQLAlchemy
- Uvicorn

## Features
- Add new student records
- View all students
- View a student by ID
- Update student details
- Delete student records
- Prevent duplicate email addresses
- Handle student records that do not exist

## Student Information
Each student record contains:
- Student ID
- Name
- Date of Birth
- Email

## Installation and Setup

### 1. Clone the Repository
```bash
git clone https://github.com/samimansari5608-netizen/Students_CRUD_Project.git
cd Students_CRUD_Project
```

### 2. Create a Virtual Environment
```bash
python -m venv .venv
```

### 3. Activate the Virtual Environment on Windows
```powershell
.venv\Scripts\activate
```

### 4. Install Dependencies
```bash
pip install -r requirements.txt
```

### 5. Run the Application
```bash
uvicorn main:app --reload
```

The application will run at:
http://127.0.0.1:8000

## API Documentation
After starting the application, open:
http://127.0.0.1:8000/docs

## API Endpoints

| Method | Endpoint | Description |
|---|---|---|
| POST | `/students` | Add a student |
| GET | `/students` | View all students |
| GET | `/students/{student_id}` | View a student by ID |
| PUT | `/students/{student_id}` | Update student details |
| DELETE | `/students/{student_id}` | Delete a student |

## Database
SQLite is used to store student records, and SQLAlchemy handles database operations.

## Author
Samim Ansari