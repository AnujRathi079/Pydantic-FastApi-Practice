from fastapi import FastAPI
from models import Student
from config import settings

app = FastAPI(title=settings.app_name)

# Preloaded data (5 students)
students = [
    Student(name="Anuj Rathi", marks=88, age=21, email="anuj@gmail.com"),
    Student(name="Rahul Sharma", marks=75, age=20, email="rahul@gmail.com"),
    Student(name="Priya Singh", marks=92, age=22, email="priya@gmail.com"),
    Student(name="Amit Kumar", marks=65, age=19, email="amit@gmail.com"),
    Student(name="Neha Verma", marks=80, age=21, email="neha@gmail.com"),
]

@app.get("/")
def home():
    return {"message": f"{settings.app_name} is running 🚀"}

# CREATE
@app.post("/student")
def create_student(student: Student):
    students.append(student)
    return {
        "message": "Student added",
        "data": student
    }

# READ
@app.get("/students")
def get_students():
    return students

# UPDATE
@app.put("/student/{index}")
def update_student(index: int, student: Student):
    if index >= len(students):
        return {"error": "Student not found"}
    
    students[index] = student
    return {"message": "Student updated", "data": student}

# DELETE
@app.delete("/student/{index}")
def delete_student(index: int):
    if index >= len(students):
        return {"error": "Student not found"}
    
    removed = students.pop(index)
    return {"message": "Student deleted", "data": removed}