def dec_to_base(num: int, base: int) -> str:
    """Перевод десятичного числа в систему счисления по основанию base."""

    alphabet = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    result = ''
    while num > 0:
        num, m = divmod(num, base)
        result += alphabet[m]
    return result[::-1]


def print_formatted(number: int):
    """Форматированный вывод чисел от 1 до number в четырех системах счисления."""

    for i in range(1, number+1):
        width = len(dec_to_base(number, 2))

        num_dec = str(i).rjust(width, ' ')
        num_bin = dec_to_base(i, 2).rjust(width, ' ')
        num_oct = dec_to_base(i, 8).rjust(width, ' ')
        num_hex = dec_to_base(i, 16).rjust(width, ' ')

        print(num_dec, num_oct, num_hex, num_bin)


if __name__ == '__main__':
    print_formatted(15)
