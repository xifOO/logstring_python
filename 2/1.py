numbers_input = input("Введите список чисел через пробел: ").split()
power_input = int(input("Введите степень: "))

try:
    numbers = [int(num) if '.' not in num else float(num) for num in numbers_input]
except ValueError:
    numbers = numbers_input

result = []
for num in numbers:
    if isinstance(num, str):
        result.append(num * power_input)
    else:
        result.append(num ** power_input)

print("Числа в степени {}: {}".format(power_input, result))
