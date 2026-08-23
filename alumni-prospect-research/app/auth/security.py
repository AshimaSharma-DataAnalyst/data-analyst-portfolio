from datetime import datetime
from datetime import timedelta
from datetime import timezone

from jose import jwt
from jose import JWTError

from passlib.context import CryptContext

from app.config.settings import settings


pwd_context = CryptContext(

    schemes=["bcrypt"],

    deprecated="auto"

)

SECRET_KEY = getattr(

    settings,

    "SECRET_KEY",

    "change-this-secret-key"

)

ALGORITHM = "HS256"

ACCESS_TOKEN_EXPIRE_MINUTES = 60


def hash_password(password: str):

    return pwd_context.hash(password)


def verify_password(

    plain_password,

    hashed_password

):

    return pwd_context.verify(

        plain_password,

        hashed_password

    )


def create_access_token(

    data: dict,

    expires_delta: timedelta | None = None

):

    to_encode = data.copy()

    expire = (

        datetime.now(timezone.utc)

        + (

            expires_delta

            if expires_delta

            else timedelta(

                minutes=ACCESS_TOKEN_EXPIRE_MINUTES

            )

        )

    )

    to_encode.update(

        {

            "exp": expire

        }

    )

    return jwt.encode(

        to_encode,

        SECRET_KEY,

        algorithm=ALGORITHM

    )


def verify_token(

    token: str

):

    try:

        payload = jwt.decode(

            token,

            SECRET_KEY,

            algorithms=[ALGORITHM]

        )

        return payload

    except JWTError:

        return None
