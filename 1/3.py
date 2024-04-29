number = input("Введите трехзначное число с различными цифрами: ")

if len(number) != 3 or len(set(number)) != 3:
    print("Введено не трехзначное число или в числе есть повторяющиеся цифры.")
else:
    for a in number:
        for b in number:
            for c in number:
                if a != b and b != c and a != c: 
                    print(a + b + c, end=" ")
