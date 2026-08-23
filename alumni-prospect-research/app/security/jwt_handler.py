from datetime import datetime
from datetime import timedelta
from typing import Optional

from jose import JWTError
from jose import jwt

from fastapi import Depends
from fastapi import HTTPException
from fastapi import status

from fastapi.security import OAuth2PasswordBearer

from sqlalchemy.orm import Session

from app.config.settings import settings
from app.database.database import get_db
from app.models.user import User
from app.services.user_service import UserService


# =====================================================
# JWT CONFIGURATION
# =====================================================

SECRET_KEY = settings.JWT_SECRET

ALGORITHM = settings.JWT_ALGORITHM

ACCESS_TOKEN_EXPIRE_MINUTES = (
    settings.ACCESS_TOKEN_EXPIRE_MINUTES
)


oauth2_scheme = OAuth2PasswordBearer(

    tokenUrl="/auth/login"

)


# =====================================================
# CREATE ACCESS TOKEN
# =====================================================

def create_access_token(

    data: dict,

    expires_delta: Optional[timedelta] = None

):

    """
    Creates a JWT token.

    Payload Example

    {

        "sub":"ashima"

    }

    """

    to_encode = data.copy()

    if expires_delta:

        expire = datetime.utcnow() + expires_delta

    else:

        expire = (

            datetime.utcnow()

            + timedelta(

                minutes=ACCESS_TOKEN_EXPIRE_MINUTES

            )

        )

    to_encode.update(

        {

            "exp": expire

        }

    )

    encoded_jwt = jwt.encode(

        to_encode,

        SECRET_KEY,

        algorithm=ALGORITHM

    )

    return encoded_jwt


# =====================================================
# VERIFY TOKEN
# =====================================================

def verify_token(

    token: str

):

    """
    Decode JWT.

    Returns username.

    """

    try:

        payload = jwt.decode(

            token,

            SECRET_KEY,

            algorithms=[ALGORITHM]

        )

        username = payload.get("sub")

        if username is None:

            raise HTTPException(

                status_code=status.HTTP_401_UNAUTHORIZED,

                detail="Invalid Token"

            )

        return username

    except JWTError:

        raise HTTPException(

            status_code=status.HTTP_401_UNAUTHORIZED,

            detail="Invalid or Expired Token"

        )


# =====================================================
# CURRENT USER
# =====================================================

def get_current_user(

    token: str = Depends(oauth2_scheme),

    db: Session = Depends(get_db)

):

    """
    Returns logged-in user.

    """

    username = verify_token(token)

    service = UserService(db)

    user = service.get_user_by_username(

        username

    )

    if user is None:

        raise HTTPException(

            status_code=status.HTTP_401_UNAUTHORIZED,

            detail="User not found"

        )

    return user


# =====================================================
# ACTIVE USER
# =====================================================

def get_current_active_user(

    current_user: User = Depends(

        get_current_user

    )

):

    """
    Checks whether account is active.

    """

    if not current_user.is_active:

        raise HTTPException(

            status_code=400,

            detail="Inactive User"

        )

    return current_user


# =====================================================
# ADMIN ONLY
# =====================================================

def admin_required(

    current_user: User = Depends(

        get_current_active_user

    )

):

    """
    Admin Authorization

    """

    if current_user.role.lower() != "admin":

        raise HTTPException(

            status_code=403,

            detail="Admin privileges required"

        )

    return current_user


# =====================================================
# RESEARCHER OR ADMIN
# =====================================================

def researcher_required(

    current_user: User = Depends(

        get_current_active_user

    )

):

    """
    Researcher Authorization

    """

    if current_user.role.lower() not in [

        "researcher",

        "admin"

    ]:

        raise HTTPException(

            status_code=403,

            detail="Researcher access required"

        )

    return current_user
