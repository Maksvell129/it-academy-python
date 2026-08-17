from pydantic import EmailStr, BaseModel
from email_validator import validate_email



print(validate_email('contact@mailcom'))