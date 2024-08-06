import sys
from datetime import date, datetime
import inflect
p = inflect.engine()

def main():
    birth = input("Date of Birth: ")
    print(f"{calculate_minutes(birth)} minutes")

def calculate_minutes(birth):
    try:
        year = int(birth.split("-")[0])
        month = int(birth.split("-")[1])
        day = int(birth.split("-")[2])
        conv_birth = date(year, month, day)
    except ValueError:
        sys.exit("Invalid date")

    datetime_birth = datetime.combine(conv_birth, datetime.min.time())
    today = datetime.combine(date.today(), datetime.min.time())
    sub = today - datetime_birth
    days = sub.days
    minutes = days * 1440
    words = p.number_to_words(minutes, andword="").capitalize()
    return words

if __name__ == "__main__":
    main()