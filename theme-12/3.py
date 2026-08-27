numbers = [1, 2, 3]

iterator = iter(numbers)

print(next(iterator))
print(next(iterator))

print("До цикла")

for number in iterator:
    print(number)

print(next(iterator))
