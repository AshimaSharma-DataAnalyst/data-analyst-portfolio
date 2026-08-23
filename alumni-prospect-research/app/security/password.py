from passlib.context import CryptContext


# =====================================================
# PASSWORD HASHING CONFIGURATION
# =====================================================

"""
This module is responsible for:

1. Hashing passwords before saving them
2. Verifying passwords during login

Passwords are NEVER stored as plain text.
"""


pwd_context = CryptContext(

    schemes=["bcrypt"],

    deprecated="auto"

)


# =====================================================
# HASH PASSWORD
# =====================================================

def hash_password(password: str) -> str:
    """
    Convert a plain password into a secure bcrypt hash.

    Example:

    Password:
        Password123

    Stored in Database:
        $2b$12$fjKls98jk....
    """

    return pwd_context.hash(password)


# =====================================================
# VERIFY PASSWORD
# =====================================================

def verify_password(

    plain_password: str,

    hashed_password: str

) -> bool:
    """
    Compare a plain password with the stored hash.

    Returns:
        True  -> Password is correct
        False -> Password is incorrect
    """

    return pwd_context.verify(

        plain_password,

        hashed_password

    )
