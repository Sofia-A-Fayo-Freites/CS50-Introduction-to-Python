def main():
    time = input("What time is it? ")

    converted_time = convert(time)

    if 7.0 <= converted_time <= 8.0:
        print("breakfast time")
    elif 12.0 <= converted_time <= 13.0:
        print("lunch time")
    elif 18.0 <= converted_time <= 19.0:
        print("dinner time")

def convert(time):
    hours, minutes = time.removesuffix("a.m.").removesuffix("p.m.").split(":")
    return float(int(hours) + int(minutes) / 60)


if __name__ == "__main__":
    main()
