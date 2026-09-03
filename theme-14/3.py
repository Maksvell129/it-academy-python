



def transfer_money(balance_id_from, balance_id_to, amount):
    try:
        cursor.execute("отнимаем от первого")
        cursor.execute("добавляем второму")

        connection.commit()

    except Exception:
        connection.rollback()
        raise