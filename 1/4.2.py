name = input("Введите ваше имя: ")
second_name = input("Введите вашу фамилию: ")
age = input("Введите ваш возраст: ")

format_output = "Ваше имя: {}, Фамилия: {}, Возраст: {} лет.".format(name, second_name, age)
f_string_output = f"Ваше имя: {name}, Фамилия: {second_name}, Возраст: {age} лет."

print("Format string: ", format_output)
print("f-string: ", f_string_output)
