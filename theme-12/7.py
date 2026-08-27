def generate_numbers():
    yield 1
    yield 2

def generate_all():
    yield from generate_numbers()
    yield 3
    yield 4


for number in generate_all():
    print(number)

