class EmailNotification:
    def send(self, message):
        print(f"Email: {message}")

class SMSNotification:
    def send(self, message):
        print(f"SMS: {message}")


def create_notification(notification_type):
    if notification_type == "email":
        return EmailNotification()

    if notification_type == "sms":
        return SMSNotification()

    raise ValueError("Неизвестный тип")



notification = create_notification("email")

notification.send("Привет!")
