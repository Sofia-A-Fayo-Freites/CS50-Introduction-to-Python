from tabulate import tabulate
import sys
import csv

if len(sys.argv) == 2:
    file = sys.argv[1]
    try:
        if file.endswith(".csv"):
            with open(file) as menu:
                table = list(csv.reader(menu))
                headers = table.pop(0)
                print(tabulate(table, headers, tablefmt="grid"))
        else:
            sys.exit("Not a CSV file")
    except FileNotFoundError:
        sys.exit("File does not exist")
elif len(sys.argv) < 2:
    sys.exit("Too few command-line arguments")
elif len(sys.argv) > 2:
    sys.exit("Too many command-line arguments")