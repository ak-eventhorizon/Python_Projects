import os
import time
from zipfile import ZipFile


def main():

    # каталоги, подлежащие архивации
    sources = ['./source1', './source2']
    # корневой каталог для бэкапов
    bkp_directory = './backup'

    # имя каталога для очередного бэкапа = корневой каталог + системный разделитель + подкаталог формата YYYY_MM_DD
    today_dir = bkp_directory + os.sep + time.strftime('%Y_%m_%d')

    # текущее время служит именем zip-архива, который будет расположен в сегодняшнем каталоге с бэкапами
    target = today_dir + os.sep + time.strftime('%H_%M_%S') + '.zip'

    # если сегодняшнего каталога еще нет - создаем его
    if not os.path.exists(today_dir):
        os.mkdir(today_dir)
        print(f'Directory created: {today_dir}')

    # определение всех файлов в директории рекурсивно (включая подпапки)
    def retrieve_file_paths(directory):
        file_paths = list()

        for root, directories, filenames in os.walk(directory):
            for filename in filenames:
                file_path = os.path.join(root, filename)
                file_paths.append(file_path)
        return file_paths

    # создание архива из указанных источников с помощью модуля zipfile
    current_zipfile = ZipFile(target, mode='a')
    for source in sources:
        files = retrieve_file_paths(source)
        for file in files:
            current_zipfile.write(file)
    current_zipfile.close()

    print(f'Backup created: {target}')


if __name__ == '__main__':
    main()
