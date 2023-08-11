import socket
import os

def main() -> None:
    """
    Сравнивает соответствие доменных имен адресам, выводит предупреждение если адрес изменился.
    Данные для анализа берутся из файла config.txt, находящегося в папке со скриптом

    """
    configFile = os.path.join(os.path.dirname( __file__ ), "config.txt")
    
    print()

    with open(configFile, "r") as file:
        for line in file:

            # пропустить итерацию если не удалось распарсить строку из файла
            try:
                [name, old_addr] = line.split()
            except:
                continue

            try:
                current_addr = socket.gethostbyname(name)
                if current_addr == old_addr:
                    print(f'OK {name} [{current_addr}]')
                else:
                    print(f'!!! CHANGED !!! -- {name} [{old_addr} --> {current_addr}]')
            except:
                print(f'!!! Unable to get IP by Hostname !!! -- {name}')

    print()


if __name__ == '__main__':
    main()
