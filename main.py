def is_prime(number):
    inx = 0
    i = 1
    while i <= number:
        if number % i == 0:
            inx += 1
        i += 1
    if inx == 2:
        return True
    else:
        return False


def divide(x, y):
    try:
        result = x / y
    except ZeroDivisionError:
        print("Ошибка: деление на ноль!")
    else:
        print("Результат: ", result)
    finally:
        print("Выполнение блока finally")


def matrx(matrix):
    for i, row in enumerate(matrix):
        if all(item > 0 for item in row):
            return i, sum(row)
    return None


def process_data(data):
    if isinstance(data, list):
        return sum(data)
    elif isinstance(data, dict):
        return sorted(data.values(), reverse=True)[:3]
    elif isinstance(data, int):
        return sum(int(digit) for digit in str(data))
    elif isinstance(data, str):
        return len(data.split())
    else:
        return "Неизвестный тип данных"


if __name__ == "__main__":
    while True:
        print("Главное меню:")
        print("1. Определение простого числа: ")
        print("2. Найти первую строку матрицы все эдементы которой положительны")
        print("3. Матрица")
        print("4. Реализация работы try/except/finally")
        print("5. Введите n для выхода")
        ind = input("Ваш выбор: ")
        if ind == "1":
            while True:
                chislo_input = input("Введите число: ")
                try:
                    chislo = int(chislo_input)
                    if chislo <= -1:
                        print("Промежуток задан от 0 до 1000")
                    elif 0 <= chislo <= 1000:
                        print(is_prime(chislo))
                        break
                    else:
                        print("Введенное число не находится в промежутке от 0 до 1000")
                except ValueError:
                    print("Введите корректное целое число!")
        elif ind == "2":
            print(process_data([1, 2, 3]))
            print(process_data({"a": 1, "b": 2, "c": 3, "d": 4}))
            print(process_data(123))
            print(process_data("Ехал реку через реку в реке рак"))
        elif ind == "3":
            matrix = [[12, -7, 87], [-4, 55, 67], [7, 8, 9]]
            result = matrx(matrix)
            if result:
                print(f"Первая строка с положительными элементами: {result[0] + 1}, сумма элементов: {result[1]}")
            else:
                print("Строка с положительными элементами не найдена")
        elif ind == "4":
            divide(5, 6)
        elif ind == "n":
            break
        else:
            print("Неконкретный ввод данных")