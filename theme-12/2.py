class Counter:
    def __init__(self, max_value):
        self.current = 2
        self.max_value = max_value

    def __iter__(self):
        return self

    def __next__(self):
        if self.current > self.max_value:
            raise StopIteration

        value = self.current
        self.current += 2

        return value


counter = Counter(max_value=30)

for number in counter:
    print(number)
# print(next(counter))
# print(next(counter))
# print(next(counter))
