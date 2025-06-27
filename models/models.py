#  _______________
#  Import LIBRARIES
from pydantic import BaseModel

#  Import FILES
#  _______________


class User(BaseModel):
    name: str
    surnamename: str
    age: int


# {"name": "Erre", "age": 18, "address":{ "city:": "London" "zipcode": "54000"}}


class Address(BaseModel):
    city: str
    zipcode: str


class Student(BaseModel):
    name: str
    age: int
    address: Address


class Valedictorian(BaseModel):
    name: str
    age: int


# class Student(BaseModel):
#     name: str
#     roll_no: int
#     email: str | None = None
#     class_name: str = "10th Grade"


# class Student(BaseModel):
#     id: int
#     name: str
#     age: int
#     email: str


class Product(BaseModel):
    product_name: str
    price: float
    description: str | None
    in_stock: bool = True


class Order(BaseModel):
    customer_name: str
    items: list[Product]  # List of objects inside the body
