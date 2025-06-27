#  _______________
#  Import LIBRARIES
from fastapi import FastAPI

#  Import FILES
from models.models import Student, User

#  _______________

app: FastAPI = FastAPI()


@app.get(path="/")
def index() -> dict[str, str]:
    return {"message": "Hello Mum"}


@app.get(path="/about/")
def about() -> dict[str, str]:
    return {"Info": "This is the about page"}


@app.get(path="/hello/{name}")
def say_hello(name: str) -> dict[str, str]:
    return {"message": f"Hello {name}, welcome on FastApi example"}


@app.post(path="/create-user")
def create_user(user: User) -> dict[str, str | int]:
    return {"message": f"User {user.name} added successfully", "age": user.age}


@app.get(path="/student/{id}")
def get_id(id: int) -> dict[str, str]:
    return {"message": f"Student id is: {id}"}


@app.post(path="/create-student")
def create_student(student: Student) -> dict[str, str | int]:
    return {
        "message": "User created successfully",
        "name": student.name,
        "age": student.age,
        "email": student.email,
    }


# @app.get(path="/student-details")
# # @app.get(path="/student-details")
# def student_details(student: Student) -> tuple[str]:
#     return (
#         f"The student name and surname are: {student.fname} {student.lname} while the age is: {student.age}",
#     )


# def main():
#     print("Hello from fast-hafiz!")


# if __name__ == "__main__":
#     main()


#  _______________
#  Import LIBRARIES
#  Import FILES
#  _______________
