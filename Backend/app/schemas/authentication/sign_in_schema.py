from pydantic import BaseModel, EmailStr, AfterValidator
from typing import Annotated

# password policy 
SPECIAL_CHARS: set[str] = {
    "$",
    "@",
    "#",
    "%",
    "!",
    "^",
    "&",
    "*",
    "(",
    ")",
    "-",
    "_",
    "+",
    "=",
    "{",
    "}",
    "[",
    "]",
}

MIN_LENGTH: int = 5
MAX_LENGTH: int = 20
INCLUDES_SPECIAL_CHARS: bool = True
INCLUDES_UPPER_CASE: bool = True
INCLUDES_LOWER_CASE: bool = True
INCLUDES_NUMBERS: bool = True

# we will attempt to validate the password here
def validate_password(value: str) -> str:
    min_length = MIN_LENGTH
    max_length = MAX_LENGTH
    includes_special_chars = INCLUDES_SPECIAL_CHARS
    includes_lower_case = INCLUDES_LOWER_CASE
    includes_upper_case = INCLUDES_UPPER_CASE
    includes_numbers = INCLUDES_NUMBERS
    special_chars = SPECIAL_CHARS

    if len(value) < min_length or len(value) > max_length:
        raise ValueError("your password should be more than {} characters and not more than 20".format(min_length))
    
    if includes_numbers and not any(char.isdigit() for char in value):
        raise ValueError("password should have at least a number")
    
    if includes_upper_case and not any(char.isupper() for char in value):
        raise ValueError("password shoult have at least a capital letter")
    
    if includes_lower_case and not any(char.islower() for char in value):
        raise ValueError("password should have at least one lower case letter")
    
    if includes_special_chars and not any(char in special_chars for char in value):
        raise ValueError("password should have on spcial character")
    
    return value


class SignInSchema(BaseModel):

    email: EmailStr 
    password: Annotated[str, AfterValidator(validate_password)]
