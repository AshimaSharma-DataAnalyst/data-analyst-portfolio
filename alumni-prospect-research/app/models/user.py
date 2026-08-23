from sqlalchemy import Boolean
from sqlalchemy import Column
from sqlalchemy import Integer
from sqlalchemy import String

from app.database.database import Base


class User(Base):

    __tablename__ = "users"

    id = Column(
        Integer,
        primary_key=True,
        index=True
    )

    username = Column(
        String,
        unique=True,
        nullable=False,
        index=True
    )

    email = Column(
        String,
        unique=True,
        nullable=False,
        index=True
    )

    hashed_password = Column(
        String,
        nullable=False
    )

    is_active = Column(
        Boolean,
        default=True
    )

    is_admin = Column(
        Boolean,
        default=False
    )