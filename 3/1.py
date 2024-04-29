def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        raise ValueError("Division by zero is not allowed")
    return x / y

def power(x, y):
    return x ** y

def run_calculator():
    while True:
        print("\nВыберите операцию:")
        print("1. Сложение")
        print("2. Вычитание")
        print("3. Умножение")
        print("4. Деление")
        print("5. Возведение в степень")
        print("6. Выход")

        choice = input("Введите номер операции: ")

        if choice not in ('1', '2', '3', '4', '5', '6'):
            print("Некорректный ввод. Пожалуйста, введите число от 1 до 6.")
            continue

        if choice == '6':
            print("Выход из программы.")
            break

        try:
            num1 = float(input("Введите первое число: "))
            num2 = float(input("Введите второе число: "))
        except ValueError:
            print("Некорректный ввод числа.")
            continue

        if choice == '1':
            print("Результат:", add(num1, num2))
        elif choice == '2':
            print("Результат:", subtract(num1, num2))
        elif choice == '3':
            print("Результат:", multiply(num1, num2))
        elif choice == '4':
            try:
                print("Результат:", divide(num1, num2))
            except ValueError as e:
                print("Ошибка:", e)
        elif choice == '5':
            print("Результат:", power(num1, num2))

run_calculator()
