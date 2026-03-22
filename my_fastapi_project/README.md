# Student API using FastAPI & Pydantic

A structured REST API project demonstrating the practical use of Pydantic models, custom validation, and configuration management within a FastAPI application.

This project is designed to showcase real-world backend concepts such as data validation, serialization, and environment-based configuration.


# Project Objectives

This project focuses on the following core Pydantic concepts:

Define Pydantic models with appropriate data types and default values
Implement custom field validators for enforcing complex rules
Use BaseSettings for managing configuration and environment variables
Integrate Pydantic models with FastAPI request/response handling
Practice serialization and deserialization of structured data


# Features
CRUD operations for student records
Strong data validation using Pydantic
Custom validators for name and email
Environment-based configuration using .env
Automatic request & response validation
Interactive API documentation (Swagger)


# Tech Stack
FastAPI – Web framework
Pydantic v2 – Data validation & parsing
Uvicorn – ASGI server
pydantic-settings – Configuration management
Python 3.10+

# Project Structure

project/
│
├── main.py        # API routes and logic
├── models.py      # Pydantic models & validators
├── config.py      # BaseSettings configuration
└── .env           # Environment variables

#  1. Pydantic Model Definition
The Student model defines structured data with constraints:

class Student(BaseModel):
    name: str
    marks: int
    age: Optional[int] = 18
    email: Optional[str] = None

# Enforces:

Type safety
Default values
Field constraints

 # 2. Custom Field Validators

 Custom validation logic ensures business rules:

 @field_validator("name")
def validate_name(cls, v):
    if not v.replace(" ", "").isalpha():
        raise ValueError("Name must contain only alphabets")
    return v.title()

# Ensures:

Clean and formatted names
No invalid characters

# Configuration using BaseSettings

Application settings are managed via environment variables:

class Settings(BaseSettings):
    app_name: str = "Student API"
    debug: bool = True

# Benefits:

Centralized configuration
Environment-based flexibility
Secure variable handling

# Request & Response Validation
FastAPI automatically validates incoming requests using Pydantic:

@app.post("/student")
def create_student(student: Student):

# Ensures:

Valid input data
Automatic error handling (422 errors)

# Serialization & Deserialization
Serialization: Convert model → JSON response
Deserialization: Convert JSON → Pydantic model

student = Student(name="Anuj", marks=90)
print(student.model_dump())  # Convert to dict

# Helps in:

API communication
Data transformation

# | Method | Endpoint           | Description      |
| ------ | ------------------ | ---------------- |
| GET    | `/`                | API status       |
| POST   | `/student`         | Create student   |
| GET    | `/students`        | Get all students |
| PUT    | `/student/{index}` | Update student   |
| DELETE | `/student/{index}` | Delete student   |

# Sample Request 
{
  "name": "Anuj Rathi",
  "marks": 88,
  "age": 21,
  "email": "anuj@gmail.com"
}

# Install dependencies
pip install fastapi uvicorn pydantic pydantic-settings

# Run the server
uvicorn main:app --reload

# Open API Docs
Swagger UI → http://127.0.0.1:8000/docs
ReDoc → http://127.0.0.1:8000/redoc

# .gitignore

This project includes a .gitignore file to exclude unnecessary and sensitive files from version control.

🔒 Ignored Files Include:
Virtual environment folders (.venv/, env/)
Python cache files (__pycache__/)
Environment variables (.env)
System files (.DS_Store, etc.)

# Why it's important:
Keeps repository clean
Prevents sensitive data leaks
Avoids uploading unnecessary files

# License

This project is licensed under the MIT License.

 What this means:
You can use, copy, modify, and distribute this project
You can use it for personal and commercial purposes
You must include the original license

# Permission is hereby granted, free of charge, to any person obtaining a copy
 of this software and associated documentation files...

 # Final Result (Your Repo Looks Like)

 project/
│
├── main.py
├── models.py
├── config.py
├── README.md
├── LICENSE
└── .gitignore

