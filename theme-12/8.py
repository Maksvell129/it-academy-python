import time
import random

raw_network_pings = [i for i in range(1, 100000000)]

print("Закончена генерация: ")
pings_gen = (ping for ping in raw_network_pings if ping > 100)
pings = [ping for ping in raw_network_pings if ping > 100]

print("Запуск по списку: ")

t1 = time.time()
for anomaly in pings:
    # print(f"Обнаружен опасный пинг: {anomaly}")
    pass

print(f"Резульат по списку: {time.time() - t1}"  )

print("Запуск по генератору: ")
t2 = time.time()
for anomaly in pings:
    # print(f"Обнаружен опасный пинг: {anomaly}")
    pass

print(f"Резульат по генератопу: {time.time() - t2}")