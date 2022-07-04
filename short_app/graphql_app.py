"""
Description: GraphQl version
Author: Prabal Pathak
"""

from typing import Optional

from fastapi import FastAPI, Depends
from pydantic import BaseModel
import strawberry
from strawberry.fastapi import GraphQLRouter


class UserSchema(BaseModel):
    """pydantic user schema

    Args:
        BaseModel : base class of pydantic models
    """

    name: str
    age: int


@strawberry.type
class User:
    """user schema"""

    name: str
    age: int


@strawberry.type
class Query:
    """graphql query details

    Returns:
        User
    """

    @strawberry.field
    def user(self) -> User:
        """user details

        Returns:
            User: user schema
        """
        return User(name="Prabal Pathak", age=23)

    @strawberry.field
    def add_user(self, name: str, age: int) -> User:
        """Add user

        Args:
            name (str): name of user

        Returns:
            dict: details added
        """
        return User(name=name, age=age)


schema = strawberry.Schema(query=Query)
graphql_app = GraphQLRouter(schema)
app = FastAPI()


@app.get("/root")
def root():
    """testing route

    Returns:
        dict: test reply
    """
    return {"message": "Hello world!"}


@app.post("/name")
def return_name(data: Optional[UserSchema] = Depends(UserSchema)):
    """return given data

    Args:
        data (User, optional): name and age

    Returns:
        User: user data
    """
    return data


app.include_router(graphql_app, prefix="/graphql")
# app.add_websocket_route("/graphql", graphql_app)
