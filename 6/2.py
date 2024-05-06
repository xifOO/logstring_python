import pytest
import os
from tempfile import TemporaryDirectory


def merge_and_write(file1_path, file2_path, output_file_path):
    try:
        with open(file1_path, 'r') as file1:
            data1 = file1.read().strip()

        with open(file2_path, 'r') as file2:
            data2 = file2.read().strip()

        merged_data = data1 + ' ' + data2

        with open(output_file_path, 'w') as output_file:
            output_file.write(merged_data)

        with open(output_file_path, 'r') as output_file:
            data = output_file.read()
        return data
    except FileNotFoundError:
        return "Один из файлов не найден"


@pytest.fixture
def create_files():
    # Создание временной директории
    with TemporaryDirectory() as temp_dir:
        file1_path = os.path.join(temp_dir, 'file1.txt')
        file2_path = os.path.join(temp_dir, 'file2.txt')
        output_file_path = os.path.join(temp_dir, 'output.txt')

        with open(file1_path, 'w') as file1:
            file1.write('Data from file 1')

        with open(file2_path, 'w') as file2:
            file2.write('Data from file 2')

        yield file1_path, file2_path, output_file_path

def test_merge_and_write(create_files):
    file1_path, file2_path, output_file_path = create_files

    result = merge_and_write(file1_path, file2_path, output_file_path)

    # Проверяем, что файл output.txt был создан и содержит ожидаемые данные
    assert os.path.exists(output_file_path)
    assert result == 'Data from file 1 Data from file 2'

def test_merge_and_write_file_not_found():
    # Пытаемся объединить и записать данные из несуществующего файла
    file1_path = 'nonexistent_file.txt'
    file2_path = 'file2.txt'  # Нужен любой существующий файл
    output_file_path = 'output.txt'

    result = merge_and_write(file1_path, file2_path, output_file_path)

    assert result == "Один из файлов не найден"
