import random
import sys

def main():
    while True:
        n = input("Level: ")
        if n.isalpha():
            continue
        if n.isdigit():
            if int(n) < 0:
                continue
            if int(n) > 0:
                guessing(n)
                break
    sys.exit()

def guessing(n):
    m = random.randint(1, int(n))
    while True:
        guess = input("Guess: ")
        if guess.isalpha():
            continue
        if guess.isdigit():
            if int(guess) < m:
                print("Too small!")
            if int(guess) > m:
                print("Too large!")
            if int(guess) == m:
                print("Just right!")
                break

main()