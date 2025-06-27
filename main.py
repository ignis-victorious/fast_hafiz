#  _______________
#  Import LIBRARIES
from fastapi import FastAPI

#  Import FILES
#  _______________

app: FastAPI = FastAPI()


@app.get(path="/")
def index() -> dict[str, str]:
    return {"message": "Hello World"}


# def main():
#     print("Hello from fast-hafiz!")


# if __name__ == "__main__":
#     main()


#  _______________
#  Import LIBRARIES
#  Import FILES
#  _______________
