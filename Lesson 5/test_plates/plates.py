def main():
    s = input("Plate: ")

    if is_valid(s) == True:
        print("Valid")
    else:
        print("Invalid")

def is_valid(s):
    if s.isalnum():
        if s.isalpha():
            if len(s) >= 2 and len(s) <= 6:
                return True
            else:
                return False

        elif s.isalnum():
            if s[0:2].isalpha():
                if len(s) >= 2 and len(s) <= 6:
                    if czero(s) == True:
                        if calpha(s) == True:
                            return True
                        else:
                            return False
                    else:
                        return False
                else:
                    return False
            else:
                return False
    else:
        return False

def digit(s):
    digit = ""
    for char in s:
       if char.isdigit():
           digit += char
    return digit

def czero(s):
    if digit(s).startswith("0"):
        return False
    else:
        return True

def calpha(s):
    result = True
    for char in range(len(s) - 1):
        if s[char].isdigit() and s[char + 1].isalpha():
            result = False
    return result

if __name__ == "__main__":
    main()