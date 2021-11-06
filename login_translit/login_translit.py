def transform(string: str) -> str:
    """
    Транформирует строку на кириллице в строку на латинице по правилам транслитерации

    иванов --> ivanov

    :param string: строка на криллице
    :return: строка на латинице
    """

    mapping = {
        'а': 'a',
        'б': 'b',
        'в': 'v',
        'г': 'g',
        'д': 'd',
        'е': 'e',
        'ё': 'e',
        'ж': 'zh',
        'з': 'z',
        'и': 'i',
        'й': 'y',
        'к': 'k',
        'л': 'l',
        'м': 'm',
        'н': 'n',
        'о': 'o',
        'п': 'p',
        'р': 'r',
        'с': 's',
        'т': 't',
        'у': 'u',
        'ф': 'f',
        'х': 'kh',
        'ц': 'ts',
        'ч': 'ch',
        'ш': 'sh',
        'щ': 'shch',
        'ъ': '',
        'ы': 'y',
        'ь': '',
        'э': 'e',
        'ю': 'yu',
        'я': 'ya'
    }

    result = ''

    # замены в строке особых случаев по правилам транслитерации
    string = string.replace('ье', 'ye')
    string = string.replace('ъе', 'ye')
    string = string.replace('ьё', 'ye')
    string = string.replace('ъё', 'ye')

    for char in string:
        # Если текущего симовла нет в таблице соответствий - символ переносится в исходном виде
        try:
            result += mapping[char]
        except KeyError:
            result += char

    return result


def translate_login(l_name: str, f_name: str, m_name: str) -> tuple:
    """
    Транформирует полную форму записи ФИО на кириллице в логин для корпоративной сети
    по правилам транслитерации. Логин генерируется в двух формах:
    основная - <первая буква имени>.<фамилия>
    дополнительная - <первая буква имени><первая буква отчества>.<фамилия>

    Иванов Иван Михайлович --> i.ivanov     (основная форма)
    Иванов Иван Михайлович --> im.ivanov    (дополнительная форма)

    :param l_name: Фамилия на кириллице
    :param f_name: Имя на кириллице
    :param m_name: Отчество на кириллице
    :return: Кортеж из двух форм логинов на латинице
    """

    l_name = transform(l_name.lower())
    f_name = transform(f_name.lower())
    m_name = transform(m_name.lower())

    form1 = f_name[0] + '.' + l_name
    form2 = f_name[0] + m_name[0] + '.' + l_name

    return form1, form2


if __name__ == '__main__':
    # last = input('Фамилиия: ')
    # first = input('Имя: ')
    # middle = input('Отчество: ')
    # print(translate_login(last, first, middle))

    print(translate_login('Козлов', 'Васисуалий', 'Петрович'))
    print(translate_login('Хъебонандинъ', 'Мустафа', 'Ибнрабинович'))
    print(translate_login('Щечежинский', 'Ыбнархам', 'Фьорбунарович'))
    print(translate_login('Пьензин', 'Потап', 'Фрунзиевич'))
    print(translate_login('Мокрошлепская-Суходрыщева', 'Юлианна', 'Эвелиновна'))
