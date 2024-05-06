import random


random_number = random.randint(1, 100)


if random_number % 2 == 0:
    print(f"Чётное число {random_number}!")
else:
    print(f"Нечётное число {random_number}!")
