import os

path = 'folder1/folder2/file.ext'

# проверяем существование файла
exists = os.path.isfile(path)

if exists:
    # получаем расширение файла
    _, extension = os.path.splitext(path)

    # выводим расширение
    print(extension)
else:
    print("ошибка получения доступа к файлу")
