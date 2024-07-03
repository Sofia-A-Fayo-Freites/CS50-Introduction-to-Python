def main():
    name = input("camelCase: ")
    print("snake_case:", convert(name))

def convert(name):
    result = ""
    for letter in name:
        if letter.isupper():
           result += "_" + letter.lower()
        else:
            result += letter
    return result

main()