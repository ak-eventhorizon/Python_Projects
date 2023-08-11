import socket

def main() -> None:
    """
    Сравнивает соответствие доменных имен адресам, выводит предупреждение если адрес изменился.

    """

    hosts_diadoc = {
        'diadoc.kontur.ru':           				'46.17.200.242',
        'en-diadoc.kontur.ru':          			'46.17.200.242',
        'edoci.kontur.ru':           				'46.17.200.242',
        'ceodoc.kontur.ru':           				'46.17.200.242',
        'bezbumag.kontur.ru':          				'46.17.200.242',
        'connector.kontur.ru':         				'46.17.200.242',
        'claims.kontur.ru':           				'46.17.200.242',
        'akibank.kontur.ru':           				'46.17.200.242',
        'edo-life.ru':                 				'46.17.200.242',
        'edifactoring.ru':           				'46.17.200.242',
        'teledoc.pro':           					'91.227.34.31',
        'diadoc-connector-api.kontur.ru':   		'46.17.206.14',
        'diadoc-public-connector-api.kontur.ru':	'46.17.200.240',
        'diadoc-api.kontur.ru':          			'46.17.206.14',
    }

    print('\n ----- KONTUR DIADOC -----')

    for name, old_addr in hosts_diadoc.items():
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
