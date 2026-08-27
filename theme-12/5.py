
def get_numbers2():
    return [1, 2, 3]



def numbers():
    print("Начало")

    yield 1

    print("После первого yield")

    yield 2

    print("Конец")


generator = numbers()

print(next(generator))
print(next(generator))
