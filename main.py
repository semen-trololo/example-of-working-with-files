import os

# Получения списка файлов и папок
files_dir = os.listdir('test')
print(files_dir)

only_files = []
for i in files_dir:
    if os.path.isfile('test\\'+i):
        only_files.append(i)

only_dir = []
for i in files_dir:
    # \\ for Windows
    if os.path.isdir('test\\'+i):
        only_dir.append(i)

print('-'*15)
print(only_files) # prints all files
print('-'*15)
print(only_dir) # prints all directories

# Переименовать файлы
for index, file_name in enumerate(only_files):
    if index % 2 == 0:
        os.rename('test\\'+file_name, 'test\\'+'Even-'+file_name)
    else:
        os.rename('test\\'+file_name, 'test\\'+'Odd-'+file_name)

# Перемещение файла.
os.rename('test\\'+'Even-123.xlsx', 'test\\'+'iii\\'+'Even-123.xlsx')

# Удаление файла
os.remove('test\\1.txt')

# Работа с файлом

with open('blogs/1.txt', 'r', encoding="UTF-8") as file:
    data = file.read()
    print(data)

"""
r	чтение
w	запись
a	добавление в файл
r+	Чтение и запись данных в файл. Предыдущие данные в файле не удаляются.
w+	Запись и чтение данных. Существующие данные перезаписываются.
a+	Добавление и чтение данных из файла. Существующие данные не перезаписываются.

"""
