password = input("Введите пароль: ")

keywords = ["123", "password"]

if len(password) < 8:
    print("Пароль слишком короткий")
elif any([word in password for word in keywords]):
    print("Пароль слишком простой и ненадежный")
else:
    print("Пароль принят")



