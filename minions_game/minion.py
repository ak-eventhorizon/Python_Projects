def minion_game(string: str) -> None:
    """Player for a minion game

        side: \n
        'c' - consonants (согласные) \n
        'v' - vowels (гласные) \n

        Подход: количество подстрок, начинающихся с определенной буквы в строке равно
        длине подстроки от этой буквы до конца строки (т.е. длина всей строки минус индекс текущей буквы).
        Например, берем подстроку "ANANA"
        в стоке "BANANA". Количество подстрок в ней = 5 (6 (длина строки) - 1 (индекс первой "A")):
        ANANA
        ANAN
        ANA
        AN
        A
        """

    score_kevin = 0  # гласные
    score_stuart = 0  # согласные

    for i in range(len(string)):
        if string[i] in 'AEIOU':
            score_kevin += len(string) - i
        else:
            score_stuart += len(string) - i

    if score_kevin == score_stuart:
        print('Draw')
    elif score_kevin > score_stuart:
        print('Kevin', score_kevin)
    else:
        print('Stuart', score_stuart)


if __name__ == '__main__':
    # minion_game('BANANA')  # -> Stuart 12
    # minion_game('BAAA')  # -> Kevin 6
    # minion_game('CRUSIFICTIONATION')  # -> Stuart 89
    # minion_game('ABBA')  # -> Draw

    with open('long.txt', 'r') as file:
        long_str = file.read().replace('\n', '')
    import time
    start_time = time.time()

    minion_game(long_str)  # -> Kevin 400173457964

    duration = time.time() - start_time  # измерение времени выполнение данного кейса
    print(f'--- {duration} seconds ---')
