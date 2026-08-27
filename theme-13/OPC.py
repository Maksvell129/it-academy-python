def pay(payment_type, amount):
    if payment_type == "card":
        print("Оплата картой")
    elif payment_type == "cash":
        print("Оплата наличными")
    elif payment_type == "crypto":
        print("Оплата криптовалютой")


class CardPayment:
    def pay(self, amount):
        print("Оплата картой")


class CashPayment:
    def pay(self, amount):
        print("Оплата наличными")


def process_payment(payment, amount):
    payment.pay(amount)
