from pydantic import BaseModel
from pydantic import ConfigDict
from pydantic import EmailStr
from pydantic import Field


class UserCreate(BaseModel):

    username: str = Field(
        ...,
        min_length=3,
        max_length=50
    )

    email: EmailStr

    password: str = Field(
        ...,
        min_length=6
    )


class UserResponse(BaseModel):

    id: int

    username: str

    email: EmailStr

    is_active: bool

    is_admin: bool

    model_config = ConfigDict(
        from_attributes=True
    )


class Token(BaseModel):

    access_token: str

    token_type: str


class TokenData(BaseModel):

    username: str | None = None