import random

def main():
    level = get_level()
    score = 0
    for _ in range(10):
        p = generate_problem(level)
        if p < 3:
            score += 1
    print(f"Score: {score}")

def get_level():
    while True:
        level = input("Level: ")
        if level.isalpha():
            continue
        if level.isdigit():
            if int(level) < 1 or int(level) > 3:
                continue
            else:
                return level

def generate_integer(level):
    if level.isalpha():
        raise ValueError
    intlevel = int(level)
    if intlevel < 1 or intlevel > 3:
        raise ValueError
    if intlevel == 1:
        return random.randrange(0, 10)
    if intlevel == 2:
        return random.randrange(10, 100)
    if intlevel == 3:
        return random.randrange(100, 1000)

def generate_problem(level):
    n = generate_integer(level)
    m = generate_integer(level)
    p = 1
    while p <= 3:
        answer = input(f"{n} + {m} = ")
        result = n + m
        if answer.isalpha():
            print("EEE")
            p += 1
            continue
        if answer.isdigit():
            if int(answer) != result:
                print("EEE")
                p += 1
                continue
            if int(answer) == result:
                break
    else:
        print(f"{n} + {m} = {result}")
    return p

if __name__ == "__main__":
    main()