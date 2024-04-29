number = int(input("Введите число: "))

# Инициализация переменных для сумм
sum_neg = 0
sum_pos = 0

print(f"Числа в интервале [-{number}, {number}]:")
for i in range(-number, number + 1):
    print(i, end=" ")

    if i < 0:
        sum_neg += i
    else:
        sum_pos += i


print("\nСумма отрицательных чисел:", sum_neg)
print("Сумма положительных чисел:", sum_pos)
