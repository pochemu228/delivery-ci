def calculate_delivery(subtotal, express=False):
    # Проверка типов: bool является подклассом int, поэтому проверяем строго
    if type(subtotal) is not int:
        raise TypeError("subtotal должен быть целым числом")
    if type(express) is not bool:
        raise TypeError("express должен быть логическим значением")
    
    # Проверка на отрицательное значение
    if subtotal < 0:
        raise ValueError("subtotal не может быть отрицательным")

    # Расчет базовой стоимости
    if subtotal < 1000:
        cost = 300
    elif 1000 <= subtotal <= 4999:
        cost = 150
    else: # от 5000
        cost = 0

    # Надбавка за экспресс-доставку
    if express:
        cost += 250

    return cost