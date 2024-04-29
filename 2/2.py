string = input("Введите строку: ")

string_lower = string.lower()

char_count = {}

for char in string_lower:
    if char == ' ':
        continue
    count = string_lower.count(char)
    char_count[char] = count

print("Словарь с количеством символов в строке:")
print(char_count)
