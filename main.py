#  _______________
#  Import LIBRARIES
from fastapi import FastAPI

#  Import FILES
from models.models import Product, Student, User

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


#  Works with: {"Name": "elle", "price": 11.99} or /search/?name=elle&price=11.99
@app.get(path="/search/")
#  Works with: {"Name": "elle", "price": 11.99} or /search/?name=elle&price=11.99
# @app.get(path="/search")
def search_item(name: str, price: float) -> dict[str, str | float]:
    return {"Name": name, "price": price}


#  Works with: /products/123?show_details=true
@app.get(path="/products/{product_id}")
def get_product(product_id: int, show_details: bool = False) -> dict[str, int | bool]:
    return {"Product Id": product_id, "Show Details": show_details}


@app.get(path="/student/{id}")
def get_id(id: int) -> dict[str, str]:
    return {"message": f"Student's id is: {id}"}


#  Works with {"name": "elle","roll_no": 20,"email": "elle@elle.com","class_name": "6th Grade"}
@app.post(path="/register/")
def register_student(student: Student) -> dict[str, str | int | None]:
    return {
        "message": "Student registered successfully",
        "name": student.name,
        "roll_no": student.roll_no,
        "email": student.email,
        "class_name": student.class_name,
    }


# @app.post(path="/create-student/")
# def create_student(student: Student) -> dict[str, str | int]:
#     return {
#         "message": "User created successfully",
#         "name": student.name,
#         "age": student.age,
#         "email": student.email,
#     }


#  Works with: {"product_name": "notebook", "price": 299.99, "description": "", "in_stock": true}
@app.post(path="/add-product")
def add_product(product: Product) -> dict[str, str | float | bool | None]:
    return {
        "message": "Product added",
        "product_name": product.product_name,
        "price": product.price,
        "description": product.description,
        "in_stock": product.in_stock,
    }


# #  Works with: /create-student/?id=1000&name=erre&age=21&email=erre@erre.com
# @app.get(path="/student-details")
# # @app.get(path="/student-details/")
# def student_details(student: Student) -> dict[str, int | str]:
#     return {
#         "id": student.id,
#         "name": student.name,
#         "age": student.age,
#     }  # return (f"The student details are: id: {student.id}, name {student.name}, age: {student.age}",)


# def main():
#     print("Hello from fast-hafiz!")


# if __name__ == "__main__":
#     main()


#  _______________
#  Import LIBRARIES
#  Import FILES
#  _______________
