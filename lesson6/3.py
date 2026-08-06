def sum_all_numbers(*args):
    # print(type(args),args)
    total = 0
    for number in args:
        total += number

    return total
#
#
# numbers = [int(n) for n in input("Введите числа: ").strip().split(" ")]
# print(f"Вы ввели числа: {numbers}")
#
# result = sum_all_numbers(*numbers)
#
# is_odd = result % 2 == 0
#
# print(f"Сумма ваших чисел: {result}")
# print(is_odd)



print(sum_all_numbers(1, 2, 3, True))
# print(sum_all_numbers(10, 20, 30, 40))
# print(sum_all_numbers(10, 20, 30, 40, 50, 60, 60, 60, 60, 60, 60, 60, 60, 60, 60, 60, 60, 60))



#
# def send_email(*mails):
#     for mail in mails:
#         print(f"Отправлено на {mail}")
#
#
# result = send_email('user@mail.ru', 'spammer@bot.com', 'admin@site.ru', 'reklama@bot.com', 'spammer@bot.com')
# print("результат", result)
# print(send_email('user@mail.ru'))
# print(send_email(10, 20, 30, 40, 123.312, [123, 31]))
