from fastapi import FastAPI, Depends, HTTPException
from pydantic import BaseModel
from sqlalchemy.orm import Session

from database import engine, Base, SessionLocal
from models import Student


app = FastAPI()

Base.metadata.create_all(bind=engine)


# Database session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


# Student input format
class StudentCreate(BaseModel):
    name: str
    date_of_birth: str
    email: str


# Home route
@app.get("/")
def home():
    return {"message": "Students CRUD Application is running!"}


# Add a new student
@app.post("/students")
def create_student(
    student: StudentCreate,
    db: Session = Depends(get_db)
):
    existing_student = (
        db.query(Student)
        .filter(Student.email == student.email)
        .first()
    )

    if existing_student:
        raise HTTPException(
            status_code=400,
            detail="Email already exists"
        )

    new_student = Student(
        name=student.name,
        date_of_birth=student.date_of_birth,
        email=student.email
    )

    db.add(new_student)
    db.commit()
    db.refresh(new_student)

    return {
        "message": "Student added successfully!",
        "id": new_student.id,
        "name": new_student.name,
        "date_of_birth": new_student.date_of_birth,
        "email": new_student.email
    }


@app.get("/students")
def get_students(db:Session = Depends(get_db)):
    students = db.query(Student).all()

    return students


@app.get("/students/{student_id}")
def get_student(student_id: int, db: Session = Depends(get_db)):
    student = db.query(Student).filter(Student.id == student_id).first()

    if student is None:
        raise HTTPException(status_code=404, detail="Student not found")

    return student


@app.put("/students/{student_id}")
def update_student(
    student_id: int,
    student: StudentCreate,
    db: Session = Depends(get_db)
):
    existing_student = db.query(Student).filter(
        Student.id == student_id
    ).first()

    if existing_student is None:
        raise HTTPException(
            status_code=404,
            detail="Student not found"
        )

    existing_student.name = student.name
    existing_student.date_of_birth = student.date_of_birth
    existing_student.email = student.email

    db.commit()
    db.refresh(existing_student)

    return {
        "message": "Student updated successfully!",
        "id": existing_student.id,
        "name": existing_student.name,
        "date_of_birth": existing_student.date_of_birth,
        "email": existing_student.email
    }

@app.delete("/students/{student_id}")
def delete_student(
    student_id: int,
    db: Session = Depends(get_db)
):
    student = db.query(Student).filter(
        Student.id == student_id
    ).first()

    if student is None:
        raise HTTPException(
            status_code=404,
            detail="Student not found"
        )

    db.delete(student)
    db.commit()

    return {
        "message": "Student deleted successfully!",
        "id": student_id
    }
