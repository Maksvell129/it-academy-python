def generate_numbers(limit):
    for number in range(limit):
        yield number


# for number in generate_numbers(5):
#     print(number)


numbers_1 = [x for x in range(1_000_000)]
print(numbers_1[10000])

numbers_2 = (x for x in range(1_000_000))
print(next(numbers_2))

