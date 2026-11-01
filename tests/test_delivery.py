import pytest
from delivery import calculate_delivery

# 1. Обычная доставка (базовые и граничные значения)
@pytest.mark.parametrize("subtotal, expected", [
    (0, 300),
    (999, 300),
    (1000, 150),
    (4999, 150),
    (5000, 0),
    (10000, 0)
])
def test_regular_delivery(subtotal, expected):
    assert calculate_delivery(subtotal, express=False) == expected

# 2. Экспресс-доставка (та же матрица + 250 руб.)
@pytest.mark.parametrize("subtotal, expected", [
    (0, 550),
    (999, 550),
    (1000, 400),
    (4999, 400),
    (5000, 250),  # Важно: для заказов от 5000 экспресс стоит 250
    (10000, 250)
])
def test_express_delivery(subtotal, expected):
    assert calculate_delivery(subtotal, express=True) == expected

# 3. Ошибочные данные: отрицательная сумма
def test_negative_subtotal():
    with pytest.raises(ValueError):
        calculate_delivery(-1)

# 4. Ошибочные данные: некорректный тип subtotal (строка)
def test_invalid_subtotal_type():
    with pytest.raises(TypeError):
        calculate_delivery("500")

# 5. Ошибочные данные: некорректный тип subtotal (float)
def test_float_subtotal():
    with pytest.raises(TypeError):
        calculate_delivery(500.0)

# 6. Ошибочные данные: некорректный тип express
def test_invalid_express_type():
    with pytest.raises(TypeError):
        calculate_delivery(1000, express="yes")

# 7. Ошибочные данные: логическое значение вместо суммы заказа
def test_bool_subtotal():
    with pytest.raises(TypeError):
        calculate_delivery(True)