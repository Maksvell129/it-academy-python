
class MessageSender:
    def send(self, message):
        print(f"Отправка: {message}")


class LoggingSender:
    def __init__(self, sender):
        self.sender = sender

    def send(self, message):
        print("Логирование отправки")
        self.sender.send(message)


class RetrySender:
    def __init__(self, sender, number):
        self.sender = sender
        self.number = number

    def send(self, message):
        print("Несколько раз")
        for _ in range(self.number):
            self.sender.send(message)



first_sender = MessageSender()

logging_sender = LoggingSender(first_sender)

retry_sender = RetrySender(logging_sender, 3)

retry_sender.send("Привет!")
