# С помощью Dict Comprehension создайте словарь, где ключом будет название товара,
# а значением — его цена с учетом скидки 20% (умножить на 0.8), если исходная цена больше 1000:

catalog = {"Phone": 1200, "Case": 150, "Tablet": 800, "Laptop": 2000}

new_catalog = {(value*0.8 if value > 1000 else value): f"На скидке {key}"  for key, value in catalog.items()}

print(new_catalog)