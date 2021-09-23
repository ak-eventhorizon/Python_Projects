def format_duration(seconds: int) -> str:
    """Transform number of seconds to duration string

    Example:
        format_duration(431536021) -> 13 years, 249 days, 15 hours, 7 minutes and 1 second
    """

    if seconds == 0:
        return 'now'

    sec_in_year = 31536000
    sec_in_day = 86400
    sec_in_hour = 3600
    sec_in_min = 60

    result_struct = dict()
    result_string = str()

    if seconds // sec_in_year:
        if seconds // sec_in_year > 1:
            result_struct['years'] = seconds // sec_in_year
        else:
            result_struct['year'] = seconds // sec_in_year
        seconds = seconds % sec_in_year

    if seconds // sec_in_day:
        if seconds // sec_in_day > 1:
            result_struct['days'] = seconds // sec_in_day
        else:
            result_struct['day'] = seconds // sec_in_day
        seconds = seconds % sec_in_day

    if seconds // sec_in_hour:
        if seconds // sec_in_hour > 1:
            result_struct['hours'] = seconds // sec_in_hour
        else:
            result_struct['hour'] = seconds // sec_in_hour
        seconds = seconds % sec_in_hour

    if seconds // sec_in_min:
        if seconds // sec_in_min > 1:
            result_struct['minutes'] = seconds // sec_in_min
        else:
            result_struct['minute'] = seconds // sec_in_min
        seconds = seconds % sec_in_min

    if seconds < sec_in_min:
        if seconds > 1:
            result_struct['seconds'] = seconds
        elif seconds == 1:
            result_struct['second'] = seconds

    for key in result_struct:
        if len(result_struct) == 1:
            result_string += f'{result_struct[key]} {key}'
        else:
            # if key represent last element in dictionary
            if key == list(result_struct.keys())[-1]:
                result_string = result_string[:-2] + f' and {result_struct[key]} {key}'
            else:
                result_string += f'{result_struct[key]} {key}, '

    return result_string


# TESTS:
if __name__ == '__main__':
    print(format_duration(0) == 'now')
    print(format_duration(1) == '1 second')
    print(format_duration(62) == '1 minute and 2 seconds')
    print(format_duration(120) == '2 minutes')
    print(format_duration(3600) == '1 hour')
    print(format_duration(3662) == '1 hour, 1 minute and 2 seconds')
    print(format_duration(132030240) == '4 years, 68 days, 3 hours and 4 minutes')
    print(format_duration(1132030255) == '35 years, 327 days, 4 hours, 50 minutes and 55 seconds')
