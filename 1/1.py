while True:
    a = input("Введите число или exit: ")

    if a.lower() == 'exit':
        print("Exit!")
        break

    if not a.isnumeric():
        print("Введено не число.")
        continue

    print("Длина числа: ", len(a))