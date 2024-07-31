import sys

def main():
    if len(sys.argv) == 2:
        file = sys.argv[1]
        try:
            if file.endswith(".py"):
                print(program_reader(file))
            else:
                sys.exit("Not a Python file")
        except FileNotFoundError:
            sys.exit("File does not exist")
    elif len(sys.argv) < 2:
        sys.exit("Too few command-line arguments")
    elif len(sys.argv) > 2:
        sys.exit("Too many command-line arguments")

def program_reader(file):
    lines = []
    with open(file) as program:
        for line in program:
            if not line.strip().startswith("#") and line.strip() != "":
                lines.append(line)

    counter = 0
    n = len(lines)
    counter += n
    return counter

if __name__ == "__main__":
    main()