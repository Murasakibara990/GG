from jose import jwt, JWTError
from models import User
from datetime import datetime, timedelta
from fastapi import Depends, HTTPException
from fastapi.security.http import HTTPBearer

SECRET_KEY = 'secret_key'
ALGORITHM = 'HS256'
ACCESS_TOKEN_EXPIRE_MINUTES = 30


async def create_access_token(user: User) -> str:
    data = {'id': user.id}
    expire = datetime.now().astimezone() + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    data['exp'] = expire
    return jwt.encode(data, SECRET_KEY, algorithm=ALGORITHM)


async def get_current_user(token: str = Depends(HTTPBearer())):
    token = token.__dict__
    try:
        payload = jwt.decode(token['credentials'], SECRET_KEY, algorithms=[ALGORITHM])
        user = await User.get_or_none(id=payload['id'])
        if not user:
            raise HTTPException(status_code=403, detail="User not found")
        return user
    except JWTError:
        raise HTTPException(status_code=401, detail='Could not validate credentials',
                            headers={'WWW-Authenticate': 'Bearer'})
