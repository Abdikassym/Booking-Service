
from datetime import datetime
import jwt
from jose import JWTError
from fastapi import Depends, Request
from app.config import settings
from app.exceptions import IncorrectTokenFormatException, TokenAbsentException, TokenExpiredException, UserIsNotAdminHiddenException, UserNotExistsHiddenException
from app.users.dao import UsersDAO
from app.users.models import Users

def get_token(request: Request):
    token = request.cookies.get("booking_access_token")
    if not token:
        raise TokenAbsentException
    return token


async def get_current_user(token: str = Depends(get_token)):
    try:
        payload = jwt.decode(
            token, settings.SECRET_KEY, settings.ALGORITHM
            )
    except JWTError:
        raise IncorrectTokenFormatException
    expire: str = payload.get("exp")

    if (not expire) or (int(expire) < datetime.utcnow().timestamp()):  
        raise TokenExpiredException
    user_id: str = payload.get("sub")
    
    
    if not user_id:
        raise UserNotExistsHiddenException
    user = await UsersDAO.find_by_id(int(user_id))
    
    
    if not user:
        raise UserNotExistsHiddenException
    return user



async def get_current_admin_user(current_user: Users = Depends(get_current_user)):
    # if current_user.role != "admin":
    #     raise UserIsNotAdminHiddenException
    return current_user