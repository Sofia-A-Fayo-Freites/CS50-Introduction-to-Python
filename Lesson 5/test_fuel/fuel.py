def main():
    while True:
        fraction = input("Fraction: ")
        try:
            percentage = convert(fraction)
            print(gauge(percentage))
            break
        except (ValueError, ZeroDivisionError):
            continue

def convert(fraction):
    m = fraction.split("/")
    try:
        X = int(m[0])
        Y = int(m[1])
        if Y == 0:
            raise ZeroDivisionError
        if X > Y:
            raise ValueError
        result = X / Y
        return result * 100
    except ValueError:
        return ValueError

def gauge(percentage):
    n = percentage
    if n <= 1:
        return("E")
    elif n >= 99:
        return("F")
    else:
        return "{:.0f}%".format(percentage)

if __name__ == "__main__":
    main()