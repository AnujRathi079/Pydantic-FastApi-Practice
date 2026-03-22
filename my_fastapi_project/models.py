from pydantic import BaseModel, Field, field_validator
from typing import Optional

class Student(BaseModel):
    name: str = Field(..., min_length=2, max_length=50)
    marks: int = Field(..., ge=0, le=100)
    age: Optional[int] = Field(default=18, ge=5, le=100)
    email: Optional[str] = None

    @field_validator("name")
    def validate_name(cls, v):
        if not v.replace(" ", "").isalpha():
            raise ValueError("Name must contain only alphabets")
        return v.title()

    @field_validator("email")
    def validate_email(cls, v):
        if v and "@" not in v:
            raise ValueError("Invalid email format")
        return v