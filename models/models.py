#  _______________
#  Import LIBRARIES
from pydantic import BaseModel

#  Import FILES
#  _______________


class User(BaseModel):
    name: str
    surnamename: str
    age: int
