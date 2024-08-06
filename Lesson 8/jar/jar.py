class Jar:
    def __init__(self, capacity=12):
        if capacity < 0:
            raise ValueError
        self._capacity = capacity
        self._size = 0

    def __str__(self):
        return "🍪" * self._size

    def deposit(self, n):
        if n < 0:
            raise ValueError
        if self._size + n > self._capacity:
            raise ValueError
        self._size += n

    def withdraw(self, n):
        if n < 0:
            raise ValueError
        if n > self._size:
            raise ValueError
        self._size -= n

    @property
    def capacity(self):
        return self._capacity

    @property
    def size(self):
        return self._size

def main():
    jar = Jar()
    print(f"Jar capacity: {jar.capacity}{jar}")
    print(f"Number of cookies in the cookie jar: {jar.size}{jar}")
    input_deposit(jar)
    input_withdraw(jar)
    current(jar)

def input_deposit(jar):
    while True:
        _deposit = input("Would you like to deposit cookies? Say YES or NO ")
        if _deposit != "YES" and _deposit != "NO":
            print("Please give a valid answer")
            continue
        if _deposit == "YES":
            depo = input("How many cookies?: ")
            try:
                depo = int(depo)
                jar.deposit(depo)
                break
            except ValueError:
                print(f"{depo} is not a valid number of cookies")
        else:
            return

def input_withdraw(jar):
    while True:
        _withdraw = input("Would you like to withdraw cookies? Say YES or NO ")
        if _withdraw != "YES" and _withdraw != "NO":
            print("Please give a valid answer")
            continue
        if _withdraw == "YES":
            withdr = input("How many cookies?: ")
            try:
                withdr = int(withdr)
                jar.withdraw(withdr)
                break
            except ValueError:
                print(f"{withdr} is not a valid number of cookies")
        else:
            return

def current(jar):
    print(f"Number of cookies in the cookie jar: {jar.size} {jar}")

if __name__ == "__main__":
    main()
