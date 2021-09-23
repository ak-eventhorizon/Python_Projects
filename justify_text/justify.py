def justify(text: str, width: int) -> str:
    """
    Justifies text with defined width.

    :param text: text string
    :param width: justifying width
    :return: string

    1) Use spaces to fill in the gaps between words.
    2) Each line should contain as many words as possible.
    3) Use '\n' to separate lines.
    4) Gap between words can't differ by more than one space.
    5) Lines should end with a word not a space.
    6) '\n' is not included in the length of a line.
    7) Large gaps go first, then smaller ones ('Lorem--ipsum--dolor--sit-amet,' (2, 2, 2, 1 spaces)).
    8) Last line should not be justified, use only one space between words.
    9) Last line should not contain '\n'
    10) Strings with one word do not need gaps ('somelongword\n').
    """

    words = text.split()
    strings = list()
    string = list()
    result = ''

    # разбиение исходной строки на списки, длина слов (с пробелами) в каждом из которых,
    # не превышает заданной ширины строки (width)
    for word in words:
        string += [word]
        if len(' '.join(string)) > width:
            strings.append(string[:-1])
            string = [word]
    strings.append(string)

    # добавление в каждую из строк пробелов до требуемой ширины строки
    # добавление последовательное, чтобы соседние пробелы не различались более чем на один
    # к последнему слову в строке и к последней строке - пробелы не добавляются
    # 'Lorem--ipsum--dolor--sit-amet,' (2, 2, 2, 1 spaces)
    for string in strings:
        needed_spaces = width - len(' '.join(string))

        # Если строка последняя - не производить с ней действий
        if string is strings[-1]:
            break

        while needed_spaces != 0:
            # перебор слов в строке
            for i in range(len(string)):
                # если строка состоит из одного слова, пробелов добавлять не требуется
                if len(string) == 1:
                    needed_spaces = 0
                    break
                # если слово последнее в строке, дополнять пробелами его не требуется
                if string[i] == string[-1]:
                    break
                # если дополнительных пробелов больше не требуется
                if needed_spaces == 0:
                    break

                string[i] += ' '
                needed_spaces -= 1

    # соединение всех списков со строками в один результат, дополняя каждую строку (кроме
    # последней) переносом строки '\n'
    for string in strings:
        if string is not strings[-1]:
            result += ' '.join(string) + '\n'
        else:
            result += ' '.join(string)

    print(result)
    return result


# TESTS:
if __name__ == '__main__':
    # justify('123 45 6', 7)  # -> '123  45\n6'
    justify('Lorem ipsum dolor sit amet, consectetur adipiscing elit. Vestibulum sagittis dolor mauris, at elementum ligula tempor eget. In quis rhoncus nunc, at aliquet orci.', 30)
    # justify('Also you can always take a look at how justification works in your text editor or directly in HTML (css: text-align: justify).', 40)
    # justify('LooooooooongWordOf30Characters LoooooooongWordOf29Characters LooooooongWordOf28Characters Lorem ipsum dolor sit. Vestibulum sagittis dolor mauri', 30)
