from typing import NoReturn


def write_read_lines(text: str, filename: str) -> NoReturn:
    with open(filename, 'a+') as file:
        file.write(text + '\n')

    with open(filename, 'r') as file:
        lines = file.readlines()
        even_lines = [line.strip() for index, line in enumerate(lines) if index % 2 != 0]
        for line in even_lines:
            print(line)