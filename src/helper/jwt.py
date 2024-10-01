from datetime import datetime, timedelta

import jwt

SECRET_KEY = 'keepitsecret'
ALROGITHM = 'HS256'
EXPIRED_TIME = 5 # 5 minutes

def encode(data: dict) -> str:
    data_cp = data.copy()
    data_cp.update({'exp': datetime.now() + timedelta(minutes=EXPIRED_TIME)})
    return jwt.encode(data_cp, SECRET_KEY, algorithm=ALROGITHM)

def decode(token: str) -> dict:
    return jwt.decode(token, SECRET_KEY, algorithms=[ALROGITHM])
