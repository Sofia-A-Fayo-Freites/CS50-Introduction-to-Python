def main():
    fuel = input("Fraction: ")

    print(print_text(fuel))

def print_text(fuel):
    n = result(fuel)
    if float(n) <= 0.01:
        return("E")
    if float(n) >= 0.99:
        return("F")
    else:
        return("{:.0f}%".format(n * 100))

def result(fuel):
    m = fuel.split("/")
    try:
        X = int(m[0])
        Y = int(m[1])
        if X > Y:
            return main()
        result = X / Y
        return result
    except (ValueError, ZeroDivisionError):
        return main()


main()
