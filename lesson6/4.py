def another_func(year):
    if year>2020:
        print("Актуален")
    else:
        print("Устарел")


def save_device_info(**kwargs):
    print(type(kwargs), kwargs)
    for key, value in kwargs.items():
        print(f"Характеристика [{key}]: {value}")


    another_func(year=kwargs["year"])


save_device_info(brand="Apple", model="iPhone 15", ram="8GB", year=2024, country="USA", city="LA", memory=[128, 256, 512])
