def main():

    text = input("Input: ")

    print("Outcome: ", convert(text))


def convert(text):
    vowel = ["a", "e", "i", "o", "u", "A", "E", "I", "O", "U"]
    result = ""
    for letter in text:
        if letter not in vowel:
            result += letter
        else:
            ""
    return result

main()
