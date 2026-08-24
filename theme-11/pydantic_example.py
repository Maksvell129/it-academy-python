from typing import Any, Self

from pydantic import BaseModel, EmailStr, PositiveInt, constr, Field, model_validator, field_validator, ValidationError


class User(BaseModel):
    name: str = Field(min_length=3, max_length=100)
    age: int = Field(ge=1, le=120)
    email: EmailStr
    roles: list[str] = Field(default=["user"])
    # phone: str = Field(pattern=r"^\+?1?\d{9,15}$")

    @field_validator("name")
    def validate_name(cls, value: Any) -> Self:
        print("Валидируем имя", value)

        return value


user = User(name='Max', age=120, email='some_email@gmail.com')
print(user.model_dump_json())