import re
import sys


def main():
    print(convert(input("Hours: ")))


def convert(s):
    pattern = r'^\s*(\d{1,2}:\d{2}|\d{1,2}) (AM|PM) to (\d{1,2}:\d{2}|\d{1,2}) (AM|PM)\s*$'

    match = re.search(pattern, s)

    if not match:
        raise ValueError("Invalid time format")

    start_time, start_period, end_time, end_period = match.groups()

    start_24 = to_24_hour(start_time, start_period)

    end_24 = to_24_hour(end_time, end_period)

    return f"{start_24} to {end_24}"


def to_24_hour(time, period):
    if ':' in time:
        hours, minutes = map(int, time.split(':'))
    else:
        hours = int(time)
        minutes = 0

    if hours < 1 or hours > 12 or minutes < 0 or minutes >= 60:
        raise ValueError("Invalid time")

    if period == 'AM':
        if hours == 12:
            hours = 0
    elif period == 'PM':
        if hours != 12:
            hours += 12

    return f"{hours:02}:{minutes:02}"


if __name__ == "__main__":
    main()
