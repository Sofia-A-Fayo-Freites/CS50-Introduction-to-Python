def main():
    shopping_list = []

    while True:
        try:
            item = input().upper()
            add_entry(shopping_list, item)

        except EOFError:
            counted_items = count_item(shopping_list)
            format_list(counted_items)
            break

def add_entry(shopping_list, item):
    shopping_list.append(item)
    return shopping_list

def count_item(shopping_list):
    count_item = {}
    for item in shopping_list:
        if item in count_item:
            count_item[item] += 1
        else:
            count_item[item] = 1
    return count_item

def format_list(counted_items):
    sorted_items = sorted(counted_items.items())
    for key, value in sorted_items:
        print(value, key)


main()