try:
    with open("data.txt", encoding="utf-8") as file:
        data = file.read()

except FileNotFoundError:
    print("Файл не найден")

except UnicodeDecodeError:
    print("Не удалось прочитать файл")

