import inflect

p = inflect.engine()

list_of_friends = []

def main():
    while True:
        try:
            name = input("Name: ")

            add_friend(list_of_friends, name)

        except EOFError:
            print(f"Adieu, adieu, to {friends(list_of_friends)}")
            break

def add_friend(list_of_friends, name):
    list_of_friends.append(name)
    return list_of_friends

def friends(list_of_friends):
    mylist = p.join(list_of_friends)
    return mylist

main()