# Создаем пользовательские исключения, наследуя их от класса Exception
class InvalidDataException(Exception):
    pass


class ProcessingException(Exception):
    pass


# Функция, которая генерирует различные исключения в зависимости от аргументов
def process_data(data):
    if not isinstance(data, int):
        raise InvalidDataException("Недопустимый тип данных. Ожидается целое число.")

    if data < 0:
        raise ProcessingException("Обнаружено отрицательное число.")

    return data * 2


# Функция, вызывающая process_data и обрабатывающая исключения
def main_function(input_data):
    try:
        result = process_data(input_data)
        print("Результат:", result)
    except InvalidDataException as e:
        print("Ошибка с недопустимыми данными:", e)
        raise
    except ProcessingException as e:
        print("Ошибка обработки:", e)
        raise


# Вызовем функцию main_function с разными данными
try:
    main_function(25)
    main_function("test")
    main_function(-6)
except Exception as e:
    print("Необработанное исключение, обнаруженное в основной программе:", e)