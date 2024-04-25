def string_to_int(s):
    try:
        return int(s)
    except ValueError:
        print("Ошибка: Невозможно преобразовать строку в целое число.")
        return None


def read_file(filename):
    try:
        with open(filename, 'r') as file:
            return file.read()
    except (FileNotFoundError, IOError) as e:
        print(f"Ошибка при чтении файла: {e}")
        return None


def divide_numbers(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        print("Ошибка: Деление на ноль.")
        return None
    except TypeError:
        print("Ошибка: Неверный тип данных для операции деления.")
        return None


def access_list_element(lst, index):
    try:
        return lst[index]
    except (IndexError, TypeError) as e:
        print(f"Ошибка при доступе к элементу списка: {e}")
        return None
