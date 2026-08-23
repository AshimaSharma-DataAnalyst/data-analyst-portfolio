from sqlalchemy.orm import Session

from app.models.user import User
from app.models.auth_schemas import UserCreate

from app.security.password import (
    hash_password,
    verify_password
)

from app.utils.logger import logger


class UserService:
    """
    Handles all user-related database operations.

    Responsibilities:
    - Register users
    - Authenticate users
    - Find users
    - Change password
    - Activate/Deactivate users
    """

    def __init__(self, db: Session):
        self.db = db

    # =====================================================
    # CREATE USER
    # =====================================================

    def create_user(
        self,
        user_data: UserCreate
    ):

        try:

            existing_user = self.get_user_by_username(
                user_data.username
            )

            if existing_user:

                raise ValueError(
                    "Username already exists."
                )

            existing_email = self.get_user_by_email(
                user_data.email
            )

            if existing_email:

                raise ValueError(
                    "Email already exists."
                )

            hashed_password = hash_password(
                user_data.password
            )

            user = User(

                username=user_data.username,

                email=user_data.email,

                hashed_password=hashed_password,

                is_active=True,

                is_admin=False

            )

            self.db.add(user)

            self.db.commit()

            self.db.refresh(user)

            logger.info(
                f"Created user: {user.username}"
            )

            return user

        except Exception as e:

            self.db.rollback()

            logger.exception(e)

            raise

    # =====================================================
    # GET USER BY USERNAME
    # =====================================================

    def get_user_by_username(
        self,
        username: str
    ):

        return (

            self.db.query(User)

            .filter(

                User.username == username

            )

            .first()

        )

    # =====================================================
    # GET USER BY EMAIL
    # =====================================================

    def get_user_by_email(
        self,
        email: str
    ):

        return (

            self.db.query(User)

            .filter(

                User.email == email

            )

            .first()

        )

    # =====================================================
    # GET USER BY ID
    # =====================================================

    def get_user_by_id(
        self,
        user_id: int
    ):

        return (

            self.db.query(User)

            .filter(

                User.id == user_id

            )

            .first()

        )

    # =====================================================
    # AUTHENTICATE USER
    # =====================================================

    def authenticate_user(
        self,
        username: str,
        password: str
    ):

        user = self.get_user_by_username(
            username
        )

        if user is None:

            logger.warning(
                f"Login failed for username: {username}"
            )

            return None

        if not verify_password(
            password,
            user.hashed_password
        ):

            logger.warning(
                f"Invalid password for username: {username}"
            )

            return None

        if not user.is_active:

            logger.warning(
                f"Inactive user attempted login: {username}"
            )

            return None

        logger.success(
            f"User authenticated: {username}"
        )

        return user

    # =====================================================
    # CHANGE PASSWORD
    # =====================================================

    def change_password(
        self,
        user_id: int,
        new_password: str
    ):

        try:

            user = self.get_user_by_id(
                user_id
            )

            if user is None:

                return None

            user.hashed_password = hash_password(
                new_password
            )

            self.db.commit()

            self.db.refresh(user)

            logger.info(
                f"Password changed for {user.username}"
            )

            return user

        except Exception as e:

            self.db.rollback()

            logger.exception(e)

            raise

    # =====================================================
    # DEACTIVATE USER
    # =====================================================

    def deactivate_user(
        self,
        user_id: int
    ):

        try:

            user = self.get_user_by_id(
                user_id
            )

            if user is None:

                return None

            user.is_active = False

            self.db.commit()

            self.db.refresh(user)

            logger.info(
                f"User deactivated: {user.username}"
            )

            return user

        except Exception as e:

            self.db.rollback()

            logger.exception(e)

            raise

    # =====================================================
    # ACTIVATE USER
    # =====================================================

    def activate_user(
        self,
        user_id: int
    ):

        try:

            user = self.get_user_by_id(
                user_id
            )

            if user is None:

                return None

            user.is_active = True

            self.db.commit()

            self.db.refresh(user)

            logger.info(
                f"User activated: {user.username}"
            )

            return user

        except Exception as e:

            self.db.rollback()

            logger.exception(e)

            raise