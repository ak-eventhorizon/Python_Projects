def factorial(n: int) -> int:
    """Возвращает факториал числа n.

    5! = 5*4*3*2*1

    factorial(5) -> 120
    """
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)


def fact_string_2_dec(string: str) -> int:
    # индекс в строке является основанием СС для расчета (A->10, C->12)
    bases = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    # реверсирование строки, чтобы старшинство разрядов было выстроено правильно
    string = string[::-1]
    result = 0

    for i in range(len(string)):
        result += bases.index(string[i]) * factorial(i)

    return result


def dec_2_fact_string(dec: int) -> str:
    """
    463 -> '341010'   \n

    Approach: \n
    dec / counter   = next-dec, remain \n
    463 / 1         = 463,      remain 0 \n
    463 / 2         = 231,      remain 1 \n
    231 / 3         = 77,       remain 0 \n
    77 / 4          = 19,       remain 1 \n
    19 / 5          = 3,        remain 4 \n
    3 / 6           = 0,        remain 3 \n

    The process terminates when the quotient reaches zero. \n
    Reading the remainders backward gives 3:4:1:0:1:0.
    """
    bases = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    counter = 1
    result = ''

    while True:
        dec, remain = divmod(dec, counter)
        counter += 1
        result += bases[remain]

        if dec == 0:
            break

    return result[::-1]


# TESTS:
# print(fact_string_2_dec('ZYXWVUTSRQPONMLKJIHGFEDCBA9876543210'))
# print(fact_string_2_dec('ONMLKJIHGFEDCBA9876543210'))
# print(fact_string_2_dec('341010'))

# print(dec_2_fact_string(371993326789901217467999448150835199999999))
# print(dec_2_fact_string(15511210043330985983999999))
# print(dec_2_fact_string(463))
