import re
import sys

def main():
    print(convert(input("Hours: ")))

def convert(s):
    american_hour = re.search(r"(1?[0-9])(:([0-5]?[0-9]))? (AM|PM) to (1?[0-9])(:([0-5]?[0-9]))? (AM|PM)", s)
    if not american_hour:
        raise ValueError

    start_hour = int(american_hour.group(1))
    start_minutes = int(american_hour.group(3)) if american_hour.group(3) else 0
    start_period = american_hour.group(4)
    end_hour = int(american_hour.group(5))
    end_minutes = int(american_hour.group(7)) if american_hour.group(7) else 0
    end_period = (american_hour.group(8))

    if start_period == "AM" and end_period == "PM":
        if start_hour == 12:
            start_hour = 0
        elif end_hour != 12:
            end_hour = end_hour + 12
        elif end_hour == 12:
            end_hour = 12
        elif end_minutes is None:
            end_minutes = 0
    elif start_period == "PM" and end_period == "AM":
        if start_hour == 12:
            start_hour = 12
        elif start_hour != 12:
            start_hour = start_hour + 12
        elif end_hour == 12:
            end_hour = 0
        elif end_minutes is None:
            end_minutes = 0

    world_hour = f"{start_hour:02}:{start_minutes:02} to {end_hour:02}:{end_minutes:02}"
    return world_hour

if __name__ == "__main__":
    main()