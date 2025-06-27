#  _______________
#  Import LIBRARIES
from fastapi import FastAPI

#  Import FILES
from models.models import User

#  _______________

app: FastAPI = FastAPI()


@app.get(path="/")
def index() -> dict[str, str]:
    return {"message": "Hello World"}


@app.get(path="/about/")
def about() -> dict[str, str]:
    return {"Info": "This is the about page"}


@app.get("/hello/{name}")
def say_hello(name: str) -> dict[str, str]:
    return {"message": f"Hello {name}, welcome on FastApi example"}


@app.post("/create-user")
def create_user(user: User) -> dict[str, str | int]:
    return {"message": f"User {user.name} added successfully", "age": user.age}


# def main():
#     print("Hello from fast-hafiz!")


# if __name__ == "__main__":
#     main()


#  _______________
#  Import LIBRARIES
#  Import FILES
#  _______________
