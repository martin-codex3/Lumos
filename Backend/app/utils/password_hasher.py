from passlib.context import CryptContext

my_context = CryptContext(schemes=["argon2"])

# we will hash the password here 
def hash_user_password(password: str) -> str:
    password_hash = my_context.hash(password)
    return password_hash

# we will verify the hashed password here 
def verify_hashed_password(user_password: str, hashed_password: str) -> bool:
    verified_password = my_context.verify(user_password, hash = hashed_password)
    if verified_password:
        return True
    else:
        return False
