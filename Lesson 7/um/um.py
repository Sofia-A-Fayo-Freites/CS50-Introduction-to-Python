import re

def main():
    print(count(input("Text: ")))

def count(s):
    search = re.findall(r"\bum\b", s, re.IGNORECASE)
    count = len(search)
    return count

if __name__ == "__main__":
    main()