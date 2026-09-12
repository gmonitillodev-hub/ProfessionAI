import uuid
from datetime import datetime
from typing import Optional, List, Self
from uuid import UUID

from pydantic import BaseModel, Field, EmailStr, PrivateAttr, ConfigDict, model_validator


class Book(BaseModel):
    title: str = Field(..., description="The title of the book", max_length=5)
    author: str
    year: int
    isbn: Optional[str] = Field(None, description="The ISBN of the book")


class User(BaseModel):
    model_config = ConfigDict(extra='allow', str_to_lower=True)
    _createdAt: datetime = PrivateAttr(default_factory=datetime.now)
    uid: UUID = Field(default_factory=uuid.uuid4)
    username: str = Field(..., description="The username of the user")
    email: EmailStr = Field(..., description="The email of the user")
    borrowed_book: List[Book] = Field(description="The list of books owned by this user", default_factory=list)

    @model_validator(mode='after')
    def validate_after(self: Self) -> Self:
        if self.username != 'andrea':
            raise ValueError("Nome non conforme")

def main():
    try:
        user1 = User(
            username="ANDREA",
            email="user1@test.com",
        )
        print(f"Without dump {user1}")
        print(f"With dump {user1.model_dump()}")
        print(f"With dump json {user1.model_dump_json()}")

    except Exception as e:
        print((e.errors()))

        print(e.error_count())


if __name__ == "__main__":
    main()
