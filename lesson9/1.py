def calculate_vat(amount: float, rate: float = 20.0) -> float:
    """Вычисляет сумму НДС для заданной стоимости.

    Args:
        amount (float): Базовая стоимость товара/услуги.
        rate (float, optional): Ставка НДС в процентах. По умолчанию 20.0.

    Returns:
        float: Рассчитанная сумма НДС.
    """
    return amount * (rate / 100)

print(calculate_vat.__doc__)
