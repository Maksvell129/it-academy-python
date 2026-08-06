from pydantic import NonNegativeInt, NegativeInt, PositiveInt, PositiveFloat

def multiply_string(text: str, count: PositiveInt) -> str:
    """Умножает строку на число
    """
    return text * count




count: int = -10
text: str = "text"

print(multiply_string(text, count))