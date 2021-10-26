def main(s: str) -> str:
    """
    You are given a string S.
    S contains alphanumeric characters only.
    Your task is to sort the string S in the following manner:

    All sorted lowercase letters are ahead of uppercase letters.
    All sorted uppercase letters are ahead of digits.
    All sorted odd digits are ahead of sorted even digits.

    Input Format
    A single line of input contains the string S.

    Output Format
    Output the sorted string S.

    Sample Input:
    Sorting1234

    Sample Output:
    ginortS1324
    """

    lower = str()
    upper = str()
    odd = str()
    even = str()

    for char in sorted(s):
        if char.islower():
            lower += char
        elif char.isupper():
            upper += char
        elif char.isdigit():
            if int(char) % 2 == 0:
                even += char
            elif int(char) % 2 == 1:
                odd += char

    return ''.join(lower + upper + odd + even)


if __name__ == '__main__':
    # user_input = input()
    user_input = 'Sorting1234'
    print(main(user_input))
