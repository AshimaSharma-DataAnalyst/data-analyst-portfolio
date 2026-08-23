from datetime import timedelta

from fastapi import APIRouter
from fastapi import Depends
from fastapi import HTTPException
from fastapi import status

from fastapi.security import OAuth2PasswordRequestForm

from sqlalchemy.orm import Session

from app.database.database import get_db

from app.models.auth_schemas import (
    UserCreate,
    UserResponse,
    Token
)

from app.security.jwt_handler import (
    create_access_token,
    get_current_active_user
)

from app.config.settings import settings

from app.services.user_service import UserService

from app.utils.logger import logger


router = APIRouter(
    prefix="/auth",
    tags=["Authentication"]
)


# =====================================================
# REGISTER USER
# =====================================================

@router.post(
    "/register",
    response_model=UserResponse,
    status_code=status.HTTP_201_CREATED,
    summary="Register a new user"
)
def register_user(
    user: UserCreate,
    db: Session = Depends(get_db)
):
    """
    Register a new application user.

    - Username must be unique.
    - Email must be unique.
    - Password will be securely hashed.
    """

    service = UserService(db)

    try:

        new_user = service.create_user(user)

        logger.info(
            f"New user registered: {new_user.username}"
        )

        return new_user

    except ValueError as e:

        logger.warning(str(e))

        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=str(e)
        )


# =====================================================
# LOGIN
# =====================================================

@router.post(
    "/login",
    response_model=Token,
    summary="Login and receive JWT token"
)
def login(
    form_data: OAuth2PasswordRequestForm = Depends(),
    db: Session = Depends(get_db)
):
    """
    Authenticate user and generate JWT access token.

    Swagger Login:

    Username:
        admin

    Password:
        admin123
    """

    service = UserService(db)

    user = service.authenticate_user(

        form_data.username,

        form_data.password

    )

    if user is None:

        logger.warning(
            f"Failed login attempt: {form_data.username}"
        )

        raise HTTPException(

            status_code=status.HTTP_401_UNAUTHORIZED,

            detail="Invalid username or password",

            headers={
                "WWW-Authenticate": "Bearer"
            }

        )

    access_token = create_access_token(

        data={
            "sub": user.username
        },

        expires_delta=timedelta(

            minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES

        )

    )

    logger.success(
        f"User logged in: {user.username}"
    )

    return {

        "access_token": access_token,

        "token_type": "bearer"

    }


# =====================================================
# CURRENT USER
# =====================================================

@router.get(
    "/me",
    response_model=UserResponse,
    summary="Get current logged-in user"
)
def get_me(
    current_user=Depends(get_current_active_user)
):
    """
    Returns the currently authenticated user.
    """

    logger.info(
        f"Profile requested by {current_user.username}"
    )

    return current_user


# =====================================================
# VERIFY TOKEN
# =====================================================

@router.get(
    "/verify",
    summary="Verify JWT Token"
)
def verify_token(
    current_user=Depends(get_current_active_user)
):
    """
    Verify whether a JWT token is valid.

    Useful for frontend applications.
    """

    return {

        "authenticated": True,

        "username": current_user.username,

        "message": "Token is valid."

    }