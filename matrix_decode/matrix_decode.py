"""
The matrix script is a NxM grid of strings.
It consists of alphanumeric characters, spaces and symbols (!,@,#,$,%,&).

To decode the script, we need to read each column and select only the alphanumeric
characters and connect them. Reads the column from top to bottom and starts
reading from the leftmost column.

If there are symbols or spaces between two alphanumeric characters of the decoded script,
then need to replaces them with a single space ' ' for better readability.

FORBIDDEN to use 'if' conditions for decoding.
"""
import re


def decode_matrix(mtrx: list) -> None:

    transposed_matrix = list(zip(*mtrx))  # перевернутая на 90 градусов матрица
    stringed_matrix = ''.join([''.join(s) for s in transposed_matrix])  # матрица, склеенная в одну строку

    # замена на пробел последовательности не цифро-буквенных символов, заключенных между двумя цифро-буквенными
    result = re.sub(r'(\w)(\W)+(\w)', r'\1 \3', stringed_matrix)

    print(result)


if __name__ == '__main__':

    matrix = ['Tsi',
              'h%x',
              'i #',
              'sM ',
              '$a ',
              '#t%',
              'ir!']

    decode_matrix(matrix)
