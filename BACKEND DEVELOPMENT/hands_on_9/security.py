from datetime import datetime, timedelta, timezone

from jose import jwt
from passlib.context import CryptContext

#below imports -> for jwt validation function
from fastapi import Depends, HTTPException
from fastapi.security import OAuth2PasswordBearer
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from database import get_db
from models import User


# PASSWORD HASHING

# bcrypt is preferred over MD5 and SHA-256 because:
# - It is intentionally slow, making brute-force attacks difficult.
# - It automatically generates a unique salt for every password.
# - MD5 and SHA-256 are fast hashing algorithms and are not
#   recommended for storing passwords.

pwd_context = CryptContext(
    schemes=["bcrypt"],
    deprecated="auto"
)


def get_password_hash(password: str) -> str:
    """
    Hash a plain-text password using bcrypt.
    """
    return pwd_context.hash(password)


def verify_password(password: str, hashed_password: str) -> bool:
    """
    Verify that the entered password matches the stored bcrypt hash.
    """
    return pwd_context.verify(password, hashed_password)


#JWT CONFIGURATION

#In production, store this in an environment variable (.env)
SECRET_KEY = "cognizant_dn_saveetha"

ALGORITHM = "HS256"

ACCESS_TOKEN_EXPIRE_MINUTES = 30


#JWT TOKEN CREATION

def create_access_token(data: dict) -> str:
    
    #Create a JWT access token that expires in 30 minutes.
    

    to_encode = data.copy()

    expire = datetime.now(timezone.utc) + timedelta(
        minutes=ACCESS_TOKEN_EXPIRE_MINUTES
    )

    to_encode.update({"exp": expire})

    token = jwt.encode(
        to_encode,
        SECRET_KEY,
        algorithm=ALGORITHM
    )

    return token



# JWT VALIDATION
#dependency

oauth2_scheme = OAuth2PasswordBearer(
    tokenUrl="/api/v1/auth/login"
)


async def get_current_user(
    token: str = Depends(oauth2_scheme),
    db: AsyncSession = Depends(get_db)
):

    try:
        payload = jwt.decode(
            token,
            SECRET_KEY,
            algorithms=[ALGORITHM]
        )

        email = payload.get("sub")

        if email is None:
            raise HTTPException(
                status_code=401,
                detail="Invalid token"
            )

    except:
        raise HTTPException(
            status_code=401,
            detail="Invalid or expired token"
        )

    result = await db.execute(
        select(User).where(User.email == email)
    )

    current_user = result.scalar_one_or_none()

    if current_user is None:
        raise HTTPException(
            status_code=401,
            detail="User not found"
        )

    return current_user


"""
OAuth2 Authorization Code Flow:
In OAuth2 authorization code flow, the user authenticates with an
authorization server (like Google or Microsoft). The application
receives an authorization code and exchanges it for an access token.

Our implementation is different:
The user directly sends email and password to our API.
The API verifies credentials and generates a JWT token.
No external authorization server or authorization code is involved.
"""
