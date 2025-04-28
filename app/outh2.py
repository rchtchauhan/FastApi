from jose import JWTError, jwt
from datetime import datetime, timedelta
from . import schema
from fastapi import Depends, status, HTTPException
from fastapi.security import OAuth2PasswordBearer
from .config import Settings
outh2_scheme = OAuth2PasswordBearer(tokenUrl='login')
#ALGORITHMS
#Expireation time

SECRET_KEY = '95u2hhggg2ovi2j292u205u295259258205252vjgjgiwjjjjIJFIJ'
ALGORITHM = 'HS256'
ACCESS_TOKEN_EXPIRE_TIME = 60

# to create token we need three things ---> what we will encode, secretkey , algorithms

def create_access_token(data:dict):
    to_encode = data.copy()

    expire = datetime.utcnow() + timedelta(minutes = ACCESS_TOKEN_EXPIRE_TIME)
    to_encode.update({"exp":expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, ALGORITHM)          #this will return token
    return encoded_jwt

def verify_access_token(token:str,credentials_expection):
    try:
        payload  = jwt.decode(token,SECRET_KEY, algorithms=[ALGORITHM])
        id:str = payload.get('user_id')
        if id is None:
            raise credentials_expection
        token_data = schema.TokenData(id=id)
    except JWTError :
        raise credentials_expection

    return token_data


def get_current_user(token:str = Depends(outh2_scheme)):
    credential_exception = HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail= ("Couldnt validate the "
                                         "credtials"), headers={'WWW-Authenticate': "Bearer"})
    
    return verify_access_token(token, credential_exception)

