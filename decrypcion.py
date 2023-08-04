import pyAesCrypt
import os


# функция дешифрования файла
def decryption(file, password):

    # задаём размер буфера
    buffer_size = 512 * 1024

    # вызываем метод дешифровки
    pyAesCrypt.decryptFile(
        str (file),
        str (os.path.splitext(file)[0]),
        password,
        buffer_size
    )

    # чтобы видеть результат выводим на печать имя зашифрованого файла
    print("[Файл '" + str(os.path.splitext(file)[0]) + "' дешифрован]")

    # удоляем исходнй файл
    os.remove(file)

# функция сконирования деректория
def walking_by_dirs(dir, password):

    for name in  os.listdir(dir):
        path = os.path.join(dir, name)

        # если находим файл то дешифруем его
        if os.path.isfile(path):
            try:
                decryption(path, password)
            except Exception as ex:
                print(ex)
        # если находи деректорий то повторяем цикл по поиску файлов
        else:
            walking_by_dirs(path, password)

password = input("введите пароль для расшифровки: ")
walking_by_dirs("/home/larioncrab", password)