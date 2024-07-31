import sys
import csv

if len(sys.argv) == 3:
    b_file = sys.argv[1]
    a_file = sys.argv[2]
    try:
        with open(b_file, "r") as before, open(a_file, "w") as a_file:
            reader = csv.DictReader(before)
            names = []
            surnames = []
            houses = []
            for row in reader:
                split_name = row["name"].split(", ")
                names.append(split_name[1])
                surnames.append(split_name[0])
                list_of_houses = row["house"]
                houses.append(list_of_houses)
            writer = csv.DictWriter(a_file, fieldnames=["first", "last", "house"])
            writer.writeheader()
            for name, surname, house in zip(names, surnames, houses):
                writer.writerow({"first": name, "last": surname, "house": house})
    except FileNotFoundError:
        sys.exit(f"Could not read {b_file}")
elif len(sys.argv) < 3:
    sys.exit("Too few command-line arguments")
elif len(sys.argv) > 3:
    sys.exit("Too many command-line arguments")