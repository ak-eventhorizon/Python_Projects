def validate_uid(s: str) -> bool:
    """
    Check if string is valid UID

    A valid UID must follow the rules below:
    1) It must contain at least 2 uppercase English alphabet characters.
    2) It must contain at least 3 digits (0-9).
    3) It should only contain alphanumeric characters (a-z,A-Z & 0-9).
    4) No character should repeat.
    5) There must be exactly 10 characters in a valid UID.

    :param s:
    :return:
    """

    uppercase = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    lowercase = 'abcdefghijklmnopqrstuvwxyz'
    digits = '0123456789'

    presented_upper = set()
    presented_lower = set()
    presented_digits = set()

    c1 = False  # condition 1 - contain at least 2 uppercase English alphabet characters
    c2 = False  # condition 2 - contain at least 3 digits (0-9)
    c3 = False  # condition 3 - only contain alphanumeric characters (a-z,A-Z & 0-9)
    c4 = False  # condition 4 - no character should repeat
    c5 = False  # condition 5 - there must be exactly 10 characters

    for char in s:
        if char in uppercase:
            presented_upper.add(char)
        elif char in lowercase:
            presented_lower.add(char)
        elif char in digits:
            presented_digits.add(char)
        else:
            return False

    if len(presented_upper) >= 2:
        c1 = True

    if len(presented_digits) >= 3:
        c2 = True

    if len(presented_upper) + len(presented_lower) + len(presented_digits) == len(s) == 10:
        c3 = True
        c4 = True
        c5 = True

    uid_is_valid = c1 and c2 and c3 and c4 and c5

    return uid_is_valid


if __name__ == '__main__':

    inputs = ['B1CD102354', 'B1CDEF2354', 'B-CDEF2354', 'BBCDEF2354', 'B1CDE']

    for i in inputs:
        if validate_uid(i):
            print('Valid')
        else:
            print('Invalid')
