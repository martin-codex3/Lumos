import jwt
from datetime import timedelta, datetime
import uuid
from app.core.config import Config
import logging

def create_jwt_token(user_data: dict, exp: timedelta = None, refresh: bool = False) -> str: # type: ignore
    payload = { # type: ignore
        "user": user_data, 
        "exp": datetime.now() + (exp if exp is not None else timedelta(minutes=60)),
        "refresh": refresh,
        "jti": uuid.uuid4()
    }

    # we will create the token here 
    jwt_token = jwt.encode(payload = payload, key = Config.JWT_KEY) # type: ignore
    return jwt_token

# we will decode the token here 
def decode_jwt_token(token: str):

    try:
        decoded_token = jwt.decode(
            jwt = token,
            key = Config.JWT_KEY,
            algorithms = [Config.JWT_ALGORITHM]
        )
        return decoded_token
    except jwt.PyJWTError as error:
        logging.exception(error)
        return None
    
    except Exception as error:
        logging.exception(error)
        return None

