def decode_morse(morse_code: str) -> str:
    """
    Decode morse string sequence to human-readable.

    :param morse_code: string "... --- ..."
    :return:  string "SOS"
    """
    morse = {
        '.-':           'A',
        '-...':         'B',
        '-.-.':         'C',
        '-..':          'D',
        '.':            'E',
        '..-.':         'F',
        '--.':          'G',
        '....':         'H',
        '..':           'I',
        '.---':         'J',
        '-.-':          'K',
        '.-..':         'L',
        '--':           'M',
        '-.':           'N',
        '---':          'O',
        '.--.':         'P',
        '--.-':         'Q',
        '.-.':          'R',
        '...':          'S',
        '-':            'T',
        '..-':          'U',
        '...-':         'V',
        '.--':          'W',
        '-..-':         'X',
        '-.--':         'Y',
        '--..':         'Z',
        '.-.-.-':       '.',
        '--..--':       ',',
        '..--..':       '?',
        '-.-.--':       '!',
        '-..-.':        '/',
        '.--.-.':       '@',
        '.----':        '1',
        '..---':        '2',
        '...--':        '3',
        '....-':        '4',
        '.....':        '5',
        '-....':        '6',
        '--...':        '7',
        '---..':        '8',
        '----.':        '9',
        '-----':        '0',
        '...---...':    'SOS',
    }

    codes = morse_code.split(' ')

    for i in range(len(codes)):
        if codes[i]:
            codes[i] = morse[codes[i]]

    result = '_'.join(codes)  # "H_E_Y___J_U_D_E"
    result = result.replace('___', ' ')  # "H_E_Y J_U_D_E"
    result = result.replace('_', '')  # "HEY JUDE"

    return result.strip()


def decode_bits(bits: str) -> str:
    """
    Decode bits-string to morse string sequence.

    "Dot" – is 1 time unit long.
    "Dash" – is 3 time units long.
    Pause between dots and dashes in a character – is 1 time unit long.
    Pause between characters inside a word – is 3 time units long.
    Pause between words – is 7 time units long.

    :param bits: '111000111111111000111'
    :return: '.-.'
    """

    # отсекание начальных и конечных нулей как не значащих
    bits = bits.strip('0')

    # Считать точкой последовательность из единиц, без возможности определить разделители - '1111111'
    if '0' not in bits:
        return '.'

    # Определение единицы времени (time unit), т.е. минимального количества битов,
    # кодирующих одну точку. На ее основании можно минифицировать всю последовательность:
    # 10101 - соответствует "..." (S) с частотой 1
    # 111000111000111 - также соответствует "..." (S) с частотой 3 и ее можно свернуть в 10101
    removed_0 = bits.replace('0', ' ').split()
    removed_1 = bits.replace('1', ' ').split()
    min_length_0 = len(min(removed_0)) if removed_0 else 1
    min_length_1 = len(min(removed_1)) if removed_1 else 1
    time_unit = min(min_length_0, min_length_1)

    # разделение на блоки, соответствующие отдельным символам
    chars = bits.split('000' * time_unit)  # Pause between characters inside a word = 3 time unit

    for i in range(len(chars)):
        if chars[i]:
            chars[i] = chars[i].replace('111' * time_unit, '-')  # Dash = 3 time unit
            chars[i] = chars[i].replace('1' * time_unit, '.')   # Dot = 1 time unit
            chars[i] = chars[i].replace('0' * time_unit, '')  # Pause between Dots and Dashes = 1 time unit
        else:
            chars[i] = ' '  # '' - equal space ' ' between words

    return ' '.join(chars)


# TESTS:

# print(decode_bits('1'))  # -> E (.)
# print(decode_bits('111'))  # -> E (.) - считать точкой последов. 1 без возможности определить разделители
# print(decode_bits('1111111'))  # -> E (.) считать точкой последов. 1 без возможности определить разделители

# print(decode_bits('10101'))  # -> S (...)
# print(decode_bits('111000111000111'))  # -> S (...)

# print(decode_bits('10101010001000111010111011100000001011101110111000101011100011101010001'))
# print(decode_bits('1100110011001100000011000000111111001100111111001111110000000000000011\
# 001111110011111100111111000000110011001111110000001111110011001100000011'))

# print(decode_morse('.... . -.--   .--- ..- -.. .'))  # -> "HEY JUDE"
# print(decode_morse('... --- ... -.-.--'))  # -> "SOS!"
# print(decode_morse('...---...'))  # -> "SOS"

# bit_string = '110011001100110000001100000011111100110011111100111111000000000000001100\
# 1111110011111100111111000000110011001111110000001111110011001100000011'
# print(decode_morse(decode_bits(bit_string)))
