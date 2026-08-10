from pydantic import EmailStr

TOTAL_RESET_PASS_COUNT = 0

def get_user(email: EmailStr) -> dict:
    users = {
        "email1@mail.ru": {"name": "Alex"},
        "email2@mail.ru": {"name": "Ann"},
        "email3@mail.ru": {"name": "Kate"},
    }

    print(f"Ищем пользователя с email = {email}")

    find_user = users[email]

    return find_user


def send_warning(email: EmailStr) -> None:
    print(f"Осторожно, кто-то пытается использовать вашу почту {email}")


def reset_password(email: EmailStr) -> dict | None:
    global TOTAL_RESET_PASS_COUNT

    try:
        user = get_user(email)
    except KeyError:
        send_warning(email)
    else:
        print(f"Логика по ресету пароля для {user}")
    finally:
        TOTAL_RESET_PASS_COUNT += 1


for _ in range(3):
    email = input("Введите email: ")
    reset_password(email)

print(f"{TOTAL_RESET_PASS_COUNT=}")