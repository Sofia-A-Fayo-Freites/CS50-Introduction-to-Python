
entrees = {
    "Baja Taco": "4.25",
    "Burrito": "7.50",
    "Bowl": "8.50",
    "Nachos": "11.00",
    "Quesadilla": "8.50",
    "Super Burrito": "8.50",
    "Super Quesadilla": "9.50",
    "Taco": "3.00",
    "Tortilla Salad": "8.00"
}


def main():
    full_price = 0

    while True:
        try:
            order = input("Item: ")
            o = order.title()

            full_price += float(entrees[o])
            print(f"${full_price:.2f}")
        except KeyError:
            pass
        except EOFError:
            pass
            print("\n")
            break

main ()