# Дан список email-адресов: ['user@mail.ru', 'spammer@bot.com', 'admin@site.ru', 'reklama@bot.com'].
# Напишите цикл for, который перебирает эти адреса и отправляет им письма (выводит в консоль «Отправлено на {email}»).
# Однако, если в адресе содержится слово «bot», программа должна пропустить отправку для этого адреса и ничего не выводить.
# Вывести в конце список отловленных ботов.

emails = ['user@mail.ru', 'spammer@bot.com', 'admin@site.ru', 'reklama@bot.com', 'spammer@bot.com']
bots = set()

for email in emails:
    if "bot" in email:
        bots.add(email)
    else:
        print(f"Отправлено на {email}")


print(f"Bots: {", ".join(bots)}")


