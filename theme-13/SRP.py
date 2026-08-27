class Report:
    def generate(self):
        print("Создание отчёта")

    def save_to_file(self):
        print("Сохранение отчёта")

    def send_email(self):
        print("Отправка отчёта")


class Report:
    def generate(self):
        print("Создание отчёта")


class ReportSaver:
    def save(self, report):
        print("Сохранение отчёта")


class ReportSender:
    def send(self, report):
        print("Отправка отчёта")
