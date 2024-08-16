from fastapi import FastAPI ,Query
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class Student(BaseModel):
    id: int
    name: str
    grade: int

students = [
    Student(id=1,name="Abdullah",grade=5),
    Student(id=2,name="Iman",grade=3)
]

@app.get("/students")
def get_students():
    return students

@app.post("/students")
def create_student(New_Student:Student):
    students.append(New_Student)
    return New_Student

@app.put("/students/{stu_id}")
def update_student(stu_id:int ,updated_student:Student):
    for index,student in enumerate(students):
        if student.id == stu_id:
            students[index] = updated_student
            return updated_student
    return {"error":"student not found"}

@app.delete("/students/{stu_id}")
def delete_student(stu_id:int):
    for index,student in enumerate(students):
        if student.id == stu_id:
            del students[index]
            return {"message":"student deleted"}
    return {"error":"student not found"}