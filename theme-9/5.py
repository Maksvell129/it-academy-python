try:
    number = int("abc")
except ValueError as e:
    error_text = str(e)
    print("Произошла ошибка" + error_text)
    raise e
