def average_num(list_num: list) -> float:
    for ind, el in enumerate(list_num):
        if not isinstance(el, int | float):
            try:
                list_num[ind] = int(el)
            except:
                return "Bad request"
    return round(sum(list_num)/len(list_num), 2)



def test_average_num():
    # Тестирование с пустым списком
    assert average_num([]) == 0, "Тест 1 не пройден: Пустой список должен вернуть 0"

    # Тестирование с положительными целыми числами
    assert average_num([1, 2, 3, 4, 5]) == 3.0, "Тест 2 не пройден: Неправильное среднее значение для положительных целых чисел"

    # Тестирование с отрицательными числами
    assert average_num([-1, -2, -3, -4, -5]) == -3.0, "Тест 3 не пройден: Неправильное среднее значение для отрицательных чисел"

    # Тестирование с дробными числами
    assert average_num([1.5, 2.5, 3.5, 4.5, 5.5]) == 3.5, "Тест 4 не пройден: Неправильное среднее значение для дробных чисел"

    # Тестирование смешанных типов данных в списке (с преобразованием в int)
    assert average_num([1, 2, '3', 4, 5]) == 3.0, "Тест 5 не пройден: Неправильное среднее значение смешанных типов данных (преобразование в int)"

    # Тестирование смешанных типов данных в списке (с преобразованием в int) и некорректным значением
    assert average_num([1, 2, 'a', 4, 5]) == "Bad request", "Тест 6 не пройден: Некорректное значение должно вызвать ошибку"

    # Тестирование смешанных типов данных в списке (с преобразованием в float)
    assert average_num([1, 2, '3.5', 4, 5]) == 3.0, "Тест 7 не пройден: Неправильное среднее значение смешанных типов данных (преобразование в float)"

    # Тестирование смешанных типов данных в списке (с преобразованием в float) и некорректным значением
    assert average_num([1, 2, 'a.5', 4, 5]) == "Bad request", "Тест 8 не пройден: Некорректное значение должно вызвать ошибку"

    # Тестирование с плавающей точкой
    assert average_num([1.5, 2.5, 3.5, 4.5, 5.5]) == 3.5, "Тест 9 не пройден: Неправильное среднее значение для дробных чисел"

    # Тестирование с одним элементом
    assert average_num([5]) == 5.0, "Тест 10 не пройден: Неправильное среднее значение для списка с одним элементом"

test_average_num()