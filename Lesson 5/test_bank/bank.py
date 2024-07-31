def main():
    greeting = input("Greet us and we will pay you! ")

    print(value(greeting))


def value(greeting):
    if greeting.casefold().strip().startswith("hello"):
        return(0)
    elif greeting.casefold().strip().startswith("h"):
        return(20)
    else:
        return(100)

if __name__ == "__main__":
    main()
