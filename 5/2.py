import os
import datetime


current_date = datetime.datetime.now().strftime("%Y-%m-%d")


directory_path = os.path.join(os.getcwd(), current_date)
os.mkdir(directory_path)


file_path = os.path.join(directory_path, "example.txt")
with open(file_path, "w") as file:
    pass


sub_directory_path = os.path.join(directory_path, "subdirectory")
os.mkdir(sub_directory_path)


new_file_path = os.path.join(sub_directory_path, "example.txt")
os.rename(file_path, new_file_path)

print(f"Директория с текущей датой создана: {directory_path}")
print(f"Файл успешно перемещён в директорию: {new_file_path}")
